# Shared rules

Operational rules used by all three skills. A skill must link to the files it
needs and tell the agent to read them before starting. Do not copy these rules
into `SKILL.md` bodies; edit them here once so the skills cannot drift apart.

| File                               | Covers                                                                                | Used by               |
| ---------------------------------- | ------------------------------------------------------------------------------------- | --------------------- |
| [`evidence.md`](evidence.md)       | No-invention rule, source tags, confidence, conflicts, gaps, open items, skill levels | All                   |
| [`interaction.md`](interaction.md) | Language, spelling, question protocol, impact capture, gap analysis, confirmations    | All                   |
| [`keywords.md`](keywords.md)       | Green/Red/Yellow classification, verifiability, placement, match tables               | Evaluation, tailoring |
| [`gates.md`](gates.md)             | Preconditions, stop conditions, human confirmation gates, final checks                | All                   |
| [`output.md`](output.md)           | Output order, document order, working-draft status, change log, handoff contract      | All                   |
| [`style.md`](style.md)             | CV, contribution, profile, cover-letter, date, punctuation, and spelling style        | Baseline, tailoring   |

## How a skill references this folder

Each `SKILL.md` should include a short section like:

```text
Before starting, read:
- ../shared/evidence.md
- ../shared/interaction.md
- ../shared/gates.md
- ../shared/output.md
Add ../shared/keywords.md for evaluation and tailoring.
Add ../shared/style.md for baseline and tailoring.
```

Relative paths are resolved from the skill folder.

## Configuration

These values are set by the user or by a local overlay, never hardcoded in the
shared files:

- output language, or bilingual output;
- spelling convention;
- salary market and currency, when salary guidance is requested;
- CV template and layout;
- source-tag vocabulary, if the user has one;
- target role types for ordering and headline options;
- any location, eligibility, or language gates supplied by the user.

## Precedence

1. Explicit user instructions for the current task.
2. The skill's own `SKILL.md` workflow.
3. These shared rules.
4. Local project overlays that only supply configuration or paths.

A local overlay may configure settings. It must not weaken the evidence rules,
the confirmation gates, or the no-invention rule.

## Maintenance

- Change a shared rule here, not in a skill body.
- Keep examples fictional and generic.
- Do not add candidate data, employer names, locations, workspace paths, or
  tool-specific infrastructure to this folder.
