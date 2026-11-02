# Skill Engineering Review Rubric

This rubric evaluates the `/mece` skill package itself. It is intended for authoring and release review, not routine execution.

Review [platform-alignment.md](platform-alignment.md) before release scoring.

## Universal scoring anchors

- `100%`: explicit, testable, production-ready, and supported by fixtures or validation.
- `90%`: production-ready with only immaterial tuning remaining.
- `75%`: strong draft with one material reliability gap.
- `50%`: usable concept with several material gaps.
- `25%`: mostly aspirational.
- `0%`: absent or invalid.

A release passes only when both reviewers score at least 90, all critical gates pass, and review confidence is at least 90%.

---

# Reviewer A — Minto Architecture of the Skill (100 points)

| Criterion | Weight | Full-credit standard |
|---|---:|---|
| 1. One governing purpose | 12 | The skill solves one coherent job and its purpose can be stated in one sentence. |
| 2. Answer-first instruction hierarchy | 10 | Core rules and workflow precede detail; supporting references are progressively disclosed. |
| 3. Vertical logic | 14 | Every section supports the skill's governing purpose; no orphan instructions. |
| 4. Horizontal logic | 14 | Sibling sections and lists use one logical basis and consistent abstraction. |
| 5. Collective coverage of the job | 14 | Routing, intake, construction, validation, delivery, and failure handling cover the full workflow. |
| 6. Separation of structure types | 12 | Distinct archetypes are separated rather than forced into one universal test. |
| 7. Ordering and sequencing | 8 | The procedure follows a clear inspect → clarify → select → build → validate → deliver sequence. |
| 8. Precision and economy | 8 | Instructions are concise, actionable, and free of repetitive ceremony. |
| 9. Edge-case integrity | 5 | Ambiguity, screenshots, hybrid structures, exceptions, and unbounded universes are handled. |
| 10. Decision usefulness | 3 | The skill reliably produces material that supports a real decision or action. |

### Minto design critical gates

```text
A1 no universal rule creates a category error across structure types
A2 the core workflow is top-down and complete
A3 the skill does not overclaim MECE or certainty
A4 output is answer-first and decision-led
```

---

# Reviewer B — 2026 Agent Skill Engineering (100 points)

| Criterion | Weight | Full-credit standard |
|---|---:|---|
| 1. Trigger description and boundaries | 12 | Frontmatter states what, when, relevant inputs, and near-miss exclusions in under 1024 characters. |
| 2. Coherent scope | 10 | One reusable workflow; adjacent tasks are handed off rather than absorbed. |
| 3. Progressive disclosure | 10 | `SKILL.md` contains core instructions; focused references, scripts, assets, and evals load only as needed. |
| 4. Multimodal and source handling | 10 | Text, files, screenshots, provenance, contradictions, and low-confidence interpretation are explicit. |
| 5. Clarification and autonomy calibration | 10 | The skill asks no more than four material questions with proposed defaults, allows one targeted follow-up, and proceeds with labeled reversible assumptions when appropriate. |
| 6. Routing and conditional workflow | 12 | Branch logic selects one primary mode, optional processing modifiers, and the correct archetype before execution. |
| 7. Determinism and validation | 10 | Deterministic checks are scripted where suitable; applicability, readiness, confidence, evidence-led gates, and a three-pass stopping rule are explicit. |
| 8. Output contracts and handoffs | 8 | Inputs, outputs, artifact boundaries, and downstream handoffs are explicit. |
| 9. Evals and observability | 12 | Balanced trigger and output evals cover positive, near-miss, edge, and regression cases; an executable adapter-based harness supports fresh-run with-skill/without-skill comparison. |
| 10. Portability, safety, and failure handling | 6 | Valid Agent Skills packaging, bounded tool assumptions, helpful errors, and no unsafe silent behavior. |

### Skill engineering critical gates

```text
B1 valid SKILL.md frontmatter and package structure
B2 description has positive and negative routing boundaries
B3 SKILL.md remains below 500 lines and uses progressive disclosure
B4 material ambiguity and screenshot uncertainty are handled
B5 balanced trigger and output fixtures exist and the evaluation harness validates and summarizes fresh-run comparisons
B6 no unsupported claim of empirical performance
```

---

# Release logic

```text
RELEASE_PASS =
  MINTO_SKILL_SCORE >= 90
  AND AGENT_SKILL_ENGINEERING_SCORE >= 90
  AND all critical gates = PASS
  AND review_confidence >= 90
```

## Review confidence

Use the minimum of:

- `spec_alignment_confidence`: alignment with current Agent Skills, ChatGPT/Codex, and Claude guidance;
- `static_validation_confidence`: frontmatter, links, line counts, JSON, and scripts validated;
- `behavioral_design_confidence`: rubric and fixture coverage support the predicted behavior.

Runtime trigger accuracy and output pass rates require execution in the target client. Do not label design review scores as measured runtime performance.
