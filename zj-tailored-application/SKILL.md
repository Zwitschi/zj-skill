---
name: zj-tailored-application
description: Create a tailored CV and cover letter for one specific job posting from an approved fit evaluation and a baseline CV. Use when the user asks to tailor or adapt a CV to a job, write a cover letter, or prepare application documents for a role. Requires an approved evidence pack and keyword map; use zj-job-fit-evaluation first when they are missing. Not for building a baseline CV or deciding whether to apply.
---

# Tailored application

Turn an approved evaluation and a baseline CV into a tailored CV and cover
letter for one posting. Use the evaluation's evidence pack and keyword map as the
only source of facts and keyword decisions. Do not re-evaluate and do not invent
new claims.

## Read before starting

Read these shared rules first:

- [`../shared/evidence.md`](../shared/evidence.md)
- [`../shared/interaction.md`](../shared/interaction.md)
- [`../shared/keywords.md`](../shared/keywords.md)
- [`../shared/gates.md`](../shared/gates.md)
- [`../shared/output.md`](../shared/output.md)
- [`../shared/style.md`](../shared/style.md)

Detailed steps are in
[`references/tailoring-workflow.md`](references/tailoring-workflow.md). Document
patterns are in
[`references/document-patterns.md`](references/document-patterns.md).

A fictional worked example, including the expected CV and cover letter, is in
[`../examples/zj-tailored-application/expected-output.md`](../examples/zj-tailored-application/expected-output.md).

If file reading is unavailable, ask the user to paste the referenced files. If
file writing is unavailable, return the CV, cover letter, change log, and open
items in the conversation as Markdown.

## What this skill does not do

- It does not build or update the baseline.
- It does not evaluate the posting or invent a score.
- It does not add facts outside the approved evidence pack.
- It does not submit, email, or publish anything.
- It does not add documents or steps beyond the tailored CV, the cover letter, the change log, and the open items.

## Preconditions

Stop and ask for the missing piece when any of these is absent:

1. A baseline CV.
2. An approved evidence pack for this posting.
3. An approved keyword map for this posting.
4. The posting text.
5. The target output language or languages.

If the evidence pack is for a different posting, or the posting has changed
materially since the evaluation, stop and request a new evaluation.

## Inputs

Required:

- baseline CV;
- approved evidence pack;
- approved keyword map;
- posting text.

Optional:

- confirmed trim list from the evaluation;
- template or layout settings;
- existing cover-letter examples for tone only, never for facts;
- a configured salary paragraph for the cover letter, only if the evaluation
  produced one.

Settings, supplied as placeholders:

| Placeholder               | Meaning                                                              |
| ------------------------- | -------------------------------------------------------------------- |
| `<working-language>`      | Language used during the conversation                                |
| `<output-language>`       | Language of the tailored CV                                          |
| `<cover-letter-language>` | Language of the cover letter; may differ from the CV                 |
| `<spelling-convention>`   | Spelling setting                                                     |
| `<cv-template>`           | Template or layout                                                   |
| `<document-order>`        | CV, cover letter, change log order if the user wants a different one |

## Workflow

1. **Preflight.** Confirm the baseline, evidence pack, keyword map, and posting.
   Confirm languages and settings.
2. **Select and trim.** Choose which baseline roles and sections support the
   posting. Role-level selection, including condensing or omitting entire roles,
   is part of tailoring: log it and get the candidate's confirmation before
   finalising. Line-level trimming inside an included role needs the confirmed
   trim list from the evaluation. Do not remove individual lines without it.
3. **Contribution.** Write the first-person prose paragraph, about six lines:
   who I am, what I do, how, and what results I achieve. Use approved evidence.
4. **Profile.** Write three to six compressed positioning bullets. Green terms
   first, no results or value claims.
5. **Experience.** Keep every official job title unchanged. Adapt at most one
   bullet per role, only where a genuine overlap exists. Quantify only with
   approved figures.
6. **Impact enhancement.** Present flagged bullets one at a time with a diagnosis
   and a suggested rewrite or a clarifying question. The candidate confirms,
   adjusts, or skips.
