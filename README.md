# Job Application Skills

General, project-agnostic skills for building a baseline CV, evaluating a job
posting, and producing tailored application documents. The skills are designed
for agent CLIs that can read repository instructions and work with files.

**Status: release 0.1.0.** Three skills, the shared rule set, and fictional
worked examples are included. The public architecture and scope are described in
[`docs/architecture.md`](docs/architecture.md).

## Skills

### zj-baseline-cv

Builds or updates one complete master CV, a skills list, and a verification report from all candidate documents. Also converts a task-based history into project-based material.

### zj-job-fit-evaluation

Evaluates one job posting against the documented evidence and returns a fit report, an approved keyword map, and an evidence pack. Does not rewrite documents.

### zj-tailored-application

Produces a tailored CV and cover letter for one posting from the baseline and the approved evaluation, with a change log.

## Workflow

1. **Baseline.** Gather the candidate's documents and build the master CV. The
   baseline is deliberately complete; later steps only select and reorder.
2. **Evaluation.** Read one posting, classify its terms, check the evidence, and
   decide whether to apply.
3. **Tailoring.** Use the approved evaluation and baseline to write the tailored
   CV and cover letter. No new facts.

Each skill can be used alone, but the handoff is designed so evaluation and
tailoring do not drift apart. Cross-skill rules, such as evidence discipline,
question protocol, keyword colours, gates, and output order, live once in
[`shared/`](shared/) and are referenced by the skills.

## Principles

- Generic by default: no candidate, employer, location, or workspace specifics
  in the skills.
- Evidence first: every claim traces to a document or an explicit answer.
- Configured, not hardcoded: language, spelling, salary market, template, and
  output format are settings.
- Human confirmation: the skills ask before trimming, rewriting, or stating a
  gap.
- No invented facts, numbers, dates, or outcomes.

## Install

Copy the `shared/` folder and the skill folder or folders into the same parent
directory used by your agent CLI, keeping them side by side. The skills link to
`../shared/`, so copying a skill alone breaks those references. Copying the whole
package is simplest.

Keep the folder name and `SKILL.md` frontmatter intact. No package manager,
build step, or runtime dependency is planned. Per-agent paths and fallback
instructions are in [`docs/INSTALL.md`](docs/INSTALL.md). See
[`RELEASE.md`](RELEASE.md) for the release checks and publication checklist.

## Documentation

The documentation index is [`docs/README.md`](docs/README.md). It links the
quick start, per-agent install, compatibility matrix, workflows, configuration,
reference, examples, troubleshooting, FAQ, privacy, and contributing guides.

## Fallback entry points

- [`AGENTS.md`](AGENTS.md) routes an agent that reads a rules file to the right
  skill.
- [`docs/INSTALL.md`](docs/INSTALL.md) lists project and user paths for Claude
  Code, Codex, Hermes, Pi, Gemini, Cursor, Windsurf, Cline, OpenHands, Goose, and
  Aider.
- `scripts/build_bundle.py` builds single-file prompt bundles in `dist/` for
  agents without skill discovery. The bundles are generated and not committed.

If an agent cannot read the package, paste the matching bundle into the
conversation. If it cannot write files, ask it to return the documents in the
conversation.

## Repository layout

```text
skills-public/
├── README.md          # this file
├── AGENTS.md          # rules-file router for agents without skill discovery
├── docs/              # architecture, compatibility, install, and scope
├── VERSION            # semantic version
├── CHANGELOG.md       # release history
├── LINT.md            # leak scan and release checks
├── TEST-REPORT.md     # skill contract walkthrough
├── RELEASE.md         # release contents, install, publication checklist
├── LICENSE            # Personal Use License
├── zj-baseline-cv/          # baseline skill and its references
├── zj-job-fit-evaluation/   # evaluation skill and its references
├── zj-tailored-application/ # tailoring skill and its references
├── shared/               # shared rules referenced by all skills
├── examples/             # fictional worked examples
├── scripts/              # bundle builder
└── dist/                 # generated bundles, not committed
```

## Scope

In scope: evidence-based CV building, posting evaluation, and tailored
application documents.

Out of scope: candidate data, job-board scraping, portal integrations,
submission, company research, interview preparation, rendering engines, and
legal or immigration advice. The full list and usage boundaries are in
[`docs/BOUNDARIES.md`](docs/BOUNDARIES.md).

## License

**Personal Use License, all rights reserved.** The skills, workflows, and
prompts may be used only for personal, private, non-commercial purposes. Copying,
modifying, publishing, distributing, sublicensing, selling, or creating
derivative products is not permitted. This is not an open-source license. See
[`LICENSE`](LICENSE) for the full terms.
