---
name: wyn-mece
description: Evaluate, repair, or create MECE frameworks. Use for "make this MECE", gaps, overlap, double-counting, mixed logic, unclear ownership, issue trees, taxonomies, workflows, or testable completion criteria. Skip ordinary copyediting and formatting.
metadata:
  author: WynWithUs
  version: "3.2.1"
---
# WYN MECE — Framework and Materials Engineering

## Objective

Turn a request or source artifact into a decision-ready structure that is logically sound, source-grounded, operational where required, and MECE at every applicable sibling set.

MECE is a validation method, not a formatting style. The validity rule depends on the structural archetype.

## Literal definitions

Apply both tests to one sibling set against its parent and under the selected archetype:

- **Mutually exclusive (ME):** siblings do not double-count the applicable unit, claim, responsibility, state, path, or contribution under that archetype's validity rule.
- **Collectively exhaustive (CE):** siblings cover the defined parent and in-scope universe to the stated proof strength.
- ME and CE are independent. A sibling set may pass one and fail the other.
- For bounded partitions and exclusive decision predicates, ME and CE combine into the **exact-one test:** every in-scope item maps to exactly one valid category or branch.

Do not turn these definitions into one universal membership test. Definitions of Done are normally conjunctive, causal models may contain interactions and feedback, workflows may contain explicit parallel work, and ownership models may have multiple contributors while retaining one accountable owner.

## Core standard

1. **Select the archetype before applying a test.** A partition, issue tree, workflow, Definition of Done, decision tree, ownership model, matrix, causal model, and narrative do not share one membership rule.
2. **Apply MECE locally.** Test each sibling set against its parent. Use exact-one classification only for bounded partitions and decision predicates that require it.
3. **Preserve provenance.** Mark material content as `SOURCE`, `DERIVED`, `ASSUMPTION`, or `OPEN`.
4. **State proof strength honestly.** Label collective exhaustiveness `PROVEN`, `SUPPORTED`, `ASSUMED`, or `NOT_ESTABLISHED`.
5. **Use one basis per sibling set.** Put a second basis on another level or axis.
6. **Make execution observable.** Add owners, evidence, thresholds, transitions, exceptions, and failure actions only where the archetype and decision require them.
7. **Lead with the answer.** Put the governing thought, verdict, or finished artifact before the audit trail.
8. **Scale the ceremony to the task.** Do not expose progress checklists, complete ledgers, or full rubrics unless they contain material findings, the user requests an audit trail, the decision is high-stakes, or another system needs the handoff.
9. **Validate every framework, including your own.** Never deliver an unevaluated build or repair.

## Routing

Choose exactly one primary mode:

| Primary mode | Use when | Required result |
|---|---|---|
| `EVALUATE` | An artifact exists and the user wants a judgment | Verdict, material defects, evidence, minimum fixes |
| `REPAIR` | An artifact exists and the user wants it corrected | Diagnosis, repaired artifact, change log, validation |
| `CREATE` | No adequate artifact exists and the user wants one built | Scope, completed framework, validation, assumptions |

Add zero or more modifiers:

- `RECONSTRUCT`: interpret a screenshot or diagram before evaluation or repair.
- `OPERATIONALIZE`: add evidence, thresholds, owners, state transitions, exceptions, or failure actions.
- `PREPARE_ARTIFACT_HANDOFF`: preserve the approved content architecture for a document, deck, spreadsheet, or diagram renderer.

If intent is ambiguous between `EVALUATE` and `REPAIR`, evaluate first and include the smallest repair required. Do not force a user-visible routing discussion when the intended result is evident.

## Workflow

### 1. Deconstruct the input

For text, notes, lists, or drafts:

1. Separate requested deliverable requirements from source content.
2. Split compound statements into atomic items: one object, claim, action, condition, state, or criterion.
3. Assign source IDs such as `T1`, `T2`, and `T3`.
4. Preserve source labels verbatim when meaning is uncertain.
5. Surface contradictions across sources instead of silently choosing one.

For screenshots or diagrams:

1. Inspect the image natively before using OCR or guessing.
2. Transcribe visible labels, annotations, and legends verbatim; mark illegible text `[unreadable]`.
3. Build a visual evidence ledger with `ID`, literal text, container or shape, relative position, connector, direction, style cue, and confidence.
4. Identify visual grammar: hierarchy, flow, matrix, timeline, swimlane, overlap, dashboard, or mixed layout.
5. Distinguish visible evidence from inferred structural meaning.
6. Trace every reconstructed element to a visual source ID or label it `DERIVED` or `ASSUMPTION`.

Read [references/intake-and-screenshot.md](references/intake-and-screenshot.md) when the source is visual, sparse, contradictory, cropped, or low-confidence.

### 2. Establish the scope contract

Define or infer:

