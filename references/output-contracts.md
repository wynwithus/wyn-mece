# Output Contracts

Choose the smallest contract that fully supports the user’s decision. Put the verdict or artifact before the audit trail. Do not expose internal progress checklists.

## Proportionality rule

Use the **compact contract** by default. Add a full applicable-check table, coverage ledger, source map, dual graders, or machine-readable handoff only when:

- a material failure or uncertainty requires it;
- the user requests a formal audit;
- the output governs a high-stakes decision or operating process;
- a screenshot or mixed source requires traceability;
- another skill or system will render the artifact.

Compress routine passes to one line. Expand `FALSE` and `NOT_ESTABLISHED` results.

## 1. Compact universal contract

```markdown
# [Governing Answer, Verdict, or Finished Framework]
[One-sentence governing thought or decision-ready artifact.]

## Key Support or Material Defects
1. [Distinct support or defect]
2. [Distinct support or defect]
3. [Distinct support or defect]

## Framework / Repair
[Tree, table, workflow, taxonomy, gate model, matrix, or outline.]

## Validation
- Archetype: [type]
- Applicable checks: [passed]/[applicable]
- Critical gates: [PASS/FAIL]
- CE status: [PROVEN | SUPPORTED | ASSUMED | NOT_ESTABLISHED]
- Readiness: [0–100, when formally scored]
- Confidence: [0–100, with basis]
- Material assumptions or failures: [only those that affect use]
```

## 2. `EVALUATE` contract

```markdown
# Verdict
[PASS | CONDITIONAL_PASS | FAIL] — [one-sentence reason]

## Highest-Impact Findings
| Priority | Failed Check | Status | Evidence | Consequence | Minimum Fix |
|---:|---|---|---|---|---|

## Structural Diagnosis
- Archetype:
- Governing parent:
- Atomic unit:
- Basis:
- Scope and exclusions:
- CE status:

## Minimum Repair
[Smallest wording or structural changes that close the material failures.]

## Validation Summary
- Passed applicable checks: [x/y]
- Critical gates: [PASS/FAIL]
- Readiness: [when formally scored]
- Confidence: [separate from readiness]
```

Provide the full applicable-check scorecard only when requested or high-stakes.

## 3. `REPAIR` contract

```markdown
# Governing Diagnosis
[The root structural problem and its consequence.]

## Repaired Framework
[Answer-first repaired artifact.]

## Assignment or Operating Rules
| Element | Inclusion / Entry / Acceptance Rule | Exclusion / Exit Rule | Edge Cases |
|---|---|---|---|

## Material Change Log
| Source Element | Repaired Element | Reason | Provenance |
|---|---|---|---|

## Remaining Failures or Assumptions
[Expand only FALSE and NOT_ESTABLISHED items.]

## Validation
[Compressed pass count, gates, CE status, readiness if scored, and confidence.]
```

## 4. `CREATE` contract

```markdown
# Recommended Structure
[Completed decision-ready artifact.]

## Scope Contract
- Decision:
- Audience:
- Universe or parent:
- Atomic unit:
- Basis:
- Exclusions:
- Evidence standard:

## Rules and Edge Cases
[Only rules needed to use the framework correctly.]

## Validation
[Compressed applicable-check result, CE status, assumptions, readiness if scored, and confidence.]
```

## 5. Failure record

Use for each material `FALSE` or `NOT_ESTABLISHED` check:

```yaml
failed_check: S4
status: FALSE
evidence: ""
root_causes: []
why_it_matters: ""
minimum_fix_required: ""
revised_wording_or_rule: ""
```

Do not force one root cause per failed check or one failed check per root cause.

## 6. Issue tree contract

```markdown
# Governing Question
[Question]

## Working Answer or Hypothesis
[Answer, if supportable; otherwise state what evidence is required.]

## Issue Tree
1. [Top-level sub-question]
   1.1 [Leaf question]
   1.2 [Leaf question]
2. [Top-level sub-question]
   2.1 [Leaf question]
   2.2 [Leaf question]

## Leaf Test Plan
| Leaf | Evidence Needed | Method | Owner, if needed | Decision Rule |
|---|---|---|---|---|

## Interaction Terms
[Cross-branch effects, confounders, or feedback that must be modeled separately.]
```

## 7. Taxonomy or segmentation contract

