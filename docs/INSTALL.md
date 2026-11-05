# Install

The skills are plain directories. Copy `shared/` and the three skill folders
together, keeping them side by side, because each `SKILL.md` links to
`../shared/`. Copy `examples/` too if you want the worked example links to
resolve.

```text
job-application-skills/
├── zj-baseline-cv/
├── zj-job-fit-evaluation/
├── zj-tailored-application/
├── shared/
└── examples/
```

From the package root, install into a project-level skills directory:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R zj-baseline-cv zj-job-fit-evaluation zj-tailored-application shared examples \
  /path/to/project/.agents/skills/
```

The result is:

```text
/path/to/project/.agents/skills/
├── zj-baseline-cv/
├── zj-job-fit-evaluation/
├── zj-tailored-application/
├── shared/
└── examples/
```

Do not copy a skill folder on its own. Its `../shared/` links will break.

## Agent paths

| Agent                  | Project path                                                                | User path                                                                      | Notes                                                                      |
| ---------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Generic / multi-agent  | `.agents/skills/`                                                           | `~/.agents/skills/`                                                            | Broadest project path                                                      |
| Claude Code            | `.claude/skills/`                                                           | `~/.claude/skills/`                                                            | Also reads the Agent Skills standard                                       |
| OpenAI Codex CLI       | `.agents/skills/` at the working directory, parents, or repository root     | `~/.agents/skills/`                                                            | Initial skill list has a context budget                                    |
| Hermes                 | No dedicated project path; use `~/.hermes/skills/` or an external directory | `~/.hermes/skills/`                                                            | External skill directories are also supported; the agent can modify skills |
| Pi Agent               | `.pi/skills/` or `.agents/skills/`                                          | `<agent-dir>/skills/` (typically `~/.pi/agent/skills/`) or `~/.agents/skills/` | Recursive discovery; `.skills/` is not a Pi discovery path                 |
| Gemini CLI             | `.gemini/skills/` or `.agents/skills/`                                      | `~/.gemini/skills/` or `~/.agents/skills/`                                     | Activation shows a consent prompt                                          |
| Cursor                 | `.cursor/skills/` or `.agents/skills/`                                      | `~/.cursor/skills/` or `~/.agents/skills/`                                     | Also reads `.claude/skills/` and `.codex/skills/`                          |
| Windsurf / Devin Local | `.devin/skills/` or `.agents/skills/`                                       | `~/.config/devin/skills/` or `~/.agents/skills/`                               | `.windsurf/skills/` is legacy                                              |
| Cline                  | `.cline/skills/`, `.clinerules/skills/`, or `.claude/skills/`               | `~/.cline/skills/`                                                             | Name must match the folder                                                 |
| OpenHands              | `.agents/skills/`                                                           | `~/.agents/skills/`                                                            | Legacy `.openhands/skills/` also works                                     |
| Goose                  | `.agents/skills/`                                                           | `~/.agents/skills/`                                                            | Also reads `.goose/skills/` and `.claude/skills/`                          |
| Aider                  | No skill discovery                                                          | No skill discovery                                                             | Use the generated bundle, see below                                        |

The matrix and its sources are in [`COMPATIBILITY.md`](COMPATIBILITY.md).

## Fallback for agents without skill discovery

Some agents read a rules file such as `AGENTS.md`, `CLAUDE.md`, or
`CONVENTIONS.md` instead of discovering skills. Point that file at the package
router:

```markdown
Read job-application-skills/AGENTS.md and follow the routed skill.
```

For a chat-only agent, or an agent that cannot read referenced files, build a
single prompt bundle:

```bash
python3 scripts/build_bundle.py --skill zj-baseline-cv
python3 scripts/build_bundle.py --skill zj-job-fit-evaluation
python3 scripts/build_bundle.py --skill zj-tailored-application
```

The bundles are written to `dist/` and are not committed. Paste the relevant
bundle into the conversation, or add it as a read-only context file:

```bash
# Aider example
aider --read dist/zj-baseline-cv.md
```

## Verify

1. Start the agent in the project where the skills are installed.
2. Ask it to list available skills, or open the skill menu.
3. Invoke the skill on the fictional example in `examples/`.
4. Confirm it reads `SKILL.md`, one shared rule, and one reference file.
5. If the skill does not appear, check the path and restart the agent.

## Update

Replace the skill folders, `shared/`, and `examples/` with the new release.
Keep any project-specific overlay outside the package. Do not edit the installed
general files; change the source package and reinstall.

## Uninstall

Remove the installed skill folders, `shared/`, and `examples/` from the agent's
skills directory. The package does not write outside its own folders.
