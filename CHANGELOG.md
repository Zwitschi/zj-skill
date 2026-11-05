# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
semantic versioning.

## [Unreleased]

### Added

- Compatibility matrix with pinned sources, support tiers, portable conventions,
  and Pi/Codex smoke tests.
- Full public documentation set with index, workflows, configuration, reference,
  examples, troubleshooting, FAQ, privacy, boundaries, glossary, and ASCII
  diagrams.
- `AGENTS.md` router, per-agent `docs/INSTALL.md`, and `scripts/build_bundle.py`
  for agents without skill discovery.
- Capability fallback for missing file tools, questions, network, shell, or
  subagents.

### Changed

- Renamed the three skills to unique `zj-` names.
- Moved the internal design record out of the public package; public contracts
  now live in `docs/architecture.md`.

### Removed

- `DESIGN.md` from the public package.

## [0.1.0] - 2026-11-05

### Added

- Renamed the three skills to unique `zj-` names: `zj-baseline-cv`,
  `zj-job-fit-evaluation`, and `zj-tailored-application`. Folders, frontmatter,
  docs, examples, bundles, and install paths use the new names.
- `zj-baseline-cv` skill: complete baseline CV, skills list, verification report,
  and task-to-project conversion, with detailed phase references.
- `zj-job-fit-evaluation` skill: configurable gates, Green/Red/Yellow keyword
  analysis, match tables, fit and risk assessment, optional salary note, and an
  evidence-pack handoff.
- `zj-tailored-application` skill: contribution paragraph, profile bullets,
  experience integration, impact enhancement, cover letter, and change log.
- Clarified role-level selection versus line-level trimming: selecting or
  condensing a whole role is allowed but must be logged and confirmed; line
  trims require the evaluation's confirmed list.
- Shared reference layer: evidence discipline, interaction and question
  protocol, keyword colours, gates, output order and handoff, and style rules.
- Fictional worked examples for all three skills, using an invented candidate
  and posting, with expected outputs.
- `LINT.md` release check: leak scan, absolute-path scan, workspace-name scan,
  frontmatter validation, link validation, and duplicate-rule review.
- `TEST-REPORT.md`: contract walkthrough for all three skills, cross-skill
  consistency checks, and recorded fixes.
- `RELEASE.md`: release contents, install steps, verification, and publication
  checklist.
- `docs/architecture.md`: public skill contracts, shared rules, handoff contract,
  scope, out-of-scope list, and support model.
- Documentation index `docs/README.md` and guides for workflows,
  configuration, reference, examples, troubleshooting, FAQ, privacy, and
  contributing.
- `docs/REFERENCE.md` with per-skill purpose, inputs, settings, workflow,
  outputs, gates, stop conditions, handoff, and example links.
- `docs/GLOSSARY.md` and ASCII component, handoff, and decision diagrams in
  `docs/architecture.md`.
- `docs/CONFIGURATION.md` with the full setting reference, gate definitions,
  scoring rules, evidence tags, template and output settings, validation, and an
  illustrative setup block.
- `docs/BOUNDARIES.md` with what the package is not, the Personal Use License,
  usage boundaries, and role responsibilities.
- `docs/TROUBLESHOOTING.md` with discovery, file, input, workflow, and output
  symptoms and fixes, including missing tools, no network, long context, stale
  evaluation, missing baseline, missing trim list, and unsupported frontmatter.
- Documentation lint and coverage checklist; all public guides marked complete.
- `docs/COMPATIBILITY.md`: compatibility dimensions, support tiers, portable
  conventions, a filled agent matrix with pinned sources and versions, common
  findings, and a test protocol.
- Personal Use License in `LICENSE`: personal, private, non-commercial use only;
  no redistribution or derivative works.
- Capability fallback for agents without file read/write, interactive questions,
  network, shell, or subagents. Documented in `shared/interaction.md` and linked
  from each skill.
- `AGENTS.md` router for rules-file agents.
- `docs/INSTALL.md` with per-agent project and user paths and fallback steps.
- `scripts/build_bundle.py` to build single-file prompt bundles in `dist/` for
  agents without skill discovery.
- Local smoke tests: Pi discovers `.agents/skills` and `.pi/skills` but not
  `.skills`; Codex discovers `.agents/skills` and completes a read-only skill run,
  reading `SKILL.md` and `shared/interaction.md` without modifying files.
