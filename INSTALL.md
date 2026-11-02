# Install WYN MECE

These instructions are for an agent whose user has asked it to install **wyn-mece**. Complete the installation, verify it, and report the result.

## Source and layout

- Repository: https://github.com/wynwithus/wyn-mece
- Source branch: `main`, unless the user requests a particular release or commit.
- Skill name: `wyn-mece`.
- Skill path within the repository: `.` (the repository root).
- Installed layout: `<skills-directory>/wyn-mece/SKILL.md`, with the supporting files beside it.

## Installation steps

1. Identify your host's supported skill installer and the user's requested scope. Use personal scope when no project-specific scope was requested. Check for an existing installation and preserve local customizations.
2. Use the host's installer to install the skill from this repository's root. In Codex, use the available `skill-installer` with repository `wynwithus/wyn-mece`, path `.`, and destination name `wyn-mece`. Other hosts should use their own supported installer.
3. If no installer is available but you can write files, download or clone the repository and copy its contents into the host's `wyn-mece/` skill directory. Keep the original file contents and relative paths, including all references, scripts, assets, evaluation files, and license notices that are present. Exclude Git metadata, caches, and generated build output.
4. Read the installed `SKILL.md`. Verify that its frontmatter name is `wyn-mece`, that supporting files are present, and that relative file links resolve. Use the host's skill listing or discovery mechanism when available.
5. Report the installed path, scope, and source revision. Explain how to invoke the skill and whether the host requires a reload or new session. Claim successful installation only after verifying the persisted files or the host's installation result.

If this environment cannot install reusable skills, explain the limitation and point the user to the manual-import or chat option in [the README](https://github.com/wynwithus/wyn-mece#readme).

## Optional Skills CLI

When Node.js and the Skills CLI are available, these are personal-scope examples. Run the command for the actual host:

```bash
# Codex
npx skills add wynwithus/wyn-mece --skill wyn-mece --agent codex --global --yes

# Claude Code
npx skills add wynwithus/wyn-mece --skill wyn-mece --agent claude-code --global --yes
```

Omit `--global` for a project-scoped installation. Other hosts use their own agent identifier. See the [CLI options](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) and [supported agents](https://github.com/vercel-labs/skills/blob/main/docs/agents.md).

After installation, use the matching CLI listing or host discovery command and check the installed skill files. A pasted prompt applies instructions to a conversation; it does not establish a reusable installation.
