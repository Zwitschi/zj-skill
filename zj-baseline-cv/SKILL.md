---
name: zj-baseline-cv
description: Build or update a complete baseline CV, skills list, and verification report from a candidate's source documents. Also converts a task-based CV into project-based material. Use when the user asks for a baseline CV, master CV, complete CV from documents, CV update, skills list, verification report, task-to-project CV, or project list. Not for evaluating a job posting or tailoring documents to one role; use zj-job-fit-evaluation or zj-tailored-application for that.
---

# Baseline CV

Build one complete, evidence-tagged baseline CV, a skills list, and a
verification report from all of a candidate's documents. The baseline is
deliberately long: later work selects and reorders from it, so no documented
fact may be lost and no undocumented fact may be added.

The skill also converts a task-based CV into project-based material for
contracting or freelance use.

## Read before starting

Read these shared rules first. They are part of the skill, not optional
background:

- [`../shared/evidence.md`](../shared/evidence.md)
- [`../shared/interaction.md`](../shared/interaction.md)
- [`../shared/gates.md`](../shared/gates.md)
- [`../shared/output.md`](../shared/output.md)
- [`../shared/style.md`](../shared/style.md)

Detailed phase instructions are in:

- [`references/baseline-phases.md`](references/baseline-phases.md)
- [`references/project-conversion.md`](references/project-conversion.md)

A fictional worked example, including source documents and the expected
baseline, is in
[`../examples/zj-baseline-cv/expected-output.md`](../examples/zj-baseline-cv/expected-output.md).

If file reading is unavailable, ask the user to paste the referenced files. If
file writing is unavailable, return the baseline, skills list, verification
report, and project variant in the conversation as Markdown.

## What this skill does not do

- It does not evaluate a posting.
- It does not write a cover letter.
- It does not tailor the CV to one role beyond ordering and headline options.
- It does not submit, email, or publish anything.
- It does not invent missing facts to fill gaps.

## Inputs

Ask for everything in one message, then wait.

Required:

- all CV versions the candidate has written, including older versions;
- reference letters, interim references, and employment confirmations;
- diplomas, transcripts, and course or certification certificates.

Optional:

- an existing skills list or matrix;
- cover letters, a profile export, portfolio or repository links;
- an existing project list or project notes.

Settings, supplied as placeholders:

| Placeholder             | Meaning                                                             |
| ----------------------- | ------------------------------------------------------------------- |
| `<working-language>`    | Language used during the conversation                               |
| `<output-language>`     | Language of the baseline documents                                  |
| `<spelling-convention>` | Spelling setting for the output language                            |
| `<cv-template>`         | Template file or layout description; use a clean fallback if absent |
| `<target-roles>`        | One to three role types, for ordering and headline options only     |
| `<evidence-tags>`       | Optional existing tag vocabulary; otherwise use the shared defaults |

Do not assume a country, market, spelling, or language. Ask.

## Workflow

Follow the phases in order. Do not build the CV before the fact base and
conflict review are complete.

1. **Settings and intake.** Confirm working language, output language, spelling,
   template, and target roles. Request the documents. See
   [`references/baseline-phases.md`](references/baseline-phases.md).
2. **Inventory and readability.** List every document with type, date or
   version, and readability. Stop on any unreadable page or file and name the
   exact file and part.
3. **Fact base.** Extract every role and fact before writing CV text: employer,
   location, all titles, dates, responsibilities, achievements with exact
   numbers, technologies, and sources. Tag every item.
4. **Conflicts and questions.** Check for conflicting dates, titles, duplicates,
   single-source claims, timeline gaps, overlapping roles, and unclear role
   types. Ask all open questions in one numbered message, at most ten. Keep
   unanswered items as open items.
5. **Skills list.** Reconcile an existing list or build one, grouped by
   category, with a conservative level and evidence.
6. **Baseline build.** Use the template and the fixed section order below. Keep
   completeness first.
7. **Verification report.** List documents used, unreadable parts, conflicts and
   resolutions, single-source claims, open items, and the baseline-only rule.
8. **Optional project conversion.** If requested, convert a task-based history
   into project-based material role by role, with confirmation between roles.
   See [`references/project-conversion.md`](references/project-conversion.md).

## Baseline section order

Use this order unless the supplied template clearly requires another:

1. Personal data.
2. Value proposition:
   - contribution paragraph, first person, prose;
   - profile bullets, three to six in a tailored CV, eight to twelve in the
     baseline.
3. Business experience, reverse chronological, one flat bullet list per role.
4. Professional development, only if documented; otherwise omit and record an
   open item.
5. Education.
6. Languages with a common reference level or "mother tongue".
7. Hobbies, only if provided; otherwise a placeholder note.
8. References, normally "upon request".

After a page break, add a clearly labelled selection pool:

- headline options;
- additional personal data such as availability and work mode;
- the full skills list as a keyword source;
- technologies used per role;
- one-line company descriptions;
- projects, awards, community work, and talks;
- quoted strengths from reference letters, attributed to the employer;
- relevant courses;
- reference signatories and open contact details.

The selection pool is baseline-only material. It is not part of the final CV.

## Project conversion contract

Use the converter only when the candidate's CV is task-based and the candidate
wants project-based material.

- Confirm the CV is task-based. If it is already project-based, say so and stop.
- Process one role at a time, chronologically.
- State the number of roles before starting.
- For each role, interview the candidate about each project using the fields in
  [`references/project-conversion.md`](references/project-conversion.md).
- Ask one field at a time, allow skips, and wait for explicit completion before
  the next role.
- Mark unconfirmed fields as `[TO CONFIRM]`.
- Mark already quantified bullets with `[QUANTIFIED]` for handoff.
- Produce a CV short version of three to five impact-led bullets per role and a
  standalone project list using the exact field structure.

## Output contract

| Artifact                  | Required contents                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| Baseline CV               | All sections above, evidence tags, selection pool                                                     |
| Skills list               | Category, skill, level, evidence, candidate-only marker                                               |
| Verification report       | Documents used, unreadable parts, conflicts, single-source claims, open items, baseline-only reminder |
| Project variant, optional | CV short versions and project list, unconfirmed fields marked                                         |
| Open items                | Short list of everything the candidate must confirm or supply                                         |

Every generated document is a working draft until the candidate approves it.
Do not overwrite source documents. Do not edit the baseline during tailoring.

## Updating an existing baseline

When a baseline already exists:

1. Inventory the new or changed documents.
2. Extract only the new facts and changes.
3. Merge into the existing fact base without dropping single-source facts.
4. Re-run the conflict check.
5. Show a short diff summary: new roles, changed dates, new certificates, new
   skills, removed claims, open items.
6. Ask before rewriting sections that the candidate has already approved.
7. Re-run the verification report and record the new version.

Never silently replace a previous baseline. Keep the old version available.

## Quality checklist

Before presenting the result:

- every required document is inventoried;
- every fact carries a source tag;
- conflicts are resolved or listed;
- single-source claims are listed for interview preparation;
- every skill level has evidence;
- the section order is complete;
- open items are visible;
- the verification report exists;
- no fact, number, date, title, or outcome was invented;
- the selection pool is clearly separated from the CV;
- the draft is labelled as a draft.

## Stop conditions

Stop and ask when:

- a required document group is missing and the candidate has not accepted a
  partial set;
- any page or file is unreadable;
- a conflict cannot be resolved without the candidate;
- a fact has no source but is needed for a section;
- the candidate asks to add a claim that cannot be evidenced.

Do not continue with a silent assumption.
