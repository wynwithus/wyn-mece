"""Regression checks for publication-review defects and boundary behavior."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]


def load_module(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


package = load_module("package_validator", "scripts/validate_skill.py")
harness = load_module("eval_harness", "evals/run_evals.py")


class IntervalRegressionTests(unittest.TestCase):
    def run_validator(self, payload):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_text(payload, encoding="utf-8")
            return subprocess.run(
                [sys.executable, "-B", str(ROOT / "scripts/validate_partition.py"), str(path)],
                text=True, capture_output=True, check=False,
            )

    def test_large_integer_gap_is_not_rounded_away(self):
        result = self.run_validator(json.dumps({"intervals": {
            "domain": {"min": 9007199254740992, "max": 9007199254740994},
            "bands": [
                {"name": "a", "min": 9007199254740992, "max": 9007199254740992,
                 "min_inclusive": True, "max_inclusive": True},
                {"name": "b", "min": 9007199254740993, "max": 9007199254740994,
                 "min_inclusive": False, "max_inclusive": True},
            ],
            "values": {"gap_item": 9007199254740993},
        }}))
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(report["gaps"])
        self.assertEqual(report["value_assignments"]["gap_item"], [])

    def test_decimal_gap_is_not_rounded_away(self):
        result = self.run_validator('''{"intervals": {
          "domain": {"min": 0.1, "max": 0.2},
          "bands": [
            {"name": "a", "min": 0.1, "max": 0.100000000000000001,
             "min_inclusive": true, "max_inclusive": true},
            {"name": "b", "min": 0.100000000000000003, "max": 0.2,
             "min_inclusive": true, "max_inclusive": true}
          ],
          "values": {"gap_item": 0.100000000000000002}
        }}''')
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertTrue(report["gaps"])
        self.assertEqual(report["value_assignments"]["gap_item"], [])

    def test_missing_category_cannot_reuse_band_name(self):
        result = self.run_validator(json.dumps({"intervals": {
            "domain": {"min": 0, "max": 100},
            "bands": [{"name": "known", "min": 0, "max": 100,
                       "min_inclusive": True, "max_inclusive": True}],
            "missing_data_category": "known", "values": {"missing": None},
        }}))
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertTrue(json.loads(result.stdout)["malformed"])

    def test_nonfinite_json_numbers_are_input_errors(self):
        for value in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(value=value):
                result = self.run_validator('{"intervals": {"domain": {"min": 0, "max": ' + value + '}}}')
                self.assertEqual(result.returncode, 2)
                self.assertIn("Non-finite", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_half_open_boundary_routes_exactly_once(self):
        result = self.run_validator(json.dumps({"intervals": {
            "domain": {"min": 0, "max": None},
            "bands": [
                {"name": "small", "min": 0, "max": 100,
                 "min_inclusive": True, "max_inclusive": False},
                {"name": "large", "min": 100, "max": None, "min_inclusive": True},
            ],
            "missing_data_category": "unknown",
            "values": {"boundary": 100, "missing": None},
        }}))
        self.assertEqual(result.returncode, 0, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["value_assignments"]["boundary"], ["large"])
        self.assertEqual(report["value_assignments"]["missing"], ["unknown"])


class EvaluationRegressionTests(unittest.TestCase):
    def test_negative_fixture_cannot_pass_on_input_error(self):
        with patch.object(package.subprocess, "run", return_value=subprocess.CompletedProcess([], 2, "", "ERROR")):
            result = package.run_validator_fixture(ROOT, "partition-fail.json", False)
        self.assertFalse(result.passed)

    def test_negative_fixture_cannot_pass_without_expected_defects(self):
        output = json.dumps({"strict_mece_pass": False, "gaps": [], "overlaps": {}})
        with patch.object(package.subprocess, "run", return_value=subprocess.CompletedProcess([], 1, output, "")):
            result = package.run_validator_fixture(ROOT, "partition-fail.json", False)
        self.assertFalse(result.passed)

    def test_partial_assertion_list_cannot_be_a_full_pass(self):
        case = harness.load_cases("output")[0]
        report = harness.summarize([{
            "suite": "output", "condition": "with_skill", "case_id": case["id"],
            "assertion_results": [True], "adapter_error": None,
        }])
        output = report["conditions"]["with_skill"]["output"]
        self.assertEqual(output["invalid_records"], 1)
        self.assertEqual(output["cases_graded"], 0)
        self.assertEqual(output["full_assertion_passes"], 0)

    def test_complete_assertion_lists_are_graded(self):
        case = harness.load_cases("output")[0]
        report = harness.summarize([{
            "suite": "output", "condition": "with_skill", "case_id": case["id"],
            "assertion_results": [True] * len(case["assertions"]), "adapter_error": None,
        }])
        output = report["conditions"]["with_skill"]["output"]
        self.assertEqual(output["invalid_records"], 0)
        self.assertEqual(output["full_assertion_passes"], 1)


if __name__ == "__main__":
    unittest.main()
