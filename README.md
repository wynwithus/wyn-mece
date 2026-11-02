# WYN MECE

Free skill for AI assistants to review plans and checklists. Find missing steps, combine repeated tasks, and clarify who does what.

Try it for a move, a family event, or a small-business project.

## When to use it

- “Check my moving list. What have I forgotten, and what have I listed twice?”
- “Help me turn these ideas for a family party into a plan. Who needs to do what?”
- “ChatGPT gave me this marketing plan. Make it easier to follow and tell me what I need to do first.”
- “Check this project plan. Is anything missing, and how will we know each step is finished?”

## Install with your agent

Give your agent this repository's URL and ask it to install **wyn-mece**. The agent can handle the setup for you.

For example:

> Install wyn-mece from https://github.com/wynwithus/wyn-mece as a reusable skill for my assistant.

### Instructions for agents

If the user has asked you to install this skill, **perform the installation** using [INSTALL.md](INSTALL.md). The skill is at the repository root: `SKILL.md` and its supporting files belong in one `wyn-mece/` skill folder. Use your host's skill installer or skills directory, verify the installed files, and tell the user where the skill was installed and how to use it.

### Install from a terminal

If you use the [Skills CLI](https://github.com/vercel-labs/skills), run:

```bash
npx skills add wynwithus/wyn-mece --skill wyn-mece
```

Choose your assistant and installation scope when prompted. Add `--global` for an installation available across projects. This optional method requires Node.js 22.20 or later; an agent can also use its own installer.

## Import or install it yourself

The same skill files work across tools that support the [Agent Skills format](https://agentskills.io/specification). No edits to the skill files are needed.

| App | Installation | How to summon it |
| --- | --- | --- |
| Claude | [Download wyn-mece.zip](https://github.com/wynwithus/wyn-mece/releases/latest/download/wyn-mece.zip). In Customize > Skills, choose + Create skill > Upload a skill, upload the ZIP, and enable it. | Ask Claude to use WYN MECE. |
| Claude Code | Extract the ZIP so `SKILL.md` is at `~/.claude/skills/wyn-mece/SKILL.md`, or `.claude/skills/wyn-mece/SKILL.md` for one project. | `/wyn-mece` |
| ChatGPT with Skills enabled | In Plugins > Skills, choose Create > Upload from your computer and upload `wyn-mece.zip`. | Select WYN MECE with `@`, or ask for it by name. |
| Codex | Ask your agent to install from this repository using [INSTALL.md](INSTALL.md), or extract the complete ZIP into your host's skills directory. | `$wyn-mece` |
| Gemini CLI | Run `gemini skills install https://github.com/wynwithus/wyn-mece`. You can also download [wyn-mece.skill](https://github.com/wynwithus/wyn-mece/releases/latest/download/wyn-mece.skill) and run `gemini skills install ./wyn-mece.skill`. | Ask Gemini to use WYN MECE. Run `/skills reload` if it was added during the session. |
| Gemini web or mobile | Create a Gem on the web. Upload [WYN-MECE.txt](https://github.com/wynwithus/wyn-mece/releases/latest/download/WYN-MECE.txt) under Knowledge. Paste [CHAT-INSTRUCTIONS.txt](CHAT-INSTRUCTIONS.txt) into Instructions and save. | Open the Gem and send your framework or request. |
| Other assistants | Import the ZIP if the app supports Agent Skills. Otherwise, attach `WYN-MECE.txt` and send the text from `CHAT-INSTRUCTIONS.txt`. You can also paste the complete text file into a chat that has room for it. | Ask the assistant to use WYN MECE for your request. |

The Python helpers require Python 3.10+.

## Rights and attribution

You may **fork, improve, reuse, and share** WYN MECE, including commercially, under the [MIT License](LICENSE).

**You must credit Nick Cybela** by retaining his copyright notice and the full MIT permission notice in all copies or substantial portions of the skill, including modified versions. Keep other applicable copyright notices too. See [TERMS.md](TERMS.md) for the reuse and attribution details.
