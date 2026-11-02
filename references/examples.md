# Worked Examples

Use these only when a rendered pattern is unclear. Adapt the logic; do not copy labels blindly.

## Example 1 — Concise `EVALUATE` for a partition

### Input

```text
Is this territory list MECE: United States, North America, Europe, APAC?
```

### Output pattern

```markdown
# Verdict
FAIL — United States is contained within North America, so the peer list overlaps.

## Minimum Fix
Choose one geographic level. For example:

- North America
- Europe
- Asia-Pacific
- Latin America
- Middle East and Africa

Boundary rule: classify each account by headquarters country as of quarter-end. Define a separate `Unknown headquarters` route until data is corrected.

## Validation
- Archetype: partition
- Material failure: S4 applicable_overlap_test = FALSE
- CE status: SUPPORTED until the intended global scope and country-to-region mapping are confirmed
```

The response does not lead with a generic definition, progress checklist, or full rubric.

## Example 2 — `REPAIR` a Definition of Done

### Input

```text
Tracking works; creative is good; landing page optimized.
```

### Repaired pattern

```markdown
# Done Means
The campaign may launch only when every required criterion below is satisfied or formally waived.

| Gate | Atomic Criterion | Evidence | Pass Threshold | Accountable Approver | Failure Action |
|---|---|---|---|---|---|
| Measurement | Primary conversion event fires once per successful submission | QA event log and analytics debug view | 10/10 scripted submissions recorded once with required parameters | Analytics Lead | Block launch and return to implementation |
| Creative | Final assets match approved copy, dimensions, and brand rules | Signed creative QA checklist | 100% required checks pass | Creative Director | Revise and re-review |
| Landing page | Page meets agreed performance and functional tests | Test report | Mobile LCP <= agreed threshold; all required links and forms pass | Web Lead | Block launch and remediate |

## Logic
`DONE = measurement_pass AND creative_pass AND landing_page_pass`
```

The criteria jointly define completion. The campaign is not classified into exactly one criterion.

## Example 3 — `CREATE` an issue tree with interactions

### Governing question

```text
Why did subscription churn increase this quarter?
```

### Working structure

```text
1. Did the customer mix become more churn-prone?
   1.1 Segment mix
   1.2 Contract and tenure mix

2. Did the delivered customer experience deteriorate?
   2.1 Product reliability and value realization
   2.2 Support and onboarding experience

3. Did commercial conditions increase cancellation pressure?
   3.1 Pricing and packaging changes
   3.2 Competitor offers and switching incentives

4. Did measurement or timing create an apparent increase?
   4.1 Cohort and denominator changes
   4.2 Billing, cancellation, or reporting-policy changes
```

Interaction terms are tested separately, such as whether a price change disproportionately affected low-adoption customers. Real churn events are not forced into exactly one cause.

## Example 4 — Four-question clarification batch with defaults

```markdown
1. **Decision:** Should this diagnose causes, assign ownership, or govern execution?  
   Default: diagnose causes, because the request asks “why.”

2. **Scope:** Does “growth” include acquisition, expansion, and retention?  
   Default: yes, all three, because no narrower boundary is stated.

3. **Atomic unit:** Should one leaf represent a causal driver or an initiative?  
   Default: causal driver; initiatives should follow after diagnosis.

4. **Deliverable:** Should the approved logic become a six-slide leadership deck?  
   Default: yes, with one governing thought, three key-line slides, one action slide, and one appendix/assumptions slide.
```

Each question can be answered by confirming or replacing the proposed default.

## Example 5 — Applicability-aware validation

A static document taxonomy does not automatically need an accountable owner per category, workflow transitions, retries, or failure actions.

```text
C1–C8: applicable
S1–S8: applicable
S9: NOT_APPLICABLE unless cross-category relationships are intentionally modeled
O1–O3 and O7: applicable when the taxonomy drives classification decisions
O4–O6: NOT_APPLICABLE for a descriptive taxonomy with no governance workflow
O8: applicable only when handed to another renderer or system
O9: applicable
```

Do not fail a structure for omitting fields the archetype and decision do not require.
