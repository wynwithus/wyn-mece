# Structural Archetypes and Correct MECE Tests

MECE is evaluated differently by structure type. Select the archetype before applying a validator.

## 1. Partition, taxonomy, or segmentation

### Purpose

Assign each entity in a bounded universe to one category.

### Formal rule

```text
For every x in U:
  category_count(x) = 1
```

### Required fields

- bounded universe `U`;
- atomic entity `x`;
- category set `C`;
- inclusion and exclusion rules;
- boundary handling;
- residual policy.

### Pass tests

- Every item maps to exactly one category.
- Category definitions use one basis at each level.
- Numeric intervals specify inclusive and exclusive endpoints.
- Null, unknown, mixed, and not-applicable cases have explicit rules.
- Reclassification over time is handled by an “as-of” date or state rule.

### Deterministic numeric-band check

Use `scripts/validate_partition.py` with an `intervals` object when a one-dimensional numeric segmentation needs mechanically verified endpoints and coverage:

```json
{
  "intervals": {
    "domain": {"min": 0, "max": null},
    "bands": [
      {"name": "lower", "min": 0, "min_inclusive": true, "max": 100, "max_inclusive": false},
      {"name": "upper", "min": 100, "min_inclusive": true, "max": null}
    ],
    "values": {"known-item": 100, "unknown-item": null},
    "missing_data_category": "unknown"
  }
}
```

`null` endpoints are unbounded and must not carry inclusivity flags. Every finite endpoint requires an explicit Boolean inclusivity flag. A strict pass proves the supplied band geometry and value routing only; it does not prove that the domain, measurement unit, as-of rule, or segmentation basis is correct or useful.

### Common failures

- Geography mixed with customer size.
- Current status mixed with historical behavior.
- A customer qualifies for two personas.
- “Other” absorbs unexamined volume.

## 2. Issue tree or problem decomposition

### Purpose

Break a governing question into distinct sub-questions or drivers that together resolve it.

### Formal rule

For each parent question `P` with children `Q1…Qn`:

```text
vertical_valid = answers(Q1…Qn) are sufficient to answer P
horizontal_valid = Qi are logically distinct and use one basis
```

Exact-one assignment of real-world events is not required unless the leaves are also a partition.

### Pass tests

- Every child is phrased as the same logical type: question, driver, or hypothesis.
- No child is merely a restatement of the parent.
- The same driver is not counted under multiple branches.
- Interactions are isolated as a separate term, bridge, or sensitivity.
- The tree terminates at answerable, testable leaves.

### Common failures

- Symptoms mixed with causes.
- Levers mixed with constraints.
- Revenue drivers mixed with implementation actions.
- A branch called “market” and another called “customer demand.”
- Causal interaction hidden to preserve artificial exclusivity.

## 3. Workflow, lifecycle, or execution plan

### Purpose

Define how work or an entity moves through ordered states or activities.

### Core rule

MECE applies to current states and transition logic, while sequence validity applies to steps.

```text
state_partition_valid = each active case has one current state, unless parallel states are explicitly allowed
transition_valid = every state has defined valid next states, exit, and exception handling
```

### Required fields

- trigger or entry condition;
- state or stage names;
- owner;
- inputs and outputs;
- dependencies;
- exit criteria;
- exception, retry, rollback, and failure paths;
- terminal states.

### Pass tests

- Stages are states or activities, not a mixture.
- Each work item has an unambiguous current state.
- Parallel work is represented as parallel lanes, not forced into one stage.
- Failed, cancelled, paused, and reopened cases are covered.
- Handoffs specify who owns the item before and after transition.

### Common failures

- “Review” is both a stage and an action inside every stage.
- A process jumps from input to output without validation.
- Exception handling is omitted.
- Milestones and departments are mixed as sibling stages.

## 4. Definition of Done or gate model

### Purpose

Define a conjunction of completion requirements.

### Formal rule

```text
DONE = criterion_1 AND criterion_2 AND ... AND criterion_n
```

The criteria do not classify the same item; exact-one is therefore not the core test. MECE means each requirement appears once, is placed under one gate, and the full set covers the intended acceptance state.

### Required fields

- criterion;
- observable evidence;
- binary or explicitly multi-state test;
- threshold;
- accountable approver or owner;
- failure action;
- timing or validity window where relevant.

### Pass tests

