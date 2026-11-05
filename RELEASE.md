# Release 0.2.0

Prepared 2026-11-05.

## Pre-flight status

| Item                             | Status      | Evidence                                                                                    |
| -------------------------------- | ----------- | ------------------------------------------------------------------------------------------- |
| Rights holder sign-off           | Pass        | Confirmed 2026-11-05; internal planning documents are excluded from publication             |
| License                          | Pass        | Personal Use License in `LICENSE`                                                           |
| `DESIGN.md` removed from package | Pass        | Internal record kept outside the public package; public contracts in `docs/architecture.md` |
| Compatibility research           | Pass        | `docs/COMPATIBILITY.md`; Pi and Codex tested, others documented-only                        |
| Public documentation             | Pass        | All guides complete; `docs/README.md` and `LINT.md`                                         |
| Leak scan                        | Pass        | No personal or project data outside `LICENSE`                                               |
| Frontmatter and links            | Pass        | Names match folders; relative links resolve                                                 |
| Example contract test            | Pass        | `TEST-REPORT.md` and regenerated examples                                                   |
| Bundle builder                   | Pass        | `scripts/build_bundle.py`; `dist/` ignored                                                  |
| Version                          | Pass        | `0.2.0` in `VERSION`; tag `v0.2.0`                                                          |
| Repository                       | Pass        | Clean local repo, tags `v0.1.0` and `v0.2.0`, no remote                                     |
| Publication                      | Not started | No push, no remote                                                                          |

The rights holder confirmed publication on 2026-11-05. Internal planning
documents are not part of the public repository.

## Repository metadata

- Description: "General job-application skills for AI agent CLIs"
- Homepage: https://github.com/Zwitschi/zj-skill/blob/main/docs/README.md
- Topics: `agent-skills`, `ai-agents`, `career`, `claude-code`, `codex`, `cv`,
  `hermes`, `job-application`, `job-search`, `pi-agent`, `prompt-engineering`,
  `resume`
- License display: GitHub reports `Other`/`NOASSERTION` because the license is a
  custom Personal Use License, not an SPDX-listed license.
- Install and usage links: `README.md` links `docs/INSTALL.md`,
  `docs/WORKFLOWS.md`, `docs/COMPATIBILITY.md`, `docs/REFERENCE.md`, and
  `docs/EXAMPLES.md`.

## Contents

- Three skills: `zj-baseline-cv`, `zj-job-fit-evaluation`, `zj-tailored-application`.
- Shared rules in `shared/`.
- Fictional examples in `examples/`.
- Release checks in `LINT.md` and `TEST-REPORT.md`.
- Architecture and scope in `docs/architecture.md`.
- Compatibility matrix and support tiers in `docs/COMPATIBILITY.md`.
- Documentation index in `docs/README.md`.
- Installation paths and fallbacks in `docs/INSTALL.md`.
- Rules-file router in `AGENTS.md` and a bundle builder in `scripts/build_bundle.py`.
- Version in `VERSION`.
- License in `LICENSE`.

## Install

1. Copy the whole package, or copy `shared/` and the skill folders side by side
   into the skills directory used by the agent CLI.
2. Keep the folder names and `SKILL.md` frontmatter intact. The skills link to
   `../shared/`, so a skill folder without its sibling `shared/` will have
   broken references.
3. No package manager, build step, or runtime dependency is required.

## Verify

From the package root:

```bash
# 1. Frontmatter and relative links
python3 - <<'PY'
import re
from pathlib import Path

for skill in Path(".").glob("*/SKILL.md"):
    text = skill.read_text(encoding="utf-8")
    assert text.startswith("---\n"), skill
    frontmatter = text.split("---\n", 2)[1]
    assert re.search(r"^name:\s*" + re.escape(skill.parent.name) + r"$", frontmatter, re.M), skill
    assert re.search(r"^description:\s*\S", frontmatter, re.M), skill

for page in Path(".").rglob("*.md"):
    if "dist" in page.parts:
        continue
    for target in re.findall(r"\]\(([^)]+)\)", page.read_text(encoding="utf-8")):
        if target.startswith(("http", "#", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        assert (page.parent / target).exists(), (page, target)
print("frontmatter and links OK")
PY

# 2. Leak scan with a private denylist kept outside the package
grep -rn -i -f <private-denylist.txt> . --exclude=LICENSE
```

The private denylist must never be committed. It contains candidate, employer,
location, workspace-folder, and absolute-path terms.

## Repository state

The package is published at https://github.com/Zwitschi/zj-skill.

- branch `main`, two commits, annotated tags `v0.1.0` and `v0.2.0`;
- neutral commit identity, so the history does not expose a personal email
  address;
- remote `origin` points to the public repository;
- no private denylist, local cache, or editor file committed;
- no internal planning documents committed.

Internal planning documents, personal workspace files, generated bundles, local
caches, and the private denylist stay outside this repository. Do not add them to
the public repository.

To recreate the repository from the files:

```bash
rm -rf .git
git init -b main
git config user.name "Release Preparation"
git config user.email "release@example.test"
git add .
git commit -m "Release v0.2.0"
git tag -a v0.2.0 -m "Release v0.2.0"
```

Before committing, re-run the checks above. Do not commit the private denylist,
local caches, or editor files.

## Publication checklist

Publication is the rights holder's action, not part of the preparation.

1. Confirm the license terms in `LICENSE` and that the rights holder is
   authorised to publish the derived prompt material.
2. Confirm that the package is intended to be source-available under the
   Personal Use License, not open source.
3. Create an empty repository with the intended visibility.
4. Add the remote, push `main`, then push the tag `v0.2.0`.
5. Inspect the public history for personal data, including the commit author and
   committer fields.
6. Confirm that `LICENSE` is the only file naming the copyright holder.
7. Do not upload the private denylist or any local test output.

## Known limitations

- The examples are a contract walkthrough, not a full independent run of every
  workflow.
- Install is tested with Pi 1.5.0 and Codex CLI 0.166.0. Aider 0.86.2 prompt
  fallback loading is tested. Other agents are documented-only.
- Lightweight CI runs the public checks on every push and pull request. It does
  not run live agent tests.
- The license restricts use and redistribution. Do not describe the package as
  open source.
