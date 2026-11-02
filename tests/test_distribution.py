"""Check packaging and preservation, without changing the original skill."""

import hashlib
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest
import zipfile


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("package_skill", ROOT / "tools/package_skill.py")
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)


def normalized(path):
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8")


class DistributionTests(unittest.TestCase):
    def test_original_instruction_body_is_preserved(self):
        manifest = json.loads((ROOT / "packaging/source-manifest.json").read_text(encoding="utf-8"))
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        body = text.split("---", 2)[2].encode("utf-8")
        self.assertEqual(hashlib.sha256(body).hexdigest(), manifest["source_body_sha256"])

    def test_original_supporting_files_are_preserved(self):
        manifest = json.loads((ROOT / "packaging/source-manifest.json").read_text(encoding="utf-8"))
        for relative, expected in manifest["original_files_sha256"].items():
            with self.subTest(path=relative):
                path = ROOT / relative
                data = path.read_bytes() if path.suffix == ".png" else normalized(path)
                self.assertEqual(hashlib.sha256(data).hexdigest(), expected)

    def test_only_allowed_frontmatter_fields_differ(self):
        manifest = json.loads((ROOT / "packaging/source-manifest.json").read_text(encoding="utf-8"))
        frontmatter = (ROOT / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
        preserved = "\n".join(line for line in frontmatter.splitlines()
                              if not line.startswith(("name:", "description:", "license:")))
        self.assertEqual(preserved, manifest["preserved_frontmatter"])

    def test_description_fits_documented_upload_limit(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        description = re.search(r"^description: (.+)$", text, re.MULTILINE).group(1)
        self.assertGreater(len(description), 0)
        self.assertLessEqual(len(description), 200)

    def test_complete_text_is_generated_without_rewriting(self):
        actual = (ROOT / "WYN-MECE.txt").read_text(encoding="utf-8")
        self.assertEqual(actual, package.make_text_bundle())
        self.assertIn((ROOT / "SKILL.md").read_text(encoding="utf-8"), actual)

    def test_archive_is_installable_and_keeps_all_source_files(self):
        archive_path = ROOT / "dist/wyn-mece.zip"
        with zipfile.ZipFile(archive_path) as archive:
            names = archive.namelist()
            self.assertTrue(all(name.startswith("wyn-mece/") for name in names))
            self.assertIn("wyn-mece/SKILL.md", names)
            self.assertFalse(any("__pycache__" in name or "_to_delete" in name for name in names))
            for path in package.skill_files():
                self.assertEqual(archive.read("wyn-mece/" + path.relative_to(ROOT).as_posix()), path.read_bytes())
            with tempfile.TemporaryDirectory() as directory:
                archive.extractall(directory)
                extracted = Path(directory) / "wyn-mece"
                for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", (extracted / "SKILL.md").read_text(encoding="utf-8")):
                    self.assertTrue((extracted / target).is_file(), target)

    def test_gemini_skill_is_the_same_archive(self):
        self.assertEqual((ROOT / "dist/wyn-mece.skill").read_bytes(), (ROOT / "dist/wyn-mece.zip").read_bytes())


if __name__ == "__main__":
    unittest.main()