```markdown
# Universe and As-of Rule
- Universe:
- Atomic item:
- As-of date or state:

## Categories
| Category | Inclusion Rule | Exclusion Rule | Boundary Rule |
|---|---|---|---|

## Exact-One Results
- Gaps:
- Overlaps:
- Unknown assignments:
- Residual share and closure rule:
- Proof scope: [the precise bounded universe for which PROVEN applies]
```

## 8. Workflow or execution-plan contract

```markdown
# Target Outcome
[Outcome]

## Workflow
| Stage | Entry | Action | Accountable Owner | Output | Exit | Exception / Failure Action |
|---|---|---|---|---|---|---|

## Transition Rules
| From | Predicate | To | Evidence | Timeout / Escalation |
|---|---|---|---|---|

## Parallel Work and Dependencies
[Explicit lanes, joins, prerequisites, retries, rollback, pause, cancellation, and terminal states.]
```

## 9. Definition of Done contract

```markdown
# Done Means
[Single acceptance statement.]

| Gate | Atomic Criterion | Evidence | Pass Threshold | Accountable Approver | Failure Action | Validity Window |
|---|---|---|---|---|---|---|

## Logic
All non-waived required criteria are conjunctively satisfied. The completed object is not forced into exactly one criterion.

## Waiver Rules
| Criterion | Who May Waive | Required Rationale | Expiry | Follow-up Owner |
|---|---|---|---|---|
```

## 10. Responsibility contract

```markdown
# Ownership Principle
[One accountable owner per decision, task, or deliverable where accountability is required.]

| Item | Accountable | Responsible | Consulted | Informed | Escalation | Backup |
|---|---|---|---|---|---|---|
```

Multiple responsible, consulted, or informed parties are permitted when explicit.

## 11. Matrix or portfolio contract

```markdown
# Decision and As-of Rule
[Decision supported and measurement date/state.]

## Axis Definitions
| Axis | Band | Inclusion Rule | Boundary Rule | Unknown Rule |
|---|---|---|---|---|

## Cell Meanings
| Cell | Interpretation | Default Action | Exceptions |
|---|---|---|---|
```

Validate each axis independently before validating cell assignments.

## 12. Screenshot reconstruction contract

```markdown
# Literal Source Recovery
| Visual ID | Literal Content | Shape / Position / Connector | Confidence | Issue |
|---|---|---|---:|---|

## Recovered Logic
[Faithful interpretation of what the source appears to mean.]

## Uncertain Interpretations
[Load-bearing ambiguities and proposed defaults.]

## Rebuilt Version
[Corrected artifact.]

## Traceability
| Rebuilt Element | Source Visual IDs | Provenance | Notes |
|---|---|---|---|
```

## 13. Executive deck or document architecture

Use conclusion-led section titles.

```yaml
governing_thought: "[Executive answer]"
key_line:
  - id: K1
    title: "[Conclusion 1]"
    role: "why | what | how | implication"
    evidence_ids: [E1]
  - id: K2
    title: "[Conclusion 2]"
    role: "why | what | how | implication"
    evidence_ids: [E2]
sections:
  - id: S1
    title: "[Action title]"
    message: "[One controlling idea]"
    support: []
appendix: []
```

## 14. Machine-readable artifact handoff

Use with `PREPARE_ARTIFACT_HANDOFF`.

```yaml
artifact_type: slide_deck | document | spreadsheet | diagram | other
audience: ""
decision: ""
governing_thought: ""
key_line:
  - id: ""
    statement: ""
    order_logic: logical | chronological | structural | comparative | causal_dependency
sections:
  - id: ""
    parent_id: null
    title: ""
    role: ""
    content: []
    evidence_ids: []
    provenance: SOURCE | DERIVED | ASSUMPTION | OPEN
sources:
  - id: ""
    location: ""
    note: ""
assumptions: []
open_questions: []
ce_status: PROVEN | SUPPORTED | ASSUMED | NOT_ESTABLISHED
validation:
  applicable_checks_passed: 0
  applicable_checks_total: 0
  minto_readiness: null
  mece_operational_readiness: null
  critical_gates: PASS | FAIL
  confidence: 0
  grading_isolation: NOT_RUN | INDEPENDENT | QUASI_INDEPENDENT
format_constraints: []
```

A renderer may compress wording or adjust layout. It may not change hierarchy, scope, basis, evidence mapping, assumptions, or validation state without revalidation.
