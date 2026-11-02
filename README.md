# WYN MECE

**Find what overlaps, what is missing, and what needs a clearer rule.**

WYN MECE is a free AI skill by [WYN](https://wynwithus.com). Bring a plan, list, framework, tracker, org model, screenshot, or diagram. It can evaluate the structure, repair it, or build one from your requirements, with clear rules and disclosed assumptions.

MECE means **mutually exclusive and collectively exhaustive**: the parts avoid double-counting and cover the scope you actually defined. The skill selects the right test for the structure. A customer segmentation needs exactly one category per customer; a Definition of Done needs all required criteria satisfied; a causal model needs its interactions preserved.

## When to summon it

Use **`$wyn-mece`** when the structure affects a decision:

| You need to… | Try asking… |
| --- | --- |
| Audit a framework | “Use $wyn-mece. Is this MECE? Show the gaps, overlap, and minimum repair.” |
| Repair mixed logic | “Use $wyn-mece to rebuild these workstreams around one clear organizing rule.” |
| Define categories | “Use $wyn-mece to make these customer segments exhaustive, with no double-counting and explicit boundary rules.” |
| Diagnose a problem | “Use $wyn-mece to create an issue tree for why churn increased. Separate hypotheses from evidence.” |
| Make completion testable | “Use $wyn-mece to turn ‘launch ready’ into a Definition of Done with evidence, thresholds, owners, and failure actions.” |
| Clarify ownership | “Use $wyn-mece to find duplicated accountability and unowned decisions in this responsibility model.” |
| Complete a workflow | “Use $wyn-mece to find missing states, handoffs, exceptions, and terminal outcomes in this process.” |
| Recover a diagram | “Use $wyn-mece to reconstruct this screenshot, flag uncertain labels, and repair its structure.” |
| Prepare executive content | “Use $wyn-mece to organize this argument into an answer-first deck outline with evidence and disclosed assumptions.” |

You can also say **“make this MECE,” “is this MECE?”, “find the gaps and overlap,”** or **“make the acceptance criteria testable.”** An assistant that supports automatic skill selection may summon it from those requests.

Use ordinary editing for tone, grammar, summaries, formatting, or visual polish. Summon WYN MECE when completeness, exclusivity, sequencing, accountability, or acceptance logic matters.

## Install and summon

Ask your skill-capable assistant:

> Install the wyn-mece skill from https://github.com/wynwithus/wyn-mece into my personal skills folder. Read its SKILL.md, then use it to review this framework: [paste your framework].

For a manual installation, copy this repository's complete contents into a skill folder named `wyn-mece` in the location your assistant uses for skills. Keep `SKILL.md`, `references/`, `scripts/`, `assets/`, and `agents/` together; the supporting files are part of the skill. Open a fresh session after installing if your assistant discovers skills at session start.

[Download the installable ZIP](https://github.com/wynwithus/wyn-mece/releases/latest/download/wyn-mece.zip). It contains a `wyn-mece/` folder with `SKILL.md` at its root. Use your assistant's skill import option if it supports this package format, or extract it into its skills directory.

Then ask:

```text
Use $wyn-mece to review the following framework.
Decision: [what this needs to help us decide]
Scope: [what is included and excluded]
Framework: [paste content or attach a screenshot]
```

Explicit invocation syntax depends on the host. `$wyn-mece` is the Codex-style example; in another assistant, ask it to use WYN MECE or its installed skill invocation control.

## What you get

- A verdict, repaired framework, or completed structure first.
- Material gaps, overlaps, mixed organizing logic, and the smallest useful fixes.
- Observable criteria, owners, evidence, and failure paths when the task needs execution.
- Source-backed content separated from derivations, assumptions, and open questions.
- Validation appropriate to the structure, with coverage claims limited to the available evidence.

The skill supports taxonomies, issue trees, workflows, Definitions of Done, decision trees, ownership models, matrices, causal models, and narrative architectures. It keeps legitimate parallel work, shared contributors, and feedback loops intact.

## Requirements and validation

The instructions run in an assistant that can read the skill and its references. Deterministic partition and numeric-band checks use Python 3.10+ and only the standard library. The skill needs no API key or background service of its own.

From this repository's root:

```bash
python scripts/validate_skill.py .
python evals/run_evals.py validate
python -m unittest discover -s tests -v
```

The package includes 24 activation cases, 18 output-quality cases, and passing/failing partition and interval fixtures. The [evaluation harness](evals/README.md) requires a target-client adapter for fresh-session model comparisons. Static checks and human/agent review do not establish measured model accuracy; see [release validation](RELEASE_VALIDATION.md) for the checks actually run.

## Package

- [SKILL.md](SKILL.md): skill instructions and routing.
- [references/archetypes.md](references/archetypes.md): structure-specific validity rules.
- [references/check-catalog.md](references/check-catalog.md): applicable validation checks.
- [references/output-contracts.md](references/output-contracts.md): deliverable formats.
- [scripts/validate_partition.py](scripts/validate_partition.py): finite-partition and numeric-interval validator.
- [evals/README.md](evals/README.md): evaluation definitions and adapter contract.

Version **3.2.1**, based on WYN's local MECE 3.2.0 skill. Released under the [MIT License](LICENSE).
