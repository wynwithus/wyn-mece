# Changelog

## 3.2.1 — Public WYN release

- Published as `wyn-mece` with WYN interface metadata and a shorter discovery description.
- Added public installation instructions, summon examples, and an MIT license consistent with WYN Clarify.
- Excluded local caches, discarded files, and historical review scores from the public package.
- Fixed numeric-interval validation to preserve large integers and decimal boundaries and reject non-finite input.
- Rejected missing-data category names that collide with numeric bands.
- Tightened negative-fixture checks and excluded incomplete assertion lists from evaluation pass counts.
- Clarified verdict precedence and adapter separation of task inputs from grading answers.
- Revalidated package structure, references, evaluation definitions, and deterministic fixtures for this release.

## 3.2.0

### Definitions and construction

- Added archetype-qualified literal definitions of mutual exclusivity and collective exhaustiveness.
- Kept exact-one membership limited to bounded partitions and exclusive decision predicates.
- Replaced overlapping ordering labels with logical, chronological, structural, comparative, and causal/dependency relations.
- Limited predecessor and blocker requirements to execution and dependency sequences.
- Added a focused construction-pattern reference covering basis selection, mixed-basis anti-patterns, bounded residuals, and evidence-safe vague-verb conversion.

### Deterministic validation

- Extended `validate_partition.py` with numeric interval validation for endpoint inclusivity, overlaps, gaps, domain coverage, missing-data routing, and supplied value assignments.
- Added passing and failing interval fixtures and included both in static package validation.

### Regression coverage

- Added output evaluations for archetype-safe literal definitions and the repaired ordering taxonomy.
- Preserved the v3.0 primary-mode routing, applicability-aware checks, proportional output behavior, artifact handoff schema, and evaluation harness.
- Removed the unsupported `compatibility` frontmatter key so the package passes the current bundled skill validator.

## 3.0.0

### Routing and activation

- Replaced five peer modes with one primary mode: `EVALUATE`, `REPAIR`, or `CREATE`.
- Added optional modifiers: `RECONSTRUCT`, `OPERATIONALIZE`, and `PREPARE_ARTIFACT_HANDOFF`.
- Expanded natural-language activation coverage for “make this MECE,” “is this MECE,” tracker holes, duplicated ownership, Boolean acceptance standards, gates, evidence, thresholds, and screenshots.
- Preserved negative boundaries for copyediting, summarization, formatting, styling, and ordinary categorization.

### Clarification and autonomy

- Reduced the initial clarification batch from five questions to four.
- Requires a proposed default and reason with every question.
- Permits one targeted follow-up only when the first answers reveal a new contradiction or materially different archetype.

### Validation and grading

- Added applicability-aware `TRUE`, `FALSE`, `NOT_APPLICABLE`, and `NOT_ESTABLISHED` statuses.
- Added compact `C`, `S`, and `O` checks with archetype applicability guidance.
- Separated `READINESS_SCORE` from `CONFIDENCE`.
- Replaced universal operational requirements with archetype- and decision-specific applicability.
- Clarified that failed checks and root causes are many-to-many.
- Added evidence-led critical gates and a maximum of three internal repair passes.
- Distinguishes `INDEPENDENT` grading from same-context `QUASI_INDEPENDENT` grading.

### Output behavior

- Added proportionality rules: routine passes are compressed; material failures are expanded.
- Prohibits user-visible progress checklists and generic rubric-first openings.
- Added mode-specific contracts and a structured failure record with minimum revised wording.
- Added worked examples for concise evaluation, Definition of Done repair, issue-tree creation, clarification defaults, and applicability-aware scoring.
- Updated artifact handoff fields to preserve applicable checks, readiness, confidence, and grading isolation.

### Evaluation and tooling

- Expanded routing evals to 24 balanced cases: 12 positive and 12 negative.
- Expanded output evals to 16 cases covering proportionality, applicability, readiness-confidence separation, and mode-plus-modifier routing.
- Added a standard-library static package validator.
- Added a model-agnostic adapter harness for fresh-session with-skill and without-skill runs and benchmark summaries.
- No empirical runtime results are bundled.
