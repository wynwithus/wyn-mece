# WYN MECE

Paste in a checklist, a plan, or an answer from ChatGPT. WYN MECE helps you find missing steps, combine repeated tasks, and make it clear who does what. Try it for a move, a family event, or a small-business project.

## When to use it

- “Check my moving list. What have I forgotten, and what have I listed twice?”
- “Help me turn these ideas for a family party into a plan. Who needs to do what?”
- “ChatGPT gave me this marketing plan. Make it easier to follow and tell me what I need to do first.”
- “Check this project plan. Is anything missing, and how will we know each step is finished?”

Copy the instructions into your AI chat, then add the plan or answer you want help with.

## Download and install

The same skill files work across tools that support the [Agent Skills format](https://agentskills.io/specification). No edits to the skill files are needed.

| App | Installation | How to summon it |
| --- | --- | --- |
| Claude | [Download wyn-mece.zip](https://github.com/wynwithus/wyn-mece/releases/latest/download/wyn-mece.zip). In Customize > Skills, choose + Create skill > Upload a skill, upload the ZIP, and enable it. | Ask Claude to use WYN MECE. |
| Claude Code | Extract the ZIP so `SKILL.md` is at `~/.claude/skills/wyn-mece/SKILL.md`, or `.claude/skills/wyn-mece/SKILL.md` for one project. | `/wyn-mece` |
| ChatGPT with Skills enabled | In Plugins > Skills, choose Create > Upload from your computer and upload `wyn-mece.zip`. | Select WYN MECE with `@`, or ask for it by name. |
| Codex | Ask `$skill-installer` to install the skill from this repository's root as `wyn-mece`. Or extract the ZIP into `~/.agents/skills/`, keeping the `wyn-mece/` folder. | `$wyn-mece` |
| Gemini CLI | Run `gemini skills install https://github.com/wynwithus/wyn-mece`. You can also download [wyn-mece.skill](https://github.com/wynwithus/wyn-mece/releases/latest/download/wyn-mece.skill) and run `gemini skills install ./wyn-mece.skill`. | Ask Gemini to use WYN MECE. Run `/skills reload` if it was added during the session. |
| Gemini web or mobile | Create a Gem on the web. Upload [WYN-MECE.txt](https://github.com/wynwithus/wyn-mece/releases/latest/download/WYN-MECE.txt) under Knowledge. Paste [CHAT-INSTRUCTIONS.txt](CHAT-INSTRUCTIONS.txt) into Instructions and save. | Open the Gem and send your framework or request. |
| Other assistants | Import the ZIP if the app supports Agent Skills. Otherwise, attach `WYN-MECE.txt` and send the text from `CHAT-INSTRUCTIONS.txt`. You can also paste the complete text file into a chat that has room for it. | Ask the assistant to use WYN MECE for your request. |

Claude's upload format and description limit are documented in [custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills); its upload steps are in [using skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude). See [Claude Code skills](https://code.claude.com/docs/en/skills) for local installation.

ChatGPT skill uploads depend on account and workspace access. See [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) and [OpenAI's skill guide](https://developers.openai.com/codex/skills/) for upload, discovery, and invocation details.

Google documents [Gemini CLI installation](https://geminicli.com/docs/cli/using-agent-skills/) separately from [Gems](https://support.google.com/gemini/answer/15146780?hl=en) and [Gem knowledge files](https://support.google.com/gemini/answer/15235603?hl=en). The text file contains the skill instructions, references, templates, and scripts together, so chat users can supply them without changing the content.

Each app has its own installation controls, account restrictions, file limits, and code execution tools. The text-file option supplies the instructions in the current chat; it becomes a reusable installation only when the app saves it as a skill, Gem, or equivalent. Python helpers need Python 3.10+ and permission to run code. An app without code execution can read the instructions but cannot run those helpers.

## Original skill and packaging

The skill body, references, templates, Python scripts, and evaluation files match WYN's original MECE 3.2.0 skill. Only the public name, discovery description, and interface metadata differ. The 169-character description fits Claude's documented 200-character limit.

Package version 3.2.2 restores the original content after the first public package included functional changes. Those changes have been removed from the current release. [Source hashes](packaging/source-manifest.json) and distribution checks verify preservation.

The ZIP contains one `wyn-mece/` folder with `SKILL.md` and all supporting resources. The `.skill` download is the same ZIP with the extension used by Gemini CLI. `WYN-MECE.txt` combines the source files without rewriting their contents. Build files and distribution checks stay outside the installable ZIP.

Package 3.2.3 updates the descriptions and examples for people who are new to AI skills. The skill instructions and supporting files are unchanged.

To check or rebuild the package:

```bash
python scripts/validate_skill.py .
python evals/run_evals.py validate
python tools/package_skill.py
python -m unittest discover -s tests -v
```

The original evaluation runner includes 24 activation cases and 18 output cases. It needs a client adapter to measure model behavior. [Release validation](RELEASE_VALIDATION.md) records what was checked; compatibility with the file format does not establish tested behavior in every app.

## Rights and attribution

You may **fork, improve, reuse, and share** WYN MECE, including commercially, under the [MIT License](LICENSE).

**You must credit Nick Cybela** by retaining his copyright notice and the full MIT permission notice in all copies or substantial portions of the skill, including modified versions. Keep other applicable copyright notices too. See [TERMS.md](TERMS.md) for the reuse and attribution details.

Package 3.2.4 adds explicit reuse and attribution terms, names Nick Cybela in the copyright notice, and includes those terms in the downloads. The skill instruction body and original supporting resources are unchanged.
