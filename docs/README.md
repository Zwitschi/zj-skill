# Documentation

Index for the public package. Start with the root [`README.md`](../README.md)
for the quick start, then choose a path below.

## Reading paths

| Reader            | Path                                                                                                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| New user          | [`README.md`](../README.md) → [`INSTALL.md`](INSTALL.md) → [`WORKFLOWS.md`](WORKFLOWS.md) → [`EXAMPLES.md`](EXAMPLES.md)                            |
| Agent implementer | [`../AGENTS.md`](../AGENTS.md) → the skill's `SKILL.md` → [`../shared/`](../shared/)                                                                |
| Contributor       | [`CONTRIBUTING.md`](CONTRIBUTING.md) → [`architecture.md`](architecture.md) → [`../LINT.md`](../LINT.md) → [`../TEST-REPORT.md`](../TEST-REPORT.md) |
| Publisher         | [`../RELEASE.md`](../RELEASE.md) → [`../CHANGELOG.md`](../CHANGELOG.md) → [`../LICENSE`](../LICENSE)                                                |

## Document set

| Document                                                             | Audience                  | Purpose                                               | Status   |
| -------------------------------------------------------------------- | ------------------------- | ----------------------------------------------------- | -------- |
| [`README.md`](../README.md)                                          | First-time user           | Quick start, skills, install entry point, license     | Existing |
| [`INSTALL.md`](INSTALL.md)                                           | Operator                  | Per-agent paths, copying, fallbacks, verification     | Existing |
| [`COMPATIBILITY.md`](COMPATIBILITY.md)                               | Operator, contributor     | Support tiers, matrix, pinned sources, smoke tests    | Existing |
| [`architecture.md`](architecture.md)                                 | Contributor, agent author | Skill contracts, shared rules, handoff, scope         | Existing |
| [`WORKFLOWS.md`](WORKFLOWS.md)                                       | User                      | End-to-end sequence and handoffs                      | Draft    |
| [`CONFIGURATION.md`](CONFIGURATION.md)                               | User                      | Settings, gates, language, spelling, salary market    | Draft    |
| [`REFERENCE.md`](REFERENCE.md)                                       | User, agent author        | Compact lookup of inputs, outputs, gates, files       | Draft    |
| [`EXAMPLES.md`](EXAMPLES.md)                                         | User, tester              | Fictional example and contract walkthrough            | Draft    |
| [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md)                           | User                      | Symptom, check, fix                                   | Draft    |
| [`FAQ.md`](FAQ.md)                                                   | User                      | Common questions and boundaries                       | Draft    |
| [`PRIVACY.md`](PRIVACY.md)                                           | User, operator            | Data handling and local-only expectations             | Draft    |
| [`CONTRIBUTING.md`](CONTRIBUTING.md)                                 | Contributor               | Edit rules, checks, versioning, license               | Draft    |
| [`../RELEASE.md`](../RELEASE.md)                                     | Maintainer                | Release contents, verification, publication checklist | Existing |
| [`../AGENTS.md`](../AGENTS.md)                                       | Agent                     | Rules-file router and required context                | Existing |
| [`../LINT.md`](../LINT.md), [`../TEST-REPORT.md`](../TEST-REPORT.md) | Maintainer                | Leak scan and contract test record                    | Existing |

## Rules for these docs

- Link to the skill and shared files. Do not duplicate a rule that lives in
  `shared/` or `SKILL.md`.
- Keep every page project-agnostic: no candidate, employer, location, or
  workspace data.
- Use Markdown and ASCII diagrams. Do not rely on Mermaid-only rendering.
- Keep relative links valid and check them before release.
- Mark unfinished pages as drafts. Do not present a draft as release-ready.
- Keep the license and usage boundaries visible from the README and FAQ.

## Coverage checklist

| Area                                              | Covered in                        | Status   |
| ------------------------------------------------- | --------------------------------- | -------- |
| Quick start and package overview                  | `README.md`                       | Complete |
| Per-agent install and fallbacks                   | `INSTALL.md`                      | Complete |
| Compatibility matrix and tiers                    | `COMPATIBILITY.md`                | Complete |
| Skill contracts and scope                         | `architecture.md`                 | Complete |
| End-to-end workflow and handoff                   | `WORKFLOWS.md`                    | Complete |
| Settings, gates, scoring, tags, templates         | `CONFIGURATION.md`                | Complete |
| Per-skill inputs, outputs, gates, stop conditions | `REFERENCE.md`                    | Complete |
| Fictional example and acceptance criteria         | `EXAMPLES.md`                     | Complete |
| Troubleshooting and diagnostic checklist          | `TROUBLESHOOTING.md`              | Complete |
| Common questions and boundaries                   | `FAQ.md`                          | Complete |
| Privacy and local data handling                   | `PRIVACY.md`                      | Complete |
| What this is not, license, responsibilities       | `BOUNDARIES.md`                   | Complete |
| Contribution rules and checks                     | `CONTRIBUTING.md`                 | Complete |
| Terms and glossary                                | `GLOSSARY.md`                     | Complete |
| Release and publication                           | `../RELEASE.md`                   | Complete |
| Agent router and required context                 | `../AGENTS.md`                    | Complete |
| Leak, link, and contract checks                   | `../LINT.md`, `../TEST-REPORT.md` | Complete |

## Documentation lint

Checked 2026-11-05.

| Check                                                 | Result                                                                                 |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Relative links                                        | All resolve; generated `dist/` excluded                                                |
| Duplicated rule sentences across docs and skill files | None over 100 characters                                                               |
| Contradictions with `SKILL.md`                        | Reviewed; `SKILL.md` and `shared/` are the source of truth                             |
| Personal or project data                              | None outside `LICENSE`                                                                 |
| Skill names                                           | `zj-baseline-cv`, `zj-job-fit-evaluation`, `zj-tailored-application` used consistently |
| Frontmatter names                                     | Match the three skill folders                                                          |
| Example links                                         | Point to the renamed example folders                                                   |
| Doc statuses                                          | No draft markers remain                                                                |

## Maintenance rule

A document is complete only when its links resolve, it does not duplicate a rule
from `SKILL.md` or `shared/`, it is consistent with the current skill names, and
the leak scan is clean. Re-run this checklist when a skill or document changes.
