# High-Stakes Output Rubric

Use this rubric for executive materials, ambiguous multi-source work, operating systems, artifact handoffs, or whenever the user requests a formal audit. For routine jobs, use `check-catalog.md` without exposing a full dual scorecard.

Scores summarize evidence. They are not targets. A numerical total cannot override a critical-gate failure.

## Scoring anchors

For each applicable criterion, award a percentage of its weight:

- `100% of weight`: complete, explicit, source-grounded, and robust under edge cases.
- `90% of weight`: production-ready; only immaterial tuning remains.
- `75% of weight`: useful but one material weakness remains.
- `50% of weight`: partially present; substantial repair is required.
- `25% of weight`: mentioned without operational substance.
- `0% of weight`: absent, contradicted, or invalid.
- `NOT_APPLICABLE`: remove the weight from the denominator.
- `NOT_ESTABLISHED`: award zero until evidence is supplied or the uncertainty is accepted as non-blocking.

Normalize each grader to 100 over applicable weight. Record evidence for every deduction.

## Isolation protocol

1. Give both graders the same frozen source ledger, scope contract, draft artifact, archetype rules, and applicable-check decisions.
2. Use separate subagents or fresh contexts when available. This is `INDEPENDENT` grading.
3. Otherwise run two blinded passes in the same context, freezing each result before reconciliation. Label this `QUASI_INDEPENDENT`.
4. Do not expose one grader’s score, deductions, or repair suggestions to the other before both initial records are frozen.
5. Resolve disagreements caused by different scope or archetype assumptions before editing the artifact.
6. The lower evidence-supported result governs release when a critical gate or material deduction is disputed.

---

# Grader A — Minto Structure Readiness

| Criterion | Weight | Full-credit standard |
|---|---:|---|
| 1. Governing decision and scope | 12 | Governing question, audience, decision, scope, unit, and exclusions are explicit or transparently assumed. |
| 2. Governing thought / answer first | 12 | The output opens with a defensible answer, verdict, or completed artifact that summarizes the key line. |
| 3. Vertical logic | 14 | Every child directly answers or supports its parent; every parent accurately synthesizes its children. |
| 4. Horizontal logic and single basis | 14 | Siblings are logically alike, at one abstraction level, and use one basis of division. |
| 5. Archetype-appropriate ME/CE proof | 14 | Overlap, gaps, boundaries, interactions, exceptions, and residuals are tested using the selected archetype’s rule. |
| 6. Granularity and deconstruction | 10 | Items are atomic enough to test or act on; compound and duplicate ideas are split or consolidated. |
| 7. Logical ordering and sequencing | 8 | One governing relation is explicit and appropriate: logical implication, chronological sequence, structural arrangement, comparative rank, or causal/dependency relation. Predecessor and blocker tests apply only to execution or dependency sequences. |
| 8. Source fidelity and assumptions | 8 | Material content is traceable to source, derivation, assumption, or open question; meaning is preserved. |
| 9. Decision usefulness | 5 | The structure changes a decision, action, priority, ownership assignment, or acceptance state. |
| 10. Clarity and economy | 3 | Labels are informative and the visible method is proportional to the task. |

## Minto critical gates

```text
M1 governing parent or decision is defined
M2 no material source meaning is silently changed
M3 every top-level sibling directly supports the governing thought or parent
M4 no known material overlap, gap, exception, or interaction is concealed
M5 collective-exhaustiveness and confidence claims are not overstated
```

---

# Grader B — MECE Operational Readiness

| Criterion | Weight | Full-credit standard |
|---|---:|---|
| 1. Correct archetype and validity rule | 14 | The output uses the correct rule for partition, tree, workflow, DoD, decision, ownership, matrix, causal, or narrative logic. |
| 2. Intake and ambiguity control | 10 | Material ambiguity was resolved with no more than four high-information questions with proposed defaults, or explicit reversible assumptions. |
| 3. Applicable overlap validation | 12 | The archetype-specific overlap or duplication test covers boundary, compound, temporal, and shared-role cases as relevant. |
| 4. Coverage validation | 12 | Coverage uses the strongest available proof method and handles unknown, null, residual, exception, and interaction cases. |
| 5. Observability and testability | 12 | Applicable criteria, predicates, states, leaves, or outputs can be verified using defined evidence or tests. |
| 6. Ownership and decision rights | 8 | Accountability is singular where required; contributors, approvers, waivers, and escalations are explicit. |
| 7. Thresholds, transitions, and failure handling | 10 | Acceptance rules, state transitions, dependencies, exceptions, retries, or failure actions are explicit where applicable. |
| 8. Traceability and evidence | 8 | Source items map to output elements; evidence is identifiable and realistically obtainable. |
| 9. Artifact handoff integrity | 6 | Rendering can preserve hierarchy, scope, basis, evidence, assumptions, and validation state. |
| 10. Efficiency and proportionality | 8 | The method is no more complex than the decision requires; routine passes are compressed and material failures are expanded. |

## Operational critical gates

```text
O1 structural archetype is identified correctly
O2 material ambiguity is resolved or labeled
O3 the applicable overlap or duplication test passes
O4 meaningful gaps, exceptions, and interactions are closed or disclosed
O5 operational criteria are testable where execution is requested
O6 accountability is singular where the archetype requires it
O7 failure states and downstream handoff risks are not silently omitted
```

---

# Readiness, confidence, and verdict

Calculate separate readiness scores for the two graders over applicable weight:

```text
MINTO_READINESS = 100 * Minto points earned / applicable Minto weight
MECE_OPERATIONAL_READINESS = 100 * Operational points earned / applicable Operational weight
```

Calculate confidence independently:

```text
SOURCE_CONFIDENCE = confidence in source legibility, completeness, and reliability
ARCHETYPE_CONFIDENCE = confidence in the selected parent, unit, basis, and structural model
COVERAGE_CONFIDENCE = confidence in the coverage proof and edge-case testing
FINAL_CONFIDENCE = minimum(SOURCE_CONFIDENCE, ARCHETYPE_CONFIDENCE, COVERAGE_CONFIDENCE)
```

Pass logic:

```text
PASS =
  MINTO_READINESS >= 90
  AND MECE_OPERATIONAL_READINESS >= 90
  AND all applicable critical gates = PASS
  AND FINAL_CONFIDENCE >= 90

CONDITIONAL_PASS =
  all applicable critical gates = PASS
  AND only disclosed, non-blocking assumptions or open evidence requests remain

FAIL =
  any critical gate = FAIL
  OR a material structural or operational defect remains
```

Apply verdicts in order: a failed critical gate or material defect means `FAIL`; otherwise use `PASS` only when all pass thresholds are met. Use `CONDITIONAL_PASS` only when the remaining limitations are disclosed and non-blocking. If evidence is insufficient to establish a gate, state that the gate is `NOT_ESTABLISHED` and withhold a pass verdict until it is resolved or justified as non-blocking.

Do not call a weighted pass percentage “confidence.” Do not average readiness and confidence.

## Repair and stopping protocol

1. List deductions in descending material impact.
2. Repair the highest-impact supported failure first.
3. Re-run the selected archetype’s checks and verify the repair did not create a new defect.
4. Re-grade using the same frozen scope and applicability decisions unless new evidence justifies a documented change.
5. Run at most three internal repair passes.
6. Stop earlier when all gates pass and thresholds are met, or when missing evidence blocks improvement.
7. If blocked, deliver the strongest supported version with the blocking evidence, assumption, or scope choice named.

Never increase a score because the output is polished or because the loop is approaching its limit.
