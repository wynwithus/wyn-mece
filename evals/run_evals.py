#!/usr/bin/env python3
"""Model-agnostic MECE skill evaluation harness.

The harness validates eval definitions, runs cases through a caller-supplied
adapter, and summarizes with-skill versus without-skill results. The adapter
is responsible for invoking the target ChatGPT/Codex or Claude environment
and for grading semantic assertions.
"""

from __future__ import annotations

import argparse
import json
import shlex
import statistics
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]


def load_cases(suite: str) -> list[dict[str, Any]]:
    cases: list[dict[str, Any]] = []
    if suite in {"trigger", "all"}:
        for case in json.loads((ROOT / "evals" / "trigger_queries.json").read_text(encoding="utf-8")):
            cases.append({"suite": "trigger", **case})
    if suite in {"output", "all"}:
        data = json.loads((ROOT / "evals" / "evals.json").read_text(encoding="utf-8"))
        for case in data["evals"]:
            cases.append({"suite": "output", **case})
    return cases


def validate_definitions() -> dict[str, Any]:
    triggers = load_cases("trigger")
    outputs = load_cases("output")
    errors: list[str] = []

    ids: set[tuple[str, str]] = set()
    for case in [*triggers, *outputs]:
        key = (case["suite"], str(case.get("id", "")))
        if not key[1]:
            errors.append(f"{case['suite']} case lacks id")
        if key in ids:
            errors.append(f"duplicate case id: {key}")
        ids.add(key)

    for case in triggers:
        if not isinstance(case.get("should_trigger"), bool):
            errors.append(f"trigger case {case.get('id')} lacks Boolean should_trigger")
        if not isinstance(case.get("query"), str) or not case["query"].strip():
            errors.append(f"trigger case {case.get('id')} lacks query")

    for case in outputs:
        if not isinstance(case.get("prompt"), str) or not case["prompt"].strip():
            errors.append(f"output case {case.get('id')} lacks prompt")
        assertions = case.get("assertions")
        if not isinstance(assertions, list) or not assertions:
            errors.append(f"output case {case.get('id')} lacks assertions")
        for rel in case.get("files", []):
            if not (ROOT / rel).exists():
                errors.append(f"output case {case.get('id')} references missing file {rel}")

    positives = sum(1 for c in triggers if c["should_trigger"])
    negatives = len(triggers) - positives
    return {
        "validation_pass": not errors,
        "trigger_cases": len(triggers),
        "positive_trigger_cases": positives,
        "negative_trigger_cases": negatives,
        "output_cases": len(outputs),
        "errors": errors,
    }


def invoke_adapter(command: str, payload: dict[str, Any], timeout: float) -> dict[str, Any]:
    started = time.perf_counter()
    proc = subprocess.run(
        shlex.split(command),
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    elapsed_ms = round((time.perf_counter() - started) * 1000, 2)
    if proc.returncode != 0:
        raise RuntimeError(f"adapter exit {proc.returncode}: {proc.stderr.strip()}")
    try:
        result = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"adapter returned invalid JSON: {exc}; stdout={proc.stdout[:500]!r}") from exc
    if not isinstance(result, dict):
        raise RuntimeError("adapter result must be a JSON object")
    result.setdefault("duration_ms", elapsed_ms)
    return result


def materialize_case(case: dict[str, Any]) -> dict[str, Any]:
    payload = dict(case)
    payload["skill_path"] = str(ROOT)
    if case["suite"] == "output":
        payload["resolved_files"] = [str((ROOT / rel).resolve()) for rel in case.get("files", [])]
    return payload


def run_cases(command: str, suite: str, condition: str, output: Path, timeout: float) -> int:
    cases = load_cases(suite)
    output.parent.mkdir(parents=True, exist_ok=True)
    failures = 0
    with output.open("w", encoding="utf-8") as fh:
        for case in cases:
            payload = {
                "condition": condition,
                "case": materialize_case(case),
                "adapter_contract_version": "1.0",
            }
            record: dict[str, Any] = {
                "suite": case["suite"],
                "case_id": case["id"],
                "condition": condition,
            }
            try:
                result = invoke_adapter(command, payload, timeout)
                record.update(result)
                record["adapter_error"] = None
            except Exception as exc:  # noqa: BLE001
                record["adapter_error"] = str(exc)
                failures += 1
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(json.dumps({"cases": len(cases), "adapter_failures": failures, "results": str(output)}, indent=2))
    return 0 if failures == 0 else 1


def read_jsonl(paths: Iterable[Path]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in paths:
        with path.open(encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, start=1):
                if not line.strip():
                    continue
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"{path}:{lineno}: {exc}") from exc
                if not isinstance(row, dict):
                    raise ValueError(f"{path}:{lineno}: record is not an object")
                rows.append(row)
    return rows


