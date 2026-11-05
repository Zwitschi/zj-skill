# Agent compatibility

Status: research pass completed 2026-11-05. Pi, Codex, and the Aider prompt
fallback have been tested; every other row is documented-only. No
universal-compatibility claim is made.

The package follows the [Agent Skills specification](https://agentskills.io/specification)
as its common baseline where an agent supports it. Native support, discovery
paths, frontmatter handling, and tool availability still differ by agent.

## Dimensions

| Dimension                    | What to record                                                                                  | Why it matters                                                                 |
| ---------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Discovery path               | Project, user, and global directories the agent scans                                           | A skill that is not discovered cannot be used                                  |
| Discovery scope              | Which parent directories are searched, and whether search stops at a repository root            | Nested installations may not be found                                          |
| Frontmatter fields           | Required, optional, ignored, and rejected fields                                                | Unknown fields may warn, error, or be ignored                                  |
| Name and description limits  | Maximum length and allowed characters                                                           | The Agent Skills baseline caps names at 64 characters and descriptions at 1024 |
| Loading model                | Index-only advertisement versus full body at startup                                            | Affects context cost and whether references load on demand                     |
| Context and file-size limits | Maximum skill or reference size, truncation behaviour                                           | Long reference files may be cut off                                            |
| Relative links               | Whether links resolve from the skill directory and whether the agent follows them automatically | `../shared/` and `references/` must remain readable                            |
| Tool assumptions             | File read, write, edit, glob, grep, shell, web fetch, search, subagents                         | Claude-specific names break portability                                        |
| Permission model             | Read/write approvals, shell restrictions, network access, project trust                         | A skill must not assume unattended writes or network                           |
| Instruction hierarchy        | System prompt, `AGENTS.md`, `CLAUDE.md`, project skills, user skills, precedence                | Local overlays must not be overridden silently                                 |
| Installation and update      | Copy, symlink, package manager, version pinning                                                 | Upgrades must not overwrite local configuration                                |
| Fallback                     | Rules-file, manual prompt injection, copy-paste, none                                           | Some agents cannot discover skills but can still follow instructions           |

## Support tiers

| Tier | Name         | Requirements                                                                                | Expected experience                                         |
| ---- | ------------ | ------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| 1    | Native skill | Discovers `SKILL.md`, reads the body on demand, can read bundled references, has file tools | Full workflow                                               |
| 2    | Rules-file   | Reads `AGENTS.md` or `CLAUDE.md`, can read files, does not discover skills                  | Full workflow when the skill text is injected or referenced |
| 3    | Manual       | Chat-only or no file tools; user pastes the skill and documents                             | Partial workflow; references and file outputs are manual    |
| 4    | Unsupported  | Cannot read or write files and cannot accept pasted documents                               | Not recommended                                             |

## Evidence standard

For each agent record:

- primary documentation URL;
- documentation version or commit, and access date;
- whether the row is tested with a real CLI or documented only;
- the exact discovery path used in the test;
- frontmatter fields that produced warnings or errors;
- any capability that required a fallback.

Blog posts and third-party summaries may guide the search but are not sufficient
evidence for a matrix row.

## Portable conventions for this package

- One skill per directory, with `SKILL.md` at its root.
- Minimal frontmatter: `name` and `description`. Add `license`, `compatibility`,
  or `metadata` only when useful. Avoid experimental fields in the base package.
- The `name` matches the folder, uses lowercase letters, numbers, and hyphens,
  and stays within 64 characters. The description stays within 1024 characters.
- `SKILL.md` is short. Detail lives in `references/` and is loaded only when
  needed.
- Use relative links from the skill directory, and tell the agent to read the
  linked files. Do not rely on automatic link following.
- Do not require network access, shell access, subagents, or a specific model.
  Use them only when available.
- Markdown only. Use ASCII diagrams, not Mermaid-only diagrams.
- Every skill states what to do when a capability is missing.
- No absolute paths, no personal data, no agent-specific tool names.
- Test on Tier 1 and Tier 2 before release.

## Agent matrix

Rows come from primary documentation, with the version and access date recorded.
Only the Pi row has a local CLI; all other rows are documented-only.

| Agent                  | Version and date                             | Discovery path                                                                                                                          | Frontmatter                                                                                                                                                                                       | Relative links                                                          | Tier | Tested or documented          | Notes                                                                                                                            |
| ---------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ---- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Claude Code            | v2.1.309+ (docs 2026-11-05; npm 2.1.318)     | `.claude/skills/<name>/SKILL.md`; project directories up to the repository root; `~/.claude/skills`; plugins                            | All fields optional; `name` defaults to the folder; `description` recommended; unknown fields ignored; listing truncates `description` plus `when_to_use` at 1,536 characters                     | Resolved from the skill directory; supporting files load on demand      | 1    | Documented only               | Agent Skills standard plus Claude extensions such as `allowed-tools`, subagents, and dynamic context                             |
| OpenAI Codex CLI       | rust-v0.166.0 (2026-10-29)                   | `.agents/skills` at the working directory, parent directories, and repository root; `$HOME/.agents/skills`; admin and system locations  | `name` and `description` required; Agent Skills standard                                                                                                                                          | Resolved from the skill directory; references load on demand            | 1    | Documented only               | Initial list capped at 2% of context or 8,000 characters; descriptions shortened first; `skills.max_context_tokens` up to 10,000 |
| Hermes                 | v0.22.7 (2026-11-03)                         | `~/.hermes/skills/`; external skill directories                                                                                         | Agent Skills standard; house style for `/learn` asks for descriptions of 60 characters or fewer                                                                                                   | Resolved from the skill directory                                       | 1    | Documented only               | The agent can modify or delete skills; installs from hub, URL, or GitHub; treat the installed copy as writable                   |
| Pi Agent               | 1.5.0 (installed 2026-11-05)                 | Project `.pi/skills/` and `.agents/skills/`; user `<agent-dir>/skills/` and `~/.agents/skills/`; recursive                              | `name` and `description`; optional `license`, `compatibility`, `metadata`, `allowed-tools`, `disable-model-invocation`; invalid fields warn; name at most 64 characters, description at most 1024 | Resolved from the skill directory; references load on demand            | 1    | Installed; smoke test pending | Name and folder mismatch is tolerated; matching names are the portable choice                                                    |
| Gemini CLI             | v0.67.0 (2026-11-04)                         | `~/.gemini/skills/`, `~/.agents/skills/`, `.gemini/skills/`, `.agents/skills/`; precedence order                                        | Agent Skills standard; `name` and `description`                                                                                                                                                   | Activation grants access to the skill directory                         | 1    | Documented only               | Activation shows a consent prompt and uses an `activate_skill` tool                                                              |
| Cursor                 | Docs 2026-11-05; changelog 2026-10-20        | `.cursor/skills/`, `.agents/skills/`, `~/.cursor/skills/`, `~/.agents/skills/`; also reads `.claude/skills`, `.codex/skills`; recursive | `name` and `description` required; name must match the folder; optional `paths`, `disable-model-invocation`, `icon`, `color`                                                                      | Resolved from the skill directory; supporting files load on demand      | 1    | Documented only               | Nested skills are scoped to their subdirectory; Cloud Agents warn on invalid frontmatter                                         |
| Windsurf (Devin Local) | Docs 2026-11-05; no version string           | `.devin/skills/`, `.agents/skills/`, legacy `.windsurf/skills/`; global `~/.config/devin/skills/`, `~/.agents/skills/`                  | `name` and `description` in YAML frontmatter                                                                                                                                                      | Resolved from the skill directory; supporting files load on demand      | 1    | Documented only               | Windsurf documentation now redirects to Devin Local; branding change                                                             |
| Cline                  | v4.1.26 (2026-10-26)                         | `.cline/skills/`, `.clinerules/skills/`, `.claude/skills/`; global `~/.cline/skills/`                                                   | `name` must match the folder; `description` at most 1024 characters; body under 5k tokens recommended                                                                                             | Resolved from the skill directory; resources read or executed on demand | 1    | Documented only               | Global skill takes precedence over a project skill with the same name                                                            |
| Aider                  | v0.86.2 (installed 2026-11-05; docs v0.86.0) | No skill discovery; `CONVENTIONS.md` via `/read` or `--read`                                                                            | No `SKILL.md` or frontmatter                                                                                                                                                                      | Read-only file added to context                                         | 2    | Tested fallback 2026-11-05    | Use the generated bundle or a conventions pointer; no progressive disclosure                                                     |
| OpenHands              | v1.35.0 (2026-11-03)                         | `.agents/skills/` project; `~/.agents/skills/` user; legacy `.openhands/skills` and `.openhands/microagents`                            | `name` and `description` required; name matches the folder; optional `triggers`, `paths`                                                                                                          | Resolved from the skill directory; references load on demand            | 1    | Documented only               | Project skills override user skills; legacy paths remain supported                                                               |
| Goose                  | v1.57.0 (2026-10-28)                         | `~/.agents/skills/`, `.agents/skills/`, plugin skills; legacy `.goose/skills`, `.claude/skills`, `~/.claude/skills`                     | `name` and `description` required                                                                                                                                                                 | Resolved from the skill directory; supporting files load on demand      | 1    | Documented only               | Backward compatibility with Claude and Goose directories                                                                         |

## Common findings

- The Agent Skills specification is the common baseline. Nine of the eleven
  rows support `SKILL.md` discovery; Aider does not.
- `.agents/skills/` is the broadest project path: Codex, Gemini, Cursor,
  Windsurf/Devin Local, OpenHands, Goose, and Pi read it. `.claude/skills/` is
  read by Claude Code, Cline, Cursor, and Goose as a compatibility path.
- `name` and `description` are the portable frontmatter pair. Name and folder
  match is enforced by Cursor, Cline, and OpenHands, and is the safest choice
  everywhere. Claude Code defaults the name to the folder.
- Description budgets vary. Claude Code truncates `description` plus
  `when_to_use` at 1,536 characters, Codex shortens descriptions under context
  pressure, Hermes house style asks for 60 characters or fewer, and Pi and Cline
  cap at 1,024. The first sentence must carry the routing signal on its own.
- Relative links resolve from the skill directory in the documented native
  paths, but no agent guarantees automatic link following. The package must keep
  telling the agent to read `../shared/` and `references/`.
- None of the package skills request tool grants. Agents differ on permissions:
  Gemini CLI asks for consent at activation, Claude Code can pre-approve tools
  per skill, and Pi or Cline may prompt for writes.
- Aider is Tier 2 only. It reads `CONVENTIONS.md` as a read-only context file and
  has no skill discovery or progressive disclosure.
- Windsurf documentation now redirects to Devin Local. Its current paths are
  `.devin/skills/` and `.agents/skills/`; `.windsurf/skills/` is legacy.
- Pi and Codex are installed and fully tested. Pi discovery, skill loading, and file reading pass. Codex discovery, skill loading, and file reading pass in read-only mode. Aider 0.86.2 was tested with a generated bundle as a read-only prompt fallback. All other rows are documented-only.
- Pi does not discover `.skills/`. Use `.agents/skills/` or `.pi/skills/`; a `.agents/skills` symlink to `.skills` is discovered. In Pi, `--no-tools` hides skills from the prompt, so smoke tests must keep tools enabled.
- Both Pi and Codex read the same `.agents/skills` path. A single `.agents/skills` symlink to `.skills` serves both, and the same path is available to Gemini, Cursor, Windsurf/Devin Local, OpenHands, and Goose.

## Sources and versions

| Agent                      | Primary source                                                           | Version and access date                                          |
| -------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| Agent Skills specification | https://agentskills.io/specification                                     | Accessed 2026-11-05                                              |
| Claude Code                | https://code.claude.com/docs/en/skills                                   | Docs reference v2.1.309; npm latest 2.1.318; accessed 2026-11-05 |
| OpenAI Codex CLI           | https://developers.openai.com/codex/skills                               | rust-v0.166.0, 2026-10-29; accessed 2026-11-05                   |
| Hermes                     | https://hermes-agent.nousresearch.com/docs/user-guide/features/skills    | v0.22.7, 2026-11-03; accessed 2026-11-05                         |
| Pi Agent                   | Bundled Pi 1.5.0 documentation                                           | 1.5.0; accessed 2026-11-05                                       |
| Gemini CLI                 | https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md | v0.67.0, 2026-11-04; accessed 2026-11-05                         |
| Cursor                     | https://cursor.com/docs/skills.md                                        | Docs accessed 2026-11-05; changelog current 2026-10-20           |
| Windsurf (Devin Local)     | https://docs.windsurf.com/windsurf/cascade/skills                        | Docs accessed 2026-11-05; no version string                      |
| Cline                      | https://docs.cline.bot/customization/skills.md                           | v4.1.26, 2026-10-26; accessed 2026-11-05                         |
| Aider                      | https://aider.chat/docs/usage/conventions.html                           | v0.86.2 installed 2026-11-05; docs v0.86.0                       |
| OpenHands                  | https://docs.openhands.dev/overview/skills.md                            | v1.35.0, 2026-11-03; accessed 2026-11-05                         |
| Goose                      | https://goose-docs.ai/docs/guides/context-engineering/using-skills.md    | v1.57.0, 2026-10-28; accessed 2026-11-05                         |

## Local smoke tests

Run 2026-11-05.

### Pi Agent 1.5.0

```bash
pi --print --no-session --approve \
  "List the exact names of available skills that contain zj-baseline-cv, zj-job-fit-evaluation, or zj-tailored-application."
```

Result: all three names. `.agents/skills` (symlink to `.skills`) and `.pi/skills`
are discovered. `.skills` alone is not. With `--no-tools`, Pi omits skills from
the prompt, so the test must keep tools enabled.

A second run asked Pi to read `zj-baseline-cv/SKILL.md` and `shared/interaction.md`
and return the first three workflow steps. It read both files and returned the
correct steps: settings and language, source-document intake, and the tagged fact
base.

### OpenAI Codex CLI 0.166.0

```bash
codex exec --skip-git-repo-check -s read-only \
  "Use the zj-baseline-cv skill from .agents/skills. Read .agents/skills/zj-baseline-cv/SKILL.md and .agents/skills/shared/interaction.md. Then list the first three steps you would take and confirm you could read both files. Do not create or modify files."
```

Result: Codex read both files, returned the correct first three steps, and created
or modified no files. `codex debug prompt-input` also advertised all three skills
before the run.

### Aider 0.86.2 fallback

```bash
cd /path/to/zj-skill
python3 scripts/build_bundle.py
aider --read dist/zj-baseline-cv.md --show-prompts --exit
```

Result: the generated bundle appeared in the prompt, the command exited 0, and no
files were changed. Aider has no skill discovery; the bundle is the fallback.
Prompt inspection does not require a chat request, but interactive use needs a
configured model and provider.

The test environment used Aider 0.86.2 installed with Python 3.12. Aider on Python
3.13 failed to start because `audioop` is unavailable.

## Test protocol

1. Install the package into the agent's documented skill location, keeping
   `shared/` and `examples/` beside the skill folders.
2. Start the agent and confirm the skill appears in its skill list or is readable
   from its rules file.
3. Invoke the skill on the fictional example.
4. Confirm the agent reads `SKILL.md`, the shared rule it needs, and one
   reference file.
5. Check that the output contract is met and that missing capabilities are named
   instead of invented.
6. Record the result as tested or documented only, with the exact version.

## Open questions

- Which path should the package recommend first: `.agents/skills/` for broad
  compatibility, or a per-agent install matrix?
- Does Pi discover `.agents/skills/` and `.pi/skills/` with the same precedence
  in the installed release? The smoke test will confirm.
- Do Claude Code and the other untested agents follow `../shared/` links without
  an explicit "read this file" instruction? The current skills already instruct
  the read.
- How does Hermes handle a skill it can modify or delete? Use a read-only copy or
  a fresh install for controlled workflows.
- Should the public package include a root `AGENTS.md` and a `.agents/skills/`
  example, so Tier 2 and multi-agent installs share one entry point?