```text
decision = choice or action the output must support
audience = consumer, approver, or operator
deliverable = tree, taxonomy, workflow, DoD, matrix, deck outline, etc.
U = bounded universe, when one exists
x = atomic unit being classified, decomposed, sequenced, or tested
parent = governing question, claim, outcome, state, or gate
B = basis of division for the current sibling set
purpose = why the structure exists
scenario = operating context, time horizon, geography, and constraints
evidence = proof required for claims, assignment, or completion
depth = required decomposition level
exclusions = explicitly out-of-scope items
```

Use this clarification gate:

1. Ask only when a different answer could materially change the archetype, parent, scope, unit, basis, acceptance test, or recommendation.
2. Ask at most four questions in the initial batch.
3. Give a proposed default with each question so the user can confirm or replace it.
4. Prefer boundary, forced-choice, and evidence questions over broad requests for context.
5. Use one targeted follow-up only if the first answers reveal a new contradiction or materially different archetype.
6. Proceed with labeled, reversible assumptions when uncertainty is minor or the user directs you to continue.

High-information questions:

- **Decision:** “Should this diagnose causes, assign entities, govern execution, or define completion? Default: [best-supported option].”
- **Boundary:** “Is [edge case] in scope? Default: [include/exclude] because [source evidence].”
- **Unit:** “Should one leaf represent a cause, task, deliverable, owner, or record? Default: [unit].”
- **Evidence:** “What proof makes a branch or gate acceptable? Default: [observable test].”

### 3. Select the structural archetype

| Archetype | Atomic unit | Core validity rule |
|---|---|---|
| Partition / taxonomy / segmentation | entity or record | each in-scope item maps to exactly one category |
| Issue tree / problem decomposition | sub-question, driver, or hypothesis | siblings are distinct and together answer the parent |
| Workflow / lifecycle / execution plan | state, transition, work item, or deliverable | entry, order, exit, dependencies, exceptions, and terminal states are complete |
| Definition of Done / gate model | completion criterion | required criteria are atomic, distinct, observable, and conjunctively satisfied |
| Decision tree | case at a decision node | exactly one branch predicate is true at that node |
| Responsibility / ownership model | decision, task, or deliverable | exactly one accountable owner where accountability is required; contributors may be plural |
| Matrix / portfolio | cell intersection | each axis is independently MECE; unknowns and empty cells are handled explicitly |
| Causal / system model | factor, mechanism, interaction, or feedback loop | factors are distinct; interactions and feedback are represented rather than forced into exclusivity |
| Narrative / deck / document architecture | supporting idea | siblings are logically alike and collectively support the governing thought |

Read [references/archetypes.md](references/archetypes.md) before constructing a high-stakes, hybrid, or unfamiliar structure.

### 4. Construct or repair the architecture

For every parent, stage, gate, or axis:

1. Express the parent as a question, claim, outcome, state, or acceptance condition.
2. Choose one basis of division `B`.
3. Create the fewest siblings needed for decision usefulness; normally favor 3–5 at a communication level, without forcing the count.
4. Keep siblings at the same abstraction level and of the same logical kind.
5. Define inclusion, exclusion, predicate, entry/exit, or acceptance rules appropriate to the archetype.
6. Map source items to leaves or identify new material as `DERIVED`, `ASSUMPTION`, or `OPEN`.
7. Resolve null, unknown, mixed, transitional, failed, waived, and exceptional cases.
8. Bound any residual with an inclusion rule, accountable review owner, trigger, and closure path.
9. Order siblings by one governing relation: logical implication, chronological sequence, structural arrangement, comparative rank, or causal/dependency relation. State the specific rule used. Apply predecessor and blocker tests only to execution or dependency sequences.
10. Preserve legitimate interactions, parallel work, shared contributors, and feedback loops instead of creating artificial exclusivity.

Repair mixed basis before moving individual items. Convert vague verbs such as “optimize,” “align,” “ensure,” “support,” “review,” and “manage” into observable tests or remove them.

Read [references/construction-patterns.md](references/construction-patterns.md) when choosing a basis, repairing mixed logic, bounding a residual, or converting vague material into observable form.

### 5. Run applicable checks

Use four statuses:

```text
TRUE = requirement is satisfied with evidence
FALSE = requirement is contradicted or materially deficient
NOT_APPLICABLE = the archetype or decision does not require it
NOT_ESTABLISHED = evidence is insufficient to judge
```

Run the compact checks in [references/check-catalog.md](references/check-catalog.md). At minimum verify:

- scope, parent, unit, archetype, basis, and provenance;
- vertical logic and same-level horizontal logic;
- the archetype-specific overlap test;
- coverage, edge cases, and residual handling;
- observability, evidence, thresholds, ownership, transitions, and failure handling where applicable;
- decision usefulness and output proportionality.

For finite partitions and decision predicates, run the exact-one test:

