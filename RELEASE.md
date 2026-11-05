# Release 0.1.0

Prepared 2026-11-05.

## Pre-flight status

| Item                             | Status                           | Evidence                                                                                               |
| -------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Rights holder sign-off           | **Pending, publication blocker** | Package is derived from prompt material; the rights holder must confirm publication and use terms      |
| License                          | Pass                             | Personal Use License in `LICENSE`                                                                      |
| `DESIGN.md` removed from package | Pass                             | Internal record in `.github/instructions/SKILLS-DESIGN.md`; public contracts in `docs/architecture.md` |
| Compatibility research           | Pass                             | `docs/COMPATIBILITY.md`; Pi and Codex tested, others documented-only                                   |
| Public documentation             | Pass                             | All guides complete; `docs/README.md` and `LINT.md`                                                    |
| Leak scan                        | Pass                             | No personal or project data outside `LICENSE`                                                          |
| Frontmatter and links            | Pass                             | Names match folders; relative links resolve                                                            |
| Example contract test            | Pass                             | `TEST-REPORT.md` and regenerated examples                                                              |
| Bundle builder                   | Pass                             | `scripts/build_bundle.py`; `dist/` ignored                                                             |
| Version                          | Pending                          | Currently `0.1.0`; planned `0.2.0` bump                                                                |
| Repository                       | Pass                             | Clean local repo, tag `v0.1.0`, no remote                                                              |
| Publication                      | Not started                      | No push, no remote                                                                                     |

Do not publish until the rights holder confirms the source-prompt rights and the
Personal Use License terms.

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

The package is a standalone local repository:

- branch `main`, one commit, annotated tag `v0.1.0`;
- neutral commit identity, so the history does not expose a personal email
  address;
- no remote configured;
- no private denylist, local cache, or editor file committed.

To recreate the repository from the files:

```bash
rm -rf .git
git init -b main
git config user.name "Release Preparation"
git config user.email "release@example.test"
git add .
git commit -m "Release v0.1.0"
git tag -a v0.1.0 -m "Release v0.1.0"
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
4. Add the remote, push `main`, then push the tag `v0.1.0`.
5. Inspect the public history for personal data, including the commit author and
   committer fields.
6. Confirm that `LICENSE` is the only file naming the copyright holder.
7. Do not upload the private denylist or any local test output.

## Known limitations

- The examples are a contract walkthrough, not an independent agent run.
- Install has not been tested against a specific agent CLI.
- No automated test suite exists yet; the checks are documented and manual.
- The license restricts use and redistribution. Do not describe the package as
  open source.