- Criteria are observable and testable.
- Vague verbs are paired with evidence and thresholds.
- No criterion duplicates another in different words.
- The set covers functional, quality, compliance, operational, and handoff requirements that are in scope.
- Waivers have an owner, reason, expiry, and approval path.

### Common failures

- “Team aligned.”
- “Tracking works.”
- One criterion contains several independent tests.
- Owner and approver are conflated.
- Evidence is unavailable until after launch.

## 5. Decision tree

### Purpose

Route one case through predicates to one outcome or next action.

### Formal rule

At every decision node:

```text
exactly_one(branch_predicate) = TRUE
```

### Pass tests

- Predicates are mutually exclusive at the same point in time.
- Predicates cover null, unknown, timeout, and error states.
- Branch labels are executable tests, not subjective adjectives.
- Terminal outcomes are explicit.
- No branch depends on information unavailable at that node.

### Common failures

- “High value” and “strategic” overlap.
- No branch for missing data.
- A yes/no node includes a third “maybe” path without redefining the predicate.

## 6. Responsibility or ownership model

### Purpose

Assign decision rights and work ownership.

### Core rule

```text
accountable_owner_count(task_or_decision) = 1
```

Multiple responsible contributors, consulted parties, or informed parties may be valid when roles are explicit.

### Pass tests

- Every task, decision, or deliverable has one accountable owner.
- Responsibility, accountability, approval, consultation, and execution are distinguished.
- Shared work has a named integrator or final decision owner.
- Escalation and absence coverage are explicit.
- No orphaned tasks or duplicated accountability.

### Common failures

- “Marketing and Sales” as joint accountable owner.
- A department named as owner with no role or decision right.
- Contributor lists mistaken for ownership.

## 7. Matrix or portfolio model

### Purpose

Classify or compare items along two independent axes.

### Formal rule

```text
row_axis is MECE
AND column_axis is MECE
AND each item maps to one row × one column for the stated time/state
```

### Pass tests

- Axes use distinct dimensions.
- Each axis has clear boundaries.
- The intersection meaning is defined.
- Empty cells are allowed and interpreted.
- The matrix does not disguise a third uncontrolled dimension.

### Common failures

- One axis is size and the other is “enterprise,” which already implies size.
- Quadrant labels replace objective axis definitions.
- Items move across cells without an as-of rule.

## 8. Causal or system model

### Purpose

Represent factors, mechanisms, interactions, feedback loops, and outcomes.

### Core rule

Factors should be distinct at each sibling set, while interactions are modeled explicitly.

```text
outcome = main_effects + interaction_effects + feedback + exogenous_factors
```

The formula may be conceptual rather than numeric.

### Pass tests

- Causes, mechanisms, moderators, outcomes, and symptoms are separated.
- Interactions have their own links or terms.
- Feedback loops are visible.
- Temporal direction is explicit.
- Exogenous or unknown factors are bounded.
- Double counting is prevented in quantification.

### Common failures

- Treating correlated factors as exclusive categories.
- Placing an outcome beside its causes.
- Omitting feedback because it breaks a tree layout.
- Calling a causal inventory “proven exhaustive” without a closed theory or bounded model.

## 9. Narrative, slide deck, or document outline

### Purpose

Communicate a governing thought through grouped support.

### Core rule

```text
governing_thought is supported by key_line_points
AND each sibling group is logically alike, ordered, and sufficient for its parent
```

### Pass tests

- The answer or recommendation appears first.
- Section titles state conclusions or roles, not generic topics.
- Each section contains one controlling idea.
- Supporting points answer the question raised by their parent.
- Detail descends by evidence and implication.
- Appendices hold useful detail that is not needed for the core decision.

### Common failures

- Topic-first titles such as “Market Overview.”
- Chronological research notes presented as the final story.
- Recommendations mixed with evidence at the same level.
- Repeated facts under several sections.

## 10. Hybrid structures

Use linked structures when one artifact cannot legitimately carry all logic.

Examples:

- Issue tree for diagnosis → prioritization matrix → execution roadmap.
- Customer segmentation → segment-specific journey workflows.
- Causal model → intervention decision tree → Definition of Done.
- Ownership matrix → workflow with handoffs.

Rules:

1. Name the role of each structure.
2. Define the handoff unit between them.
3. Keep each structure internally valid.
4. Do not merge different bases into one sibling list.
5. Re-run traceability across the full chain.
