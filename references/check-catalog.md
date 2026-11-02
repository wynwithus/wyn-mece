# Applicable Check Catalog

Use this catalog for routine validation. Mark each check `TRUE`, `FALSE`, `NOT_APPLICABLE`, or `NOT_ESTABLISHED`. Score only applicable checks. A critical-gate failure overrides the weighted score.

## Status rules

- `TRUE`: satisfied with cited or observable evidence.
- `FALSE`: contradicted or materially deficient.
- `NOT_APPLICABLE`: the selected archetype or decision does not require the check.
- `NOT_ESTABLISHED`: relevant, but available evidence is insufficient.

`NOT_ESTABLISHED` is not a pass. Resolve it, disclose it as a non-blocking assumption, or fail the relevant gate.

## Scope and interpretation checks

| ID | Check | Weight | TRUE when |
|---|---|---:|---|
| C1 | governing_parent_defined | 6 | The governing question, claim, outcome, state, or acceptance condition is explicit. |
| C2 | decision_and_audience_defined | 5 | The decision or action and intended consumer are explicit or safely assumed. |
| C3 | scope_and_exclusions_defined | 5 | In-scope and out-of-scope boundaries are explicit enough to test coverage. |
| C4 | atomic_unit_defined | 5 | One leaf, row, record, criterion, state, or factor has a clear meaning. |
| C5 | archetype_correct | 8 | The selected archetype matches the logic the artifact must represent. |
| C6 | basis_defined | 5 | The organizing logic for each sibling set or axis is stated or unambiguous. |
| C7 | provenance_preserved | 6 | Material content is tagged or traceable as source, derivation, assumption, or open question. |
| C8 | ambiguity_controlled | 5 | Material uncertainty is resolved through high-information questions or reversible assumptions. |

## Structural checks

| ID | Check | Weight | TRUE when |
|---|---|---:|---|
| S1 | elements_defined | 5 | Categories, branches, stages, predicates, criteria, axes, or factors have explicit rules or meanings. |
| S2 | vertical_logic | 7 | Every child answers, supports, causes, executes, or completes its parent. |
| S3 | same_basis_and_level | 7 | Siblings use one basis and one abstraction level. |
| S4 | applicable_overlap_test | 8 | The archetype-specific exclusivity or duplication test passes, including boundary and compound cases. |
| S5 | coverage_established | 8 | Coverage uses the strongest available proof method and the CE status is justified. |
| S6 | edge_cases_resolved | 6 | Null, unknown, mixed, transitional, waived, failed, and exceptional cases are assigned or disclosed. |
| S7 | residual_bounded | 4 | Any residual has an inclusion rule, review trigger, accountable owner where needed, and closure path. |
| S8 | order_and_sequence_valid | 4 | The logical order, state sequence, or causal direction is explicit and internally consistent. |
| S9 | interactions_preserved | 5 | Legitimate cross-branch interactions, parallel work, shared contributors, or feedback loops are explicit. |

## Operational checks

Apply only where the decision requires execution, acceptance, ownership, or handoff.

| ID | Check | Weight | TRUE when |
|---|---|---:|---|
| O1 | observable_and_testable | 7 | A non-author can verify each applicable criterion, predicate, state, or output. |
| O2 | evidence_producible | 5 | Named proof is identifiable and realistically obtainable. |
| O3 | thresholds_or_decision_rules_defined | 6 | “Good enough,” routing, or acceptance is explicit through numeric, enumerated, or evidence-based rules. |
| O4 | accountability_valid | 6 | Exactly one accountable owner exists where accountability is required; other roles may be plural. |
| O5 | transitions_and_dependencies_defined | 6 | Workflow entry, exit, prerequisites, joins, and handoffs are explicit where applicable. |
| O6 | exceptions_and_failure_actions_defined | 6 | Failure, timeout, retry, rollback, waiver, pause, cancellation, and escalation paths are covered as applicable. |
| O7 | decision_useful | 6 | A branch, classification, or pass/fail result changes an action, decision, priority, owner, or acceptance state. |
| O8 | artifact_handoff_integrity | 4 | Rendering can preserve hierarchy, scope, basis, evidence, assumptions, and validation state. |
| O9 | proportionality | 4 | The method and visible audit trail are no heavier than the decision requires. |

## Archetype applicability guide

This table supplies defaults. Override them when the user’s decision materially changes the need.

| Archetype | Required structural checks | Common operational checks | Common `NOT_APPLICABLE` checks |
|---|---|---|---|
| Partition / taxonomy / segmentation | S1–S8 | O1–O3, O7; O4 if governed operationally | O5–O6 unless it controls a lifecycle |
| Issue tree | S1–S6, S8–S9 | O2, O3, O7; O4 for a test plan | O5–O6 unless converted into execution |
| Workflow / lifecycle / execution plan | S1–S9 | O1–O7 | O8 unless handed off |
| Definition of Done / gate model | S1–S8 | O1–O4, O6–O7 | O5 unless criteria have state dependencies |
| Decision tree | S1–S8 | O1–O3, O6–O7 | O4–O5 unless execution ownership is included |
| Responsibility / ownership model | S1–S7 | O4, O6–O7 | O1–O3 unless acceptance criteria are included; O5 unless workflowed |
| Matrix / portfolio | S1–S8 | O1–O3, O7 | O4–O6 unless used for governance |
| Causal / system model | S1–S6, S8–S9 | O2–O3, O7 | O4–O6 unless converted into interventions |
| Narrative / deck / document | S1–S6, S8–S9 | O2, O7–O9 | O1, O3–O6 unless the content governs action |

## Readiness calculation

```text
applicable_weight = sum(weights for TRUE, FALSE, and NOT_ESTABLISHED checks)
passed_weight = sum(weights for TRUE checks)
READINESS_SCORE = 100 * passed_weight / applicable_weight
```

Do not count `NOT_APPLICABLE` in the denominator. Keep `NOT_ESTABLISHED` in the denominator so missing evidence cannot inflate readiness.

## Failure record

For every material `FALSE` or `NOT_ESTABLISHED` result, capture:

```yaml
failed_check: S4
status: FALSE
evidence: "Boundary item 100k maps to both Mid-Market and Enterprise."
root_causes:
  - overlapping_interval_endpoints
  - undefined_as_of_rule
why_it_matters: "The same account can be double-counted."
minimum_fix_required: "Use half-open intervals and define the measurement date."
revised_wording_or_rule: "Mid-Market: 100k <= ARR < 500k as of month-end."
```

Root causes and failed checks are many-to-many. Preserve that relationship instead of forcing a single label.