def safe_mean(values: list[float]) -> float | None:
    return round(statistics.mean(values), 4) if values else None


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    trigger_truth = {c["id"]: c["should_trigger"] for c in load_cases("trigger")}
    output_counts = {c["id"]: len(c["assertions"]) for c in load_cases("output")}
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[str(row.get("condition", "unknown"))].append(row)

    by_condition: dict[str, Any] = {}
    for condition, items in sorted(grouped.items()):
        tp = tn = fp = fn = 0
        output_passes = 0
        output_total = 0
        invalid_output_records = 0
        assertion_rates: list[float] = []
        grader_scores: list[float] = []
        durations: list[float] = []
        adapter_errors = 0

        for row in items:
            if row.get("adapter_error"):
                adapter_errors += 1
                continue
            if isinstance(row.get("duration_ms"), (int, float)):
                durations.append(float(row["duration_ms"]))
            if row.get("suite") == "trigger":
                expected = trigger_truth.get(str(row.get("case_id")))
                actual = row.get("activated")
                if expected is None or not isinstance(actual, bool):
                    continue
                if expected and actual:
                    tp += 1
                elif not expected and not actual:
                    tn += 1
                elif not expected and actual:
                    fp += 1
                else:
                    fn += 1
            elif row.get("suite") == "output":
                results = row.get("assertion_results")
                expected_count = output_counts.get(str(row.get("case_id")))
                if (isinstance(results, list) and expected_count is not None
                        and len(results) == expected_count
                        and all(isinstance(v, bool) for v in results)):
                    output_total += 1
                    passed = all(results)
                    output_passes += int(passed)
                    assertion_rates.append(sum(results) / len(results))
                else:
                    invalid_output_records += 1
                    continue
                if isinstance(row.get("grader_score"), (int, float)):
                    grader_scores.append(float(row["grader_score"]))

        trigger_total = tp + tn + fp + fn
        precision = tp / (tp + fp) if tp + fp else None
        recall = tp / (tp + fn) if tp + fn else None
        accuracy = (tp + tn) / trigger_total if trigger_total else None
        by_condition[condition] = {
            "records": len(items),
            "adapter_errors": adapter_errors,
            "trigger": {
                "tp": tp,
                "tn": tn,
                "fp": fp,
                "fn": fn,
                "precision": round(precision, 4) if precision is not None else None,
                "recall": round(recall, 4) if recall is not None else None,
                "accuracy": round(accuracy, 4) if accuracy is not None else None,
            },
            "output": {
                "cases_graded": output_total,
                "invalid_records": invalid_output_records,
                "full_assertion_passes": output_passes,
                "pass_rate": round(output_passes / output_total, 4) if output_total else None,
                "mean_assertion_rate": safe_mean(assertion_rates),
                "mean_grader_score": safe_mean(grader_scores),
            },
            "mean_duration_ms": safe_mean(durations),
        }

    delta: dict[str, Any] | None = None
    if "with_skill" in by_condition and "without_skill" in by_condition:
        with_skill = by_condition["with_skill"]
        without = by_condition["without_skill"]

        def diff(path: tuple[str, str]) -> float | None:
            a = with_skill[path[0]][path[1]]
            b = without[path[0]][path[1]]
            return round(a - b, 4) if isinstance(a, (int, float)) and isinstance(b, (int, float)) else None

        delta = {
            "trigger_accuracy": diff(("trigger", "accuracy")),
            "trigger_precision": diff(("trigger", "precision")),
            "trigger_recall": diff(("trigger", "recall")),
            "output_pass_rate": diff(("output", "pass_rate")),
            "mean_assertion_rate": diff(("output", "mean_assertion_rate")),
            "mean_grader_score": diff(("output", "mean_grader_score")),
        }

    return {
        "conditions": by_condition,
        "with_skill_minus_without_skill": delta,
        "limitations": [
            "Semantic assertion grading is supplied by the adapter and should be blinded where possible.",
            "Run each case in a fresh target-client session for credible activation and output measurements.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("validate", help="Validate eval definitions and referenced files")

    run = sub.add_parser("run", help="Run eval cases through a caller-supplied adapter")
    run.add_argument("--adapter", required=True, help="Executable command that reads one JSON payload from stdin and writes one JSON result to stdout")
    run.add_argument("--suite", choices=["trigger", "output", "all"], default="all")
    run.add_argument("--condition", choices=["with_skill", "without_skill"], required=True)
    run.add_argument("--results", type=Path, required=True)
    run.add_argument("--timeout", type=float, default=180.0)

    summary = sub.add_parser("summarize", help="Summarize one or more JSONL result files")
    summary.add_argument("results", type=Path, nargs="+")
    summary.add_argument("--output", type=Path)

    args = parser.parse_args()
    if args.command == "validate":
        report = validate_definitions()
        print(json.dumps(report, indent=2))
        return 0 if report["validation_pass"] else 1
    if args.command == "run":
        return run_cases(args.adapter, args.suite, args.condition, args.results, args.timeout)
    if args.command == "summarize":
        report = summarize(read_jsonl(args.results))
        rendered = json.dumps(report, indent=2)
        print(rendered)
        if args.output:
            args.output.write_text(rendered + "\n", encoding="utf-8")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