7. **Cover letter.** Write the role-specific narrative: why this role, the
   underlying motivation, and how the development leads there. Yellow terms
   carry the letter; Green and Red support.
8. **Check and log.** Verify every claim against the evidence pack, check the
   keyword map, and write the change log plus open items.

## Document rules

### Contribution

- First person, prose, no bullets.
- About six lines.
- Opens with a variation of "with X years of experience in ...".
- Covers who I am, what I do, how I do it, and what results I achieve.
- Uses two or three of the strongest approved results.
- Does not repeat the profile or list education.

### Profile

- Three to six bullets.
- Compressed positioning statements.
- Education, role identity, years, and named Green technologies.
- No results, achievements, or value claims.

### Experience

- Reverse chronological, consistent with the baseline.
- Official titles unchanged.
- One adapted bullet per role at most.
- No forced overlap.
- No seniority inflation.
- Approved figures only.

### Impact enhancement

- One bullet at a time.
- Diagnose: task-only, partial outcome, or strong outcome.
- Offer a rewrite only when the outcome is already supported by the evidence.
- Otherwise ask one short question.
- Leave strong bullets untouched.
- Never invent a number or outcome.

### Cover letter

- Explains why this specific role fits the career path.
- Explains the underlying motivation.
- Shows how the professional development leads to the role.
- Uses Yellow terms deliberately and authentically.
- Uses Green and Red terms sparingly, in support.
- No filler phrases, generic company praise, or clichés.
- Does not repeat the CV.
- Does not claim a connection to the employer that is not evidenced.

## Selection and trimming

Role-level selection:

- Choosing which roles and sections to include is part of tailoring.
- Condensing or omitting an entire role is role-level selection, not a line
  trim.
- Log every selection decision and ask the candidate to confirm it before
  finalising.
- Do not omit a role silently.

Line-level trimming:

- Apply only the trim decisions confirmed in the evaluation.
- Do not trim additional lines because they seem less relevant.
- If no trim list exists, leave the included roles intact and note that
  line-level trimming was not requested.
- Never remove a line that carries a unique differentiator or continuity signal
  without explicit confirmation.

## Output contract

| Artifact     | Required contents                                                                                |
| ------------ | ------------------------------------------------------------------------------------------------ |
| Tailored CV  | Contribution, profile, experience integration, impact-enhanced bullets, consistent section order |
| Cover letter | Role-specific motivation and narrative, no invented facts                                        |
| Change log   | Section and line, before and after, reason, evidence, confirmation status                        |
| Open items   | Anything the candidate must confirm before submission                                            |

Every document is a working draft until the candidate approves it. Do not
overwrite the baseline or the evaluation artefacts.

## Change log

For every edit record:

- section and line or bullet;
- before and after;
- reason: keyword match, impact enhancement, clarity, role selection, trim, or
  target-role integration;
- evidence or source tag supporting the change;
- confirmation status.

## Handoff

This skill consumes the evidence pack and keyword map defined in
[`../shared/output.md`](../shared/output.md). It must not create a second
evidence set. If a new claim is needed, stop, ask the candidate, and update the
pack before using it.

The evaluation's trim list is the only approved source of line-level removals.
Role-level selection is allowed, but it is not a trim: log it and confirm it with
the candidate. The converter's `[QUANTIFIED]` markers are authoritative for
already-quantified bullets; do not ask again for those figures.

## Quality checklist

- Preconditions were met before writing.
- Every claim traces to the evidence pack.
- Official job titles are unchanged.
- At most one adapted bullet per role.
- No invented numbers, tools, or outcomes.
- Only confirmed line trims were applied, and every role-level selection is
  logged and confirmed.
- Green terms are used only where verifiable.
- The cover letter uses Yellow terms as the narrative and Green/Red in support.
- The change log explains every edit.
- Open items are listed.
- No submission happened.

## Stop conditions

Stop and ask when:

- the baseline, evidence pack, keyword map, or posting is missing;
- the evidence pack is stale or for another posting;
- the candidate asks for a claim that is not in the pack;
- a bullet needs an outcome that was never captured;
- the candidate asks to trim beyond the confirmed line list;
- an entire role would be omitted or condensed without confirmation;
- the request would change an official job title or inflate seniority.
