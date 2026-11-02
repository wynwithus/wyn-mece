# WYN MECE package 3.2.3

Description update checked November 1, 2026. The description and public examples now explain the skill in everyday language. The original instruction-body and supporting-file preservation checks still apply.

# WYN MECE package 3.2.2 review record

Checked November 1, 2026. Source skill version: 3.2.0.

## Content preservation

The prior public package, 3.2.1, changed a verdict rule, numeric validation, evaluation checks, and some reference text. Package 3.2.2 restores the original source. These functional changes are absent from the current release.

The source manifest records the original instruction-body hash, preserved frontmatter, and hashes for the original supporting files. Text comparison ignores only LF versus CRLF line endings. The distribution tests check those hashes. The permitted differences are the `wyn-mece` public name, discovery description, and UI metadata. The original version, 3.2.0, remains in SKILL.md.

## Distribution checks

- Skill metadata and relative links pass the bundled package validator.
- Original evaluation definitions parse: 24 activation cases and 18 output cases.
- Seven distribution tests check source preservation, the 200-character description limit, complete text export, ZIP contents, extracted references, and identical ZIP/.skill content.
- ZIP entries use one `wyn-mece/` root with no caches or discarded files.
- The plain-text export includes the full skill, references, templates, and Python source without content edits.

The source scripts are preserved as requested. This release makes no claim that their behavior was improved. The previous nine regression tests for functional changes were replaced with distribution and preservation tests.

## Platform review

The README links to the official installation instructions for Claude, Claude Code, ChatGPT, Codex, Gemini CLI, and Gemini Gems. Native skill hosts share the Agent Skills directory layout. Gemini's web app uses a Gem with instructions and a knowledge file, supplied as ready-to-use text.

No authenticated installation was performed in Claude, Gemini, or ChatGPT. No claim of tested model behavior or universal native importing is made. Account access, file limits, and execution tools remain properties of each host. The standalone text export provides a path for chat apps that can read the complete file.
