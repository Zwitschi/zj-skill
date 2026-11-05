# Lint and leak scan

Release check for the public package. Run after any content change.

Checked 2026-11-05.

## Checks and results

| Check                                                      | Result                                                                                      |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Real personal names, contact details, locations, employers | None found outside `LICENSE` and the scan patterns in this report                           |
| Workspace folder names                                     | None found; covered by the private denylist                                                 |
| Absolute paths                                             | None found; covered by the private denylist                                                 |
| Real employer names                                        | None found; all example employers are invented                                              |
| YAML frontmatter in each `SKILL.md`                        | Valid; `name` matches the folder                                                            |
| Relative links                                             | All resolve                                                                                 |
| Duplicated rule sentences across shared and skill files    | None; the only repeated sentences are intentional consistency inside the fictional examples |
| Personal data in examples                                  | Fictional only: `.test` email domain, `555` phone range, invented people and employers      |

## Exceptions

- `LICENSE` names the copyright holder and links to the holder's profile. This
  is legal attribution, not candidate data, and must stay.
- The examples contain fictional names, addresses, dates, and metrics. They are
  test fixtures, not real data. Do not replace them with real candidate details.

## Commands used

Run from the package root.

```bash
# Candidate, employer, location, workspace-folder, and absolute-path terms are
# kept in a private denylist outside this package. The denylist is not shipped.
grep -rn -i -f <private-denylist.txt> . --exclude=LICENSE
```

A small Python check validates frontmatter and relative links:

```python
import re
from pathlib import Path

root = Path(".")
for skill in root.glob("*/SKILL.md"):
    text = skill.read_text(encoding="utf-8")
    assert text.startswith("---\n"), skill
    frontmatter = text.split("---\n", 2)[1]
    assert re.search(r"^name:\s*" + re.escape(skill.parent.name) + r"$", frontmatter, re.M), skill
    assert re.search(r"^description:\s*\S", frontmatter, re.M), skill

for page in root.rglob("*.md"):
    if "dist" in page.parts:
        continue  # generated bundles; relative links are informational
    for target in re.findall(r"\]\(([^)]+)\)", page.read_text(encoding="utf-8")):
        if target.startswith(("http", "#", "mailto:")):
            continue
        target = target.split("#", 1)[0]
        assert (page.parent / target).exists(), (page, target)
print("frontmatter and links OK")
```

## Documentation lint

Checked 2026-11-05.

- Relative links resolve, excluding generated `dist/`.
- No duplicated rule sentences over 100 characters across docs and skill files.
- Documentation reviewed against `SKILL.md`; the skill and shared files remain
  the source of truth.
- No personal or project data outside `LICENSE`.
- Skill names are `zj-baseline-cv`, `zj-job-fit-evaluation`, and
  `zj-tailored-application`.
- Frontmatter names match the folders.
- Coverage checklist: [`docs/README.md`](docs/README.md#coverage-checklist).

## Not yet covered

- Install test with a specific agent CLI.
- License and publication review.
- A real agent run after installation. The contract walkthrough is in
  `TEST-REPORT.md`.
