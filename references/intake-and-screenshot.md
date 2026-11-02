# Intake, Ambiguity, and Screenshot Protocol

Use this reference when the request is underspecified, the source is visual, or the intended structure is uncertain.

## 1. Materiality test for clarification

A missing fact is material when a plausible answer would change one or more of:

- governing decision or audience;
- scope boundary or time horizon;
- atomic unit;
- structural archetype;
- basis of division;
- number or meaning of top-level branches;
- acceptance evidence or threshold;
- recommended action.

Ask when at least one material dependency is unresolved. Proceed with labeled assumptions when ambiguity only affects wording, formatting, or low-impact detail.

## 2. Question prioritization

Rank candidate questions by expected structural information gain:

```text
priority = probability_answer_changes_structure × magnitude_of_change × irreversibility
```

Ask no more than four questions in the initial batch. Give a proposed default and a brief reason with each question so the user can confirm or replace it. Prefer questions that eliminate entire alternative structures. Use one targeted follow-up only when the first answers reveal a new contradiction or materially different archetype.

### Strong question forms

- **Boundary:** “Does the scope include existing customers, prospects, or both? Default: both, because the source uses ‘accounts’ without a lifecycle qualifier.”
- **Unit:** “Should each leaf represent a cause, an action, or a deliverable? Default: cause, because the governing question asks why performance changed.”
- **Axis:** “Should the top level use customer lifecycle, business function, or time? Default: lifecycle, because the decision concerns conversion loss.”
- **Decision:** “Is this for diagnosis, prioritization, ownership, or execution? Default: diagnosis, based on the request to identify drivers.”
- **Evidence:** “What observable result marks each gate complete? Default: named artifact plus approver acceptance.”
- **Forced choice with escape hatch:** “Is the primary audience executives, operators, or clients? Default: executives, because the requested output is a leadership deck.”

### Weak question forms

- “Can you provide more context?”
- “What do you want?”
- “Anything else?”
- Asking for information already visible or supplied.
- Asking about presentation preferences before structure is settled.

## 3. Assumption protocol

When proceeding without an answer:

1. State each material assumption in one sentence.
2. Explain which part of the structure it controls.
3. Use a reversible default.
4. Mark affected branches `ASSUMPTION`.
5. Reduce confidence and collective-exhaustiveness status accordingly.

Do not hide assumptions inside labels or prose.

## 4. Visual evidence ledger

For each meaningful visual element, capture:

| Field | Meaning |
|---|---|
| ID | Stable source identifier, e.g. `V1` |
| Text | Exact visible wording; use `[unreadable]` when needed |
| Container | Box, circle, lane, header, callout, free text, icon |
| Position | Relative location: top, left, row 2, column 3, nested under V4 |
| Connector | Arrow, line, bracket, adjacency, overlap, none |
| Direction | Source → destination when discernible |
| Style cue | Color, weight, size, numbering, indentation |
| Literal meaning | What is directly shown |
| Structural inference | What the layout may imply |
| Confidence | 0–100 for the inference, not for image quality alone |

## 5. Visual grammar detection

Classify the diagram before reconstructing it.

### Hierarchy or tree

Signals:

- one parent above or left of children;
- indentation or containment;
- branching connectors;
- repeated sibling shapes.

Tests:

- Do siblings answer the same parent?
- Are levels consistent?
- Are cross-links evidence of interaction or accidental overlap?

### Workflow or sequence

Signals:

- directional arrows;
- numbered stages;
- start/end symbols;
- swimlanes or handoffs.

Tests:

- Is every arrow direction clear?
- Are entry, exit, exception, retry, and failure paths shown?
- Are categories being mistaken for steps?

### Matrix

Signals:

- two labeled axes;
- rows and columns;
- quadrants or cell intersections.

Tests:

- Is each axis independently MECE?
- Are cells exclusive by definition?
- Are empty cells valid, impossible, or simply missing?

### Timeline

Signals:

- chronological labels;
- left-to-right or top-to-bottom progression;
- milestones and intervals.

Tests:

- Are time periods contiguous and non-overlapping?
- Are activities, outcomes, and dates mixed on the same level?

### Venn-like or overlap map

Signals:

- intersecting circles or regions;
- shared labels in intersections.

Tests:

- Is overlap intentional?
- Does the user's goal require conversion to a partition, matrix, or interaction model?
- Do not label a Venn structure non-MECE merely because it represents real overlap.

### Dashboard or collage

Signals:

- independent cards, metrics, and charts;
- little or no explicit hierarchy;
- visual grouping by proximity.

Tests:

- Is there an implied story or only a collection?
- What decision should govern the regrouping?

## 6. Confidence thresholds for visual interpretation

- `90–100`: explicit label or unambiguous connector.
- `75–89`: strong layout inference; verify when material.
- `50–74`: plausible interpretation; ask before using as a structural premise.
- `<50`: record as unknown; do not use to build logic.

Do not use OCR output as authoritative when it conflicts with visual inspection or context. Use OCR only as a supporting tool when native inspection is insufficient and the environment permits it.

## 7. Source reconstruction sequence

1. Capture literal elements.
2. Build the evidence ledger.
3. Detect visual grammar.
4. Recover parent-child or state-transition relationships.
5. Separate content from styling.
6. Identify structural defects in the source.
7. Ask material questions.
8. Rebuild the content architecture.
9. Map each new element to source, derivation, assumption, or open question.
10. Render only after validation.

## 8. Screenshot-specific failure modes

- Decorative arrows interpreted as dependencies.
- Columns treated as categories when they are merely layout.
- Color used as a category without a visible legend.
- Repeated labels collapsed even though they refer to different stages.
- Cropped branches omitted without disclosure.
- Illegible text guessed from context.
- Existing overlap “fixed” before determining whether it represents a real interaction.
- Styling copied while the source logic remains mixed or incomplete.
