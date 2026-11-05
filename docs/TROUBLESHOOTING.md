# Troubleshooting

Status: complete. Find the symptom, run the check, apply the fix. Use the
fictional example for a clean reproduction before testing with real documents.

## Quick table

| Symptom                                   | Likely cause                                        | Fix                                                                                    |
| ----------------------------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Skill not listed                          | Wrong path, missing siblings, project not trusted   | Recheck the install path; copy `shared/` and `examples/`; restart; approve the project |
| Skill listed in one agent but not another | Different discovery paths                           | Use `.agents/skills/` as the shared project path                                       |
| Pi does not see the skill                 | `.skills/` is not a Pi path, or `--no-tools` is set | Use `.agents/skills/` or `.pi/skills/`; keep tools enabled                             |
| Codex does not see the skill              | Not logged in, or wrong path                        | `codex login`; `codex debug prompt-input`; use `.agents/skills/`                       |
| Relative link fails                       | `shared/` or `examples/` is missing                 | Keep all folders side by side                                                          |
| No file tools                             | Agent is chat-only                                  | Paste `SKILL.md`, the shared rule, and the documents                                   |
| No write tools                            | Agent cannot create files                           | Return Markdown in the conversation; mark it as a draft                                |
| No network                                | Sandbox or offline mode                             | The package does not require network; paste the posting                                |
| Context too long                          | Whole package pasted, or too many references        | Read one skill and only the needed shared files                                        |
| Stale evaluation                          | Posting changed after evaluation                    | Re-run `zj-job-fit-evaluation`                                                            |
| Missing baseline                          | Baseline was skipped                                | Run `zj-baseline-cv`, or use an evidence profile and say so                               |
| Missing trim list                         | No confirmed line trims                             | Do not remove lines; role selection is separate and must be confirmed                  |
| Unsupported frontmatter                   | Agent-specific field or bad YAML                    | Keep `name` and `description`; remove extensions; fix YAML                             |

## Skill discovery

### Skill is not listed

Check:

- the path against [`INSTALL.md`](INSTALL.md);
- that `zj-baseline-cv/`, `zj-job-fit-evaluation/`, `zj-tailored-application/`,
  `shared/`, and `examples/` are siblings;
- that the project is trusted or approved;
- that the agent was restarted after copying.

Fix: copy the whole package into the agent's skill directory, restart, and list
skills again.

### The skill appears in one agent but not another

Agents use different paths. `.agents/skills/` is the broadest project path;
`.claude/skills/` is the Claude-compatible path. Use `.agents/skills/` and, where
needed, a symlink to the same folder. See [`COMPATIBILITY.md`](COMPATIBILITY.md).

### Pi does not see the skill

- `.skills/` is not a Pi discovery path. Use `.agents/skills/` or `.pi/skills/`.
- `--no-tools` hides skills from the prompt. Keep tools enabled.
- Project-local skills require trust; approve the project for the run.

### Codex does not see the skill

- Run `codex login` and confirm the status.
- Run `codex debug prompt-input` and search for the skill names.
- Use `.agents/skills/` at the working directory, a parent, or the repository
  root.

### Frontmatter warning or rejected skill

- `name` must be lowercase words separated by hyphens and should match the
  folder.
- `description` must be present and explain when to use the skill.
- Unknown or experimental fields may warn or be ignored. Remove
  agent-specific fields from the portable copy.
- YAML must start on the first line and be valid.

## Files and links

### `shared/` or `examples/` is missing

The skills link to `../shared/` and `../examples/`. Copy the whole package, not a
single skill folder.

### Relative links do not resolve

- Keep the folder structure intact.
- Tell the agent to read the linked file explicitly; do not rely on automatic
  link following.
- For a single-file fallback, use the generated bundle.

### No file tools

Ask the user to paste `SKILL.md`, the shared rule, and the source documents. Use
the bundle builder for a single prompt file. Do not pretend to read a file.

### No write tools

Return the document in the conversation as Markdown and mark it as a draft. Keep
the change log and open items in the same response.

### Permission denied

Install into a user-writable path such as `.agents/skills/` or
`~/.agents/skills/`. Do not require sudo for a user-level skill.

## Inputs

### No network

The package does not require network access. Skip any optional web step and ask
for the posting or source material as text. Do not invent fetched content.

### Missing baseline

Run `zj-baseline-cv`, or use an equivalent evidence profile and state that the
baseline is unavailable. Evaluation can proceed from an evidence profile;
tailoring still needs an approved evidence pack.

### Missing posting

Stop and ask for the posting. Do not evaluate from a title, a snippet, or a
guess.

### Unreadable documents

Name the exact file and part, stop, and ask for a better copy. Do not build
around an unreadable page or guess its content.

### Context is too long

- Read `SKILL.md` first, then only the shared files and reference the task needs.
- Do not paste the whole package or all examples.
- Run one skill at a time: baseline, evaluation, then tailoring.

### Unsupported frontmatter

Keep the portable pair `name` and `description`. Remove fields such as
`allowed-tools`, `disable-model-invocation`, `paths`, or `triggers` when the
target agent does not support them. Unknown fields may be ignored or may warn.

## Workflow

### Stale evaluation

Re-run `zj-job-fit-evaluation` when the posting changes materially or the evidence
pack is for another posting. Tailoring must stop.

### Missing trim list

Do not remove individual lines. Role-level selection is allowed but must be
logged and confirmed. Ask for a trim review if line-level removals are needed.

### Missing evidence pack or keyword map

Run evaluation first. Tailoring must not create its own evidence set.

### Role selection is not confirmed

Record the selection in the change log and list it as an open item. Do not
present the draft as final.

### Skill does not trigger

- Make the description specific about what the skill does and when to use it.
- Invoke it explicitly with the agent's skill command or by naming the skill.
- Check that the skill is enabled and not hidden by `--no-tools`, a denylist, or
  a disabled setting.

### Agent modifies installed skills

Hermes can modify or delete skills. Use a read-only copy or a fresh install.
Reinstall from the source package after an unintended change.

### Aider or another rules-file agent

Use a generated bundle or a `CONVENTIONS.md` pointer to `AGENTS.md`. Aider has no
skill discovery.

## Output

### Wrong format or path

State the output format and path as settings. Use a project overlay for local
paths. Skill bodies must not contain absolute paths.

### Empty or partial posting

Do not infer the missing parts. Ask for the full text or mark the evaluation as
partial with the missing sections named.

### Unresolved conflict

Keep both versions, flag the difference, and list it as an open item. Do not
average dates or silently pick one.

### No questions possible

State assumptions and open items. Do not infer agreement from silence.

### Submission or external write

The package never submits, emails, or publishes. Do that manually after review.

## Diagnostic checklist

1. Agent and version.
2. Skill path and trust status.
3. Presence of `shared/` and `examples/`.
4. Frontmatter name and description.
5. File read and write capability.
6. Network, shell, and subagent availability.
7. Current posting and evaluation date.
8. Confirmed trim list and role selection.
9. Output format and path.
10. Personal data kept local.
