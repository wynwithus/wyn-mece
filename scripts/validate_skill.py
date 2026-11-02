#!/usr/bin/env python3
"""Static validator for the portable MECE Agent Skill package.

Uses only the Python standard library. It validates package structure,
frontmatter constraints, local Markdown links, JSON evals, Python syntax,
and the finite-partition fixtures. It does not claim runtime model quality.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


@dataclass
class Check:
    name: str
    passed: bool
    detail: str


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) < 3 or lines[0].strip() != "---":
        raise ValueError("SKILL.md must begin with YAML frontmatter")
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("SKILL.md frontmatter is not closed") from exc

    fm_lines = lines[1:end]
    data: dict[str, Any] = {}
    current_map: dict[str, Any] | None = None
    for raw in fm_lines:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        if ":" not in raw:
            raise ValueError(f"unsupported frontmatter line: {raw}")
        key, value = raw.strip().split(":", 1)
        value = value.strip()
        if indent == 0:
            if value == "":
                current_map = {}
                data[key] = current_map
            else:
                data[key] = value.strip('"\'')
                current_map = None
        else:
            if current_map is None:
                raise ValueError(f"unexpected nested frontmatter line: {raw}")
            current_map[key] = value.strip('"\'')
    body = "\n".join(lines[end + 1 :])
    return data, body


def local_markdown_links(root: Path) -> list[tuple[Path, str, Path]]:
    missing: list[tuple[Path, str, Path]] = []
    for md in root.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for target in LINK_RE.findall(text):
            target = target.split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (md.parent / target).resolve()
            if not resolved.exists():
                missing.append((md, target, resolved))
    return missing


def validate_json_files(root: Path) -> tuple[list[str], list[str]]:
    parsed: list[str] = []
    errors: list[str] = []
    for path in sorted(root.rglob("*.json")):
        try:
            json.loads(path.read_text(encoding="utf-8"))
            parsed.append(str(path.relative_to(root)))
        except Exception as exc:  # noqa: BLE001 - validator should report all files
            errors.append(f"{path.relative_to(root)}: {exc}")
    return parsed, errors


def validate_python_files(root: Path) -> tuple[list[str], list[str]]:
    parsed: list[str] = []
    errors: list[str] = []
    for path in sorted(root.rglob("*.py")):
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            parsed.append(str(path.relative_to(root)))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.relative_to(root)}: {exc}")
    return parsed, errors


def validate_eval_definitions(root: Path) -> list[str]:
    errors: list[str] = []
    trigger_path = root / "evals" / "trigger_queries.json"
    output_path = root / "evals" / "evals.json"

    triggers = json.loads(trigger_path.read_text(encoding="utf-8"))
    if not isinstance(triggers, list):
        errors.append("trigger_queries.json must contain a list")
    else:
        ids: set[str] = set()
        positives = negatives = 0
        for idx, item in enumerate(triggers):
            if not isinstance(item, dict):
                errors.append(f"trigger case {idx} is not an object")
                continue
            case_id = item.get("id")
            if not isinstance(case_id, str) or not case_id:
                errors.append(f"trigger case {idx} lacks a non-empty id")
            elif case_id in ids:
                errors.append(f"duplicate trigger id: {case_id}")
            else:
                ids.add(case_id)
            if not isinstance(item.get("query"), str) or not item["query"].strip():
                errors.append(f"trigger case {case_id or idx} lacks a query")
            if not isinstance(item.get("should_trigger"), bool):
                errors.append(f"trigger case {case_id or idx} lacks Boolean should_trigger")
            elif item["should_trigger"]:
                positives += 1
            else:
                negatives += 1
        if positives < 10 or negatives < 10:
            errors.append(f"trigger suite needs at least 10 positive and 10 negative cases; got {positives}/{negatives}")

    outputs = json.loads(output_path.read_text(encoding="utf-8"))
    cases = outputs.get("evals") if isinstance(outputs, dict) else None
    if not isinstance(cases, list):
        errors.append("evals.json must contain an evals list")
    else:
        ids = set()
        for idx, item in enumerate(cases):
            if not isinstance(item, dict):
                errors.append(f"output case {idx} is not an object")
                continue
            case_id = item.get("id")
            if not isinstance(case_id, str) or not case_id:
                errors.append(f"output case {idx} lacks a non-empty id")
                continue
            if case_id in ids:
                errors.append(f"duplicate output id: {case_id}")
            ids.add(case_id)
            for field in ("prompt", "expected_output"):
                if not isinstance(item.get(field), str) or not item[field].strip():
                    errors.append(f"output case {case_id} lacks {field}")
            assertions = item.get("assertions")
            if not isinstance(assertions, list) or not assertions or not all(isinstance(x, str) and x.strip() for x in assertions):
                errors.append(f"output case {case_id} needs non-empty string assertions")
            for rel in item.get("files", []):
                if not (root / rel).exists():
                    errors.append(f"output case {case_id} references missing file: {rel}")
    return errors


def run_validator_fixture(root: Path, fixture: str, expect_success: bool) -> Check:
    validator = root / "scripts" / "validate_partition.py"
    fixture_path = root / "evals" / "files" / fixture
    proc = subprocess.run(
        [sys.executable, str(validator), str(fixture_path)],
        text=True,
        capture_output=True,
        check=False,
    )
    passed = (proc.returncode == 0) if expect_success else (proc.returncode != 0)
    detail = f"exit={proc.returncode}; expected {'0' if expect_success else 'non-zero'}"
    if not passed and proc.stderr.strip():
        detail += f"; stderr={proc.stderr.strip()}"
    return Check(f"validator_fixture:{fixture}", passed, detail)


def validate(root: Path) -> dict[str, Any]:
    checks: list[Check] = []
    skill = root / "SKILL.md"

    checks.append(Check("required:SKILL.md", skill.exists(), str(skill)))
    required_dirs = ["references", "scripts", "evals", "assets", "agents"]
    for directory in required_dirs:
        checks.append(Check(f"required_dir:{directory}", (root / directory).is_dir(), str(root / directory)))

    try:
        fm, _ = parse_frontmatter(skill)
        name = str(fm.get("name", ""))
        description = str(fm.get("description", ""))
        metadata = fm.get("metadata") if isinstance(fm.get("metadata"), dict) else {}
        checks.extend(
            [
                Check("frontmatter:name_format", bool(NAME_RE.fullmatch(name)), name),
                Check("frontmatter:name_matches_directory", name == root.name, f"name={name}; directory={root.name}"),
                Check("frontmatter:description_present", bool(description.strip()), f"chars={len(description)}"),
                Check("frontmatter:description_length", len(description) <= 1024, f"chars={len(description)}"),
                Check("frontmatter:version_present", bool(metadata.get("version")), str(metadata.get("version", ""))),
            ]
        )
    except Exception as exc:  # noqa: BLE001
        checks.append(Check("frontmatter:parse", False, str(exc)))

    line_count = len(skill.read_text(encoding="utf-8").splitlines()) if skill.exists() else 0
    checks.append(Check("SKILL.md:under_500_lines", line_count < 500, f"lines={line_count}"))

    missing_links = local_markdown_links(root)
    checks.append(
        Check(
            "markdown:local_links_resolve",
            not missing_links,
            "; ".join(f"{p.relative_to(root)} -> {target}" for p, target, _ in missing_links) or "all local links resolve",
        )
    )

    parsed_json, json_errors = validate_json_files(root)
    checks.append(Check("json:parse", not json_errors, f"parsed={len(parsed_json)}; errors={json_errors}"))

    parsed_py, py_errors = validate_python_files(root)
    checks.append(Check("python:syntax", not py_errors, f"parsed={len(parsed_py)}; errors={py_errors}"))

    try:
        eval_errors = validate_eval_definitions(root)
    except Exception as exc:  # noqa: BLE001
        eval_errors = [str(exc)]
    checks.append(Check("evals:definitions", not eval_errors, "; ".join(eval_errors) or "valid"))

    checks.append(run_validator_fixture(root, "partition-pass.json", True))
    checks.append(run_validator_fixture(root, "partition-fail.json", False))
    checks.append(run_validator_fixture(root, "intervals-pass.json", True))
    checks.append(run_validator_fixture(root, "intervals-fail.json", False))

    passed = all(check.passed for check in checks)
    return {
        "skill_root": str(root),
        "static_validation_pass": passed,
        "checks": [asdict(c) for c in checks],
        "limitations": [
            "Static validation does not measure model activation accuracy or output quality.",
            "Runtime claims require fresh-session with-skill and without-skill evaluations in target clients.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()

    report = validate(args.root.resolve())
    rendered = json.dumps(report, indent=2)
    print(rendered)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    return 0 if report["static_validation_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
