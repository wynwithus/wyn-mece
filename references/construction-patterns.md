# Construction Patterns

Use this reference when selecting a basis of division, repairing mixed sibling logic, bounding a residual, or converting vague material into testable form. Archetype-specific validity rules remain in [archetypes.md](archetypes.md).

## Basis-of-division catalog

Choose the basis that best supports the governing decision. Use one basis per sibling set; put another basis on a lower level or a separate matrix axis.

- **Formula decomposition:** an identity such as `Profit = Revenue - Cost` or `Revenue = Traffic x Conversion Rate x Average Order Value`. Strong for diagnosing a metric when the identity and units are valid.
- **Lifecycle or state:** one current state per item at the stated time, unless parallel states are explicitly modeled. Strong for pipelines and case management.
- **Process or activity:** work grouped by stage or activity. Strong for execution plans; distinguish activities from states and deliverables.
- **Component or structure:** parts of a defined whole, such as regions, product lines, systems, or organizational units. Test cross-component and shared cases explicitly.
- **Segment attribute:** one declared attribute such as size, industry, tier, or risk. If two attributes matter independently, use a matrix instead of combining them silently in labels.
- **Decision predicate:** branches defined by executable conditions. Include null, unknown, timeout, and error cases where relevant.
- **Causal mechanism:** factors grouped by distinct mechanisms. Preserve interaction terms, feedback, and exogenous factors rather than forcing exact-one membership.

Stock frames such as internal/external, supply/demand, and people/process/tools can generate hypotheses, but they are not automatically complete or decision-useful. Validate them against the parent, scope, and evidence.

## Grouping and ordering heuristics

- Prefer the fewest siblings that preserve meaning and decision usefulness. Three to five often communicates well, but do not force the count or infer a defect from two or more than five alone.
- Every sibling set should support one accurate parent summary. If the parent cannot summarize its children without adding or dropping meaning, repair the vertical logic.
- Use one governing ordering relation: logical implication, chronological sequence, structural arrangement, comparative rank, or causal/dependency relation.
- For an execution or dependency sequence, name prerequisites, downstream blockers, joins, and parallel work. Do not require blocker logic for a structural list, ranked comparison, or ordinary narrative grouping.
- Treat a second classification basis as another level or axis, not as an adjective embedded in one category.

## High-signal anti-patterns

Flag these when they are siblings under one parent:

- channels mixed with tasks;
- outcomes mixed with inputs;
- owners mixed with deliverables;
- symptoms mixed with causes;
- strategic goals mixed with execution steps;
- states mixed with activities or milestones;
- generic labels that differ only in tone rather than inclusion rule;
- `Other`, `Miscellaneous`, `TBD`, `As needed`, or `Various` without a bounded rule and closure path;
- a technically exact partition whose basis does not change any decision, action, priority, ownership, or acceptance state.

## Vague-verb conversions

Convert a vague statement only when the source and decision justify the added specificity. Otherwise mark the required evidence or threshold `OPEN` rather than inventing it.

| Vague expression | Observable replacement pattern |
|---|---|
| optimize / improve | named metric, baseline, target or delta, measurement method, and date |
| ensure | named check, evidence, threshold, and accountable owner where required |
| align | named parties record approval or disagreement on a named artifact by a stated point |
| support | concrete deliverable, service level, decision right, or remove the word |
| handle / manage / coordinate | atomic actions, outputs, handoffs, and exception paths |
| review | reviewer records an outcome against a named standard and identifies the next action |
| ready / good / works | binary or enumerated acceptance test with producible evidence |

Never manufacture thresholds, owners, evidence, or approval states merely to make wording appear operational.
