"""Package the existing skill without rewriting its instructions or resources."""

from pathlib import Path
import hashlib
import shutil
import zipfile


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_VERSION = "3.2.4"
RESOURCE_DIRS = ("agents", "assets", "evals", "references", "scripts")


def skill_files():
    files = [ROOT / "SKILL.md", ROOT / "INSTALL.md", ROOT / "LICENSE", ROOT / "TERMS.md", ROOT / "CHANGELOG.md"]
    for directory in RESOURCE_DIRS:
        files.extend(path for path in (ROOT / directory).rglob("*")
                     if path.is_file() and "__pycache__" not in path.parts
                     and path.suffix not in {".pyc", ".pyo"}
                     and "artifacts" not in path.parts)
    return sorted(files)


def make_text_bundle():
    paths = [ROOT / "SKILL.md", ROOT / "TERMS.md", ROOT / "LICENSE"]
    for directory in ("references", "assets", "scripts"):
        paths.extend(path for path in (ROOT / directory).rglob("*")
                     if path.is_file() and path.suffix in {".md", ".yaml", ".py"}
                     and "__pycache__" not in path.parts)
    sections = [
        "WYN MECE\n\n"
        "Use the SKILL.md instructions below for my requests in this conversation. "
        "The remaining file sections contain its referenced resources.\n\n"
    ]
    for path in paths:
        relative = path.relative_to(ROOT).as_posix()
        sections.append(f"===== FILE: {relative} =====\n")
        sections.append(path.read_text(encoding="utf-8"))
        sections.append(f"\n===== END FILE: {relative} =====\n\n")
    return "".join(sections)


def build():
    output = ROOT / "dist"
    output.mkdir(exist_ok=True)
    (ROOT / "WYN-MECE.txt").write_text(make_text_bundle(), encoding="utf-8", newline="\n")
    with zipfile.ZipFile(output / "wyn-mece.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for path in skill_files():
            relative = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(f"wyn-mece/{relative}", date_time=(2026, 11, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    shutil.copyfile(output / "wyn-mece.zip", output / "wyn-mece.skill")
    for name in ("WYN-MECE.txt", "CHAT-INSTRUCTIONS.txt"):
        shutil.copyfile(ROOT / name, output / name)
    checksums = []
    for name in ("wyn-mece.zip", "wyn-mece.skill", "WYN-MECE.txt", "CHAT-INSTRUCTIONS.txt"):
        path = output / name
        checksums.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {name}\n")
    (output / "SHA256SUMS.txt").write_text("".join(checksums), encoding="utf-8", newline="\n")
    print(f"Built package {PACKAGE_VERSION}: ZIP, .skill, complete chat text, and checksums.")


if __name__ == "__main__":
    build()
