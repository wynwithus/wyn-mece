#!/usr/bin/env python3
"""Validate a finite partition or a set of numeric interval bands.

Input JSON:
{
  "universe": ["item-a", "item-b"],
  "categories": {
    "category-1": ["item-a"],
    "category-2": ["item-b"]
  }
}

Partition mode reports gaps, overlaps, assignments outside the universe,
duplicate entries within a category, and whether strict MECE passes.

Interval mode is selected by a top-level ``intervals`` key. It validates
explicit endpoint inclusivity, pairwise disjointness, full domain coverage,
missing-data routing, and exact-one routing for any supplied numeric values.
``null`` endpoints are unbounded. Exit codes are 0 for a strict pass, 1 for
validation failures, and 2 for invalid input.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


NEG_INF = float("-inf")
POS_INF = float("inf")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that every item in a finite universe belongs to exactly one "
            "category, or that numeric interval bands are disjoint and cover a domain."
        )
    )
    parser.add_argument("input", type=Path, help="Path to the input JSON file.")
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path for the JSON report. Prints to stdout when omitted.",
    )
    parser.add_argument(
        "--allow-duplicates-within-category",
        action="store_true",
        help="Do not fail strict MECE solely because a category repeats an item.",
    )
    return parser.parse_args()


def load_payload(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"Cannot read input file '{path}': {exc}") from exc

    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Invalid JSON in '{path}' at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc

    if not isinstance(payload, dict):
        raise ValueError("Input root must be a JSON object.")
    return payload


def validate_schema(payload: dict[str, Any]) -> tuple[list[str], dict[str, list[str]]]:
    universe = payload.get("universe")
    categories = payload.get("categories")

    if not isinstance(universe, list):
        raise ValueError("'universe' must be a JSON array.")
    if not isinstance(categories, dict):
        raise ValueError("'categories' must be a JSON object mapping names to arrays.")

    normalized_universe: list[str] = []
    for index, item in enumerate(universe):
        if not isinstance(item, str) or not item.strip():
            raise ValueError(f"universe[{index}] must be a non-empty string.")
        normalized_universe.append(item)

    normalized_categories: dict[str, list[str]] = {}
    for name, items in categories.items():
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Every category name must be a non-empty string.")
        if not isinstance(items, list):
            raise ValueError(f"Category '{name}' must map to a JSON array.")
        normalized_items: list[str] = []
        for index, item in enumerate(items):
            if not isinstance(item, str) or not item.strip():
                raise ValueError(
                    f"categories['{name}'][{index}] must be a non-empty string."
                )
            normalized_items.append(item)
        normalized_categories[name] = normalized_items

    return normalized_universe, normalized_categories


def validate_partition(
    universe: list[str],
    categories: dict[str, list[str]],
    *,
    allow_duplicates_within_category: bool,
) -> dict[str, Any]:
    universe_counts = Counter(universe)
    duplicate_universe_items = sorted(
        item for item, count in universe_counts.items() if count > 1
    )
    universe_set = set(universe)

    assignments: dict[str, list[str]] = defaultdict(list)
    duplicate_entries: dict[str, list[str]] = {}
    assigned_outside_universe: dict[str, list[str]] = {}

    for category, raw_items in categories.items():
        counts = Counter(raw_items)
        duplicates = sorted(item for item, count in counts.items() if count > 1)
        if duplicates:
            duplicate_entries[category] = duplicates

        outside = sorted(item for item in counts if item not in universe_set)
        if outside:
            assigned_outside_universe[category] = outside

        for item in counts:
            if item in universe_set:
                assignments[item].append(category)

    gaps = sorted(item for item in universe_set if len(assignments[item]) == 0)
    overlaps = {
        item: sorted(assignments[item])
        for item in sorted(universe_set)
        if len(assignments[item]) > 1
    }
    exact_one_items = sorted(
        item for item in universe_set if len(assignments[item]) == 1
    )

    duplicate_failure = bool(duplicate_entries) and not allow_duplicates_within_category
    strict_mece_pass = not any(
        [
            duplicate_universe_items,
            gaps,
            overlaps,
            assigned_outside_universe,
            duplicate_failure,
        ]
    )

    return {
        "strict_mece_pass": strict_mece_pass,
        "universe_size": len(universe_set),
        "category_count": len(categories),
        "exact_one_count": len(exact_one_items),
        "exact_one_items": exact_one_items,
        "gaps": gaps,
        "overlaps": overlaps,
        "assigned_outside_universe": assigned_outside_universe,
        "duplicate_entries_within_category": duplicate_entries,
        "duplicate_items_in_universe": duplicate_universe_items,
        "membership": {
            item: sorted(assignments[item]) for item in sorted(universe_set)
        },
        "notes": [
            "This validator proves exact-one membership only for the supplied finite universe and assignments.",
            "It does not prove that the supplied universe is complete or that category definitions use a sound basis of division.",
        ],
    }


class Band:
    """A one-dimensional interval with explicit endpoint inclusivity."""

    def __init__(self, name: str, lo: float, lo_inc: bool, hi: float, hi_inc: bool):
        self.name = name
        self.lo = lo
        self.lo_inc = lo_inc
        self.hi = hi
        self.hi_inc = hi_inc

    def contains(self, value: float) -> bool:
        above = value > self.lo or (value == self.lo and self.lo_inc)
        below = value < self.hi or (value == self.hi and self.hi_inc)
        return above and below

    def label(self) -> str:
        left = "[" if self.lo_inc else "("
        right = "]" if self.hi_inc else ")"
        lo = "-inf" if self.lo == NEG_INF else format_number(self.lo)
        hi = "+inf" if self.hi == POS_INF else format_number(self.hi)
        return f"{left}{lo}, {hi}{right}"


def format_number(value: float) -> str:
    if value == int(value):
        return str(int(value))
    return repr(value)


def parse_endpoint(
    band: dict[str, Any], key: str, band_name: str, infinite: float
) -> tuple[float, bool, list[str]]:
    """Return value, inclusivity, and validation problems for one endpoint."""
    problems: list[str] = []
    sentinel = object()
    raw = band.get(key, sentinel)
    inc_key = f"{key}_inclusive"
    if raw is sentinel:
        problems.append(f"Band '{band_name}' is missing '{key}' (use null for unbounded).")
        return infinite, False, problems
    if raw is None:
        if inc_key in band:
            problems.append(
                f"Band '{band_name}' sets '{inc_key}' on an unbounded endpoint; remove it."
            )
        return infinite, False, problems
    if not isinstance(raw, (int, float)) or isinstance(raw, bool):
        problems.append(f"Band '{band_name}' has a non-numeric '{key}'.")
        return infinite, False, problems
    if inc_key not in band or not isinstance(band[inc_key], bool):
        problems.append(
            f"Band '{band_name}' has a finite '{key}' without an explicit boolean "
            f"'{inc_key}'."
        )
        return float(raw), False, problems
    return float(raw), band[inc_key], problems


def bands_overlap(a: Band, b: Band) -> str | None:
    """Return a label for the overlapping region, or None when disjoint."""
    if a.lo > b.lo or (a.lo == b.lo and not a.lo_inc and b.lo_inc):
        a, b = b, a
    lo, lo_inc = b.lo, b.lo_inc
    if a.lo == b.lo:
        lo_inc = a.lo_inc and b.lo_inc
    hi, hi_inc = (a.hi, a.hi_inc) if a.hi < b.hi else (b.hi, b.hi_inc)
    if a.hi == b.hi:
        hi, hi_inc = a.hi, a.hi_inc and b.hi_inc
    if lo < hi or (lo == hi and lo_inc and hi_inc):
        return Band("overlap", lo, lo_inc, hi, hi_inc).label()
    return None


def coverage_gaps(domain: Band, bands: list[Band]) -> list[str]:
    """Walk the domain from left to right and report uncovered intervals."""
    gaps: list[str] = []
    ordered = sorted(bands, key=lambda band: (band.lo, not band.lo_inc))
    needed_value, needed_closed = domain.lo, domain.lo_inc
    done = False

    for band in ordered:
        if done:
            break
        starts_in_time = (
            band.lo < needed_value
            or (band.lo == needed_value and (band.lo_inc or not needed_closed))
        )
        ends_usefully = band.hi > needed_value or (
            band.hi == needed_value and band.hi_inc and needed_closed
        )
        if not ends_usefully:
            continue
        if not starts_in_time:
            gaps.append(
                Band(
                    "gap", needed_value, needed_closed, band.lo, not band.lo_inc
                ).label()
            )
        if band.hi == POS_INF:
            done = True
            continue
        needed_value, needed_closed = band.hi, not band.hi_inc

    if not done:
        past_domain_end = needed_value > domain.hi or (
            needed_value == domain.hi and not (needed_closed and domain.hi_inc)
        )
        if not past_domain_end:
            gaps.append(
                Band(
                    "gap", needed_value, needed_closed, domain.hi, domain.hi_inc
                ).label()
            )
    return gaps


def validate_intervals(spec: dict[str, Any]) -> dict[str, Any]:
    """Validate that numeric bands form a strict partition of a domain."""
    if not isinstance(spec, dict):
        raise ValueError("'intervals' must be a JSON object.")

    raw_domain = spec.get("domain")
    if not isinstance(raw_domain, dict) or not {"min", "max"} <= set(raw_domain):
        raise ValueError(
            "'intervals.domain' must contain 'min' and 'max' numbers or null."
        )
    for key in ("min", "max"):
        value = raw_domain[key]
        if value is not None and (
            not isinstance(value, (int, float)) or isinstance(value, bool)
        ):
            raise ValueError(f"'intervals.domain.{key}' must be a number or null.")
    domain = Band(
        "domain",
        NEG_INF if raw_domain["min"] is None else float(raw_domain["min"]),
        raw_domain["min"] is not None,
        POS_INF if raw_domain["max"] is None else float(raw_domain["max"]),
        raw_domain["max"] is not None,
    )
    if domain.lo > domain.hi:
        raise ValueError("'intervals.domain' has min greater than max.")

    raw_bands = spec.get("bands")
    if not isinstance(raw_bands, list) or not raw_bands:
        raise ValueError("'intervals.bands' must be a non-empty JSON array.")

    malformed: list[str] = []
    bands: list[Band] = []
    seen_names: Counter[str] = Counter()
    for index, raw_band in enumerate(raw_bands):
        if not isinstance(raw_band, dict):
            malformed.append(f"bands[{index}] must be a JSON object.")
            continue
        name = raw_band.get("name")
        if not isinstance(name, str) or not name.strip():
            malformed.append(f"bands[{index}] needs a non-empty string 'name'.")
            name = f"bands[{index}]"
        seen_names[name] += 1
        lo, lo_inc, lo_problems = parse_endpoint(raw_band, "min", name, NEG_INF)
        hi, hi_inc, hi_problems = parse_endpoint(raw_band, "max", name, POS_INF)
        malformed.extend(lo_problems + hi_problems)
        if lo_problems or hi_problems:
            continue
        candidate = Band(name, lo, lo_inc, hi, hi_inc)
        if lo > hi or (lo == hi and not (lo_inc and hi_inc)):
            malformed.append(f"Band '{name}' is empty: {candidate.label()}.")
            continue
        bands.append(candidate)
    malformed.extend(
        f"Band name '{name}' is used {count} times; names must be unique."
        for name, count in sorted(seen_names.items())
        if count > 1
    )

    overlaps: list[dict[str, str]] = []
    for index, left in enumerate(bands):
        for right in bands[index + 1 :]:
            region = bands_overlap(left, right)
            if region is not None:
                overlaps.append(
                    {"bands": f"{left.name} x {right.name}", "region": region}
                )

    outside_domain = [
        {"band": band.name, "extent": band.label()}
        for band in bands
        if band.lo < domain.lo
        or band.hi > domain.hi
        or (band.lo == domain.lo and band.lo_inc and not domain.lo_inc)
        or (band.hi == domain.hi and band.hi_inc and not domain.hi_inc)
    ]
    gaps = coverage_gaps(domain, bands) if bands else [domain.label()]

    raw_values = spec.get("values", {})
    if not isinstance(raw_values, dict):
        raise ValueError(
            "'intervals.values' must map item names to numbers or null."
        )
    missing_category = spec.get("missing_data_category")
    if missing_category is not None and (
        not isinstance(missing_category, str) or not missing_category.strip()
    ):
        raise ValueError(
            "'intervals.missing_data_category' must be a non-empty string when present."
        )

    assignments: dict[str, list[str]] = {}
    null_values: list[str] = []
    values_outside_domain: list[str] = []
    for item in sorted(raw_values):
        value = raw_values[item]
        if value is None:
            null_values.append(item)
            assignments[item] = [missing_category] if missing_category else []
            continue
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise ValueError(f"'intervals.values[{item!r}]' must be a number or null.")
        numeric_value = float(value)
        if not domain.contains(numeric_value):
            values_outside_domain.append(item)
        assignments[item] = sorted(
            band.name for band in bands if band.contains(numeric_value)
        )

    missing_data_unrouted = bool(null_values) and not missing_category
    value_routing_failures = sorted(
        item
        for item, homes in assignments.items()
        if item not in null_values and len(homes) != 1
    )
    strict_interval_mece_pass = not any(
        [
            malformed,
            overlaps,
            gaps,
            outside_domain,
            missing_data_unrouted,
            value_routing_failures,
            values_outside_domain,
        ]
    )

    return {
        "mode": "intervals",
        "strict_interval_mece_pass": strict_interval_mece_pass,
        "domain": domain.label(),
        "band_count": len(bands),
        "bands": {band.name: band.label() for band in bands},
        "malformed": malformed,
        "overlaps": overlaps,
        "gaps": gaps,
        "bands_outside_domain": outside_domain,
        "value_assignments": assignments,
        "value_routing_failures": value_routing_failures,
        "values_outside_domain": values_outside_domain,
        "null_values": null_values,
        "missing_data_category": missing_category,
        "missing_data_unrouted": missing_data_unrouted,
        "notes": [
            "This validator proves band geometry and supplied value routing only for the supplied specification.",
            "It does not prove that the domain, unit, as-of rule, or banding basis is correct or decision-useful.",
            "Null values require a declared missing_data_category outside the numeric bands.",
        ],
    }
def emit(report: dict[str, Any], output: Path | None) -> None:
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if output is None:
        sys.stdout.write(rendered)
        return

    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"Cannot write output file '{output}': {exc}") from exc


def main() -> int:
    args = parse_args()
    try:
        payload = load_payload(args.input)
        if "intervals" in payload:
            report = validate_intervals(payload["intervals"])
            passed = report["strict_interval_mece_pass"]
        else:
            universe, categories = validate_schema(payload)
            report = validate_partition(
                universe,
                categories,
                allow_duplicates_within_category=args.allow_duplicates_within_category,
            )
            passed = report["strict_mece_pass"]
        emit(report, args.output)
    except ValueError as exc:
        sys.stderr.write(f"ERROR: {exc}\n")
        return 2

    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