```text
for each x in bounded U:
  n = count(valid categories or predicates containing x)
  n = 0  -> gap
  n = 1  -> pass
  n >= 2 -> overlap
```

A parent containing its child is decomposition, not overlap. A Definition of Done is normally a conjunction of required criteria, not a partition of the completed object. A causal system may contain cross-branch interactions.

When `U` and assignments are finite, use `scripts/validate_partition.py` to detect gaps, overlaps, duplicate assignments, and unknown items. For numeric bands, use its `intervals` input to test explicit endpoints, pairwise disjointness, domain coverage, missing-data routing, and supplied value assignments.

### 6. Grade, repair, and stop

Use evidence-led gates before numerical scores.

Critical gates:

```text
G1 correct structural archetype and governing parent
G2 material source meaning preserved or changes disclosed
G3 every top-level sibling supports or answers its parent
G4 no known material overlap, gap, exception, or interaction is concealed
G5 collective-exhaustiveness and confidence claims are not overstated
G6 operational criteria are testable where execution is requested
```

Compute:

```text
READINESS_SCORE = 100 * passed applicable weight / total applicable weight
CONFIDENCE = minimum(source_confidence, archetype_confidence, coverage_confidence)
```

`READINESS_SCORE` summarizes rubric compliance. It is not confidence.

Verdicts:

```text
PASS = all critical gates pass AND readiness >= 90 AND confidence >= 90
CONDITIONAL_PASS = all critical gates pass AND only disclosed, non-blocking assumptions remain
FAIL = any critical gate fails or a material structural defect remains
```

Apply verdicts in order: a failed critical gate or material defect means `FAIL`; otherwise use `PASS` only when all pass thresholds are met. Use `CONDITIONAL_PASS` only when the remaining limitations are disclosed and non-blocking. If evidence is insufficient to establish a gate, state that the gate is `NOT_ESTABLISHED` and withhold a pass verdict until it is resolved or justified as non-blocking.

For routine work, use one compact applicable-check pass. For high-stakes materials, read [references/output-rubric.md](references/output-rubric.md) and run the Minto and MECE-operational graders.

- Use isolated subagents or fresh contexts when available.
- Otherwise run two blinded rubric passes and label them `QUASI_INDEPENDENT`; do not claim true independence.
- Freeze both initial results before reconciliation.
- Treat scores as summaries of evidence, not targets to be raised.
- Repair the highest-impact supported failure first.
- Run at most three internal repair passes.
- Stop earlier when all gates pass, the required threshold is reached, or missing source evidence blocks further improvement.
- Never manufacture evidence, certainty, or a passing score.

### 7. Deliver answer-first

Read [references/output-contracts.md](references/output-contracts.md) and choose the smallest contract that supports the decision.
Read [references/examples.md](references/examples.md) only when a rendered pattern is unclear.

Default order:

1. governing thought, finished framework, or verdict;
2. key-line support or highest-impact defects;
3. repaired or created artifact;
4. material failures with minimum fixes;
5. assumptions and open questions;
6. validation summary.

For each material failure, report:

```text
failed_check:
status:
evidence:
root_causes: []
why_it_matters:
minimum_fix_required:
revised_wording_or_rule:
```

Root causes and failed checks are many-to-many. Do not force one failure type per check.

Output density:

- `EVALUATE`: show the verdict and material failed or not-established checks; provide the full applicable scorecard only when requested or high-stakes.
- `REPAIR` and `CREATE`: compress passes to one line and expand failures, assumptions, and edge cases.
- `RECONSTRUCT`: show literal source recovery and uncertain interpretations before presenting derived repairs.
- `PREPARE_ARTIFACT_HANDOFF`: include a machine-readable handoff that preserves hierarchy, evidence, assumptions, CE status, readiness, and confidence.

Do not lead with a generic definition, progress checklist, long rubric, or procedural narration.

## Failure handling

- **Unreadable screenshot:** identify load-bearing unreadable regions, request a higher-resolution crop when necessary, and continue only with legible content plus labeled uncertainty.
- **Contradictory sources:** preserve both claims, identify the conflict, and state which source or assumption governs each provisional branch.
- **Unbounded universe:** provide a bounded hypothesis structure and label CE `ASSUMED`, `SUPPORTED`, or `NOT_ESTABLISHED`.
- **Mixed structures:** separate them into levels, axes, or linked artifacts.
- **Missing evidence:** deliver the strongest supported version with the blocking evidence named; do not infer a pass.
- **Style-only request:** do not invoke this skill unless structural completeness, exclusivity, sequencing, or operability is part of the job.

## Single-line standard

A framework is MECE-ready when every applicable sibling set uses one governing logic, known overlap and gaps are resolved or disclosed, each operational path is testable where required, and the output supports the stated decision without overstating evidence or exhaustiveness.
