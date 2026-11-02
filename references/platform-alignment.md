# 2026 Platform Alignment Notes

Reviewed: 2026-07-21

This file documents release-level design choices. It is not part of the routine MECE workflow.

## OpenAI / ChatGPT / Codex

Current OpenAI guidance treats a skill as a focused directory containing required `SKILL.md` instructions and optional `scripts/`, `references/`, `assets/`, and `agents/openai.yaml`. Codex first sees the skill name and description, then loads the full instructions only after activation. OpenAI recommends concise descriptions with clear scope, boundaries, and natural trigger phrases; imperative inputs and outputs; instructions before scripts unless deterministic execution improves reliability; and prompt testing for activation and output behavior.

Sources:

- https://developers.openai.com/codex/build-skills
- https://developers.openai.com/codex/learn/best-practices
- https://developers.openai.com/blog/eval-skills

Package implications:

- The description front-loads `Evaluate`, `repair`, `create`, `MECE`, and common user phrases.
- Negative trigger boundaries are explicit.
- `SKILL.md` contains the core workflow; detailed archetypes, rubrics, contracts, and eval guidance use progressive disclosure.
- Scripts are limited to deterministic validation and a model-agnostic eval harness.
- `agents/openai.yaml` supplies optional interface metadata and implicit invocation policy.

## Anthropic / Claude

Current Claude Code guidance follows the Agent Skills open standard, uses descriptions for automatic invocation, recommends concise skill bodies with supporting files for detail, and explicitly advises keeping `SKILL.md` under 500 lines. Anthropic separates activation quality from output quality and recommends fresh-session comparisons with the skill enabled and disabled. Its skill-creator workflow records prompts, input files, assertions, grading, benchmarks, and blind version comparisons.

Sources:

- https://code.claude.com/docs/en/skills
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- https://platform.claude.com/docs/en/test-and-evaluate/develop-tests

Package implications:

- `SKILL.md` remains below 500 lines.
- Instructions are direct, imperative, and answer-first.
- The skill uses supporting references rather than loading all detail on every invocation.
- Eval definitions separate trigger cases from output assertions.
- The harness supports isolated with-skill and without-skill result collection through a target-client adapter.

## Cross-platform constraints

- Keep the skill focused on one coherent job: engineering decision-ready MECE frameworks and materials.
- Use structural archetype selection before validation to prevent category errors.
- Preserve source content and label interpretation, assumptions, and open questions.
- Use deterministic scripts only for finite, mechanically checkable claims.
- Treat static design review and runtime model performance as different evidence classes.
- Do not claim measured trigger accuracy or output pass rates without actual fresh-session runs.
