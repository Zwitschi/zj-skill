# Reference

Compact reference for the three skills. Binding detail is in each `SKILL.md` and
in `shared/`; this page is the map.

## zj-baseline-cv

**Purpose:** build or update one complete baseline CV, a skills list, and a
verification report from all candidate documents. It also converts a task-based
history into project-based material.

**Use when:** no baseline exists, new documents arrive, conflicts need
resolution, or a contracting project list is needed.

**Do not use for:** posting evaluation or job-specific tailoring.

### Inputs

| Input                                          | Required | Notes                                       |
| ---------------------------------------------- | -------- | ------------------------------------------- |
| All CV versions                                | Yes      | Older versions often contain dropped detail |
| Reference letters and employment confirmations | Yes      | Third-party evidence                        |
| Diplomas, transcripts, certificates            | Yes      | Credential evidence                         |
| Existing skills list                           | No       | Reconciled with the fact base               |
| Project list or project notes                  | No       | Used for project conversion                 |
| Template or layout description                 | Setting  | Clean fallback if absent                    |
| Working and output language                    | Setting  | Asked before output                         |
| Spelling convention                            | Setting  | Never hardcoded                             |
| Target roles                                   | Setting  | Ordering and headlines only                 |
| Evidence tags                                  | Setting  | Map an existing scheme to the defaults      |

### Workflow

1. Confirm settings and collect documents.
2. Inventory every document and check readability.
3. Extract the fact base per role with source tags.
4. Resolve conflicts and ask up to ten open questions in one batch.
5. Reconcile or build the skills list.
6. Write the baseline and the selection pool.
7. Produce the verification report.
8. Optionally convert to a project-based CV and project list.

### Outputs

- Baseline CV: personal data, contribution, profile, experience, development,
  education, languages, hobbies, references, selection pool.
- Skills list with levels and evidence.
- Verification report.
- Optional project CV and project list.
- Open items.

### Gates and stop conditions

- Required document groups present, or the user accepts a partial set.
- Every page needed for a fact is readable; otherwise stop and name the file and
  part.
- Language and settings chosen before output.
- No CV text before the fact base and conflict review.
- No invented fact, number, date, title, or outcome.
- No silent overwrite of an approved baseline.

### Handoff

The baseline and verification report are the evidence source for
`zj-job-fit-evaluation`. The optional project variant preserves `[QUANTIFIED]`
markers and `[TO CONFIRM]` fields.

### Example

[`../examples/zj-baseline-cv/expected-output.md`](../examples/zj-baseline-cv/expected-output.md)

### Full instructions

[`../zj-baseline-cv/SKILL.md`](../zj-baseline-cv/SKILL.md) and
[`../zj-baseline-cv/references/`](../zj-baseline-cv/references/).

## zj-job-fit-evaluation

**Purpose:** evaluate one posting against documented evidence and produce a fit
report, keyword map, and evidence pack. It does not rewrite the CV or write a
cover letter.

**Use when:** deciding whether to apply, comparing a posting with the profile,
or preparing approved evidence for tailoring.

**Do not use for:** baseline building, CV writing, cover letters, or company
research.

### Inputs

| Input                        | Required | Notes                                            |
| ---------------------------- | -------- | ------------------------------------------------ |
| Posting text                 | Yes      | Read the posting, not the title                  |
| Baseline or evidence profile | Yes      | Source of candidate claims                       |
| Eligibility rule             | Optional | User-supplied only                               |
| Language rule                | Optional | Compare posting requirement with declared levels |
| Location and travel rules    | Optional | User-supplied only                               |
| Scoring scheme               | Optional | Weights and bands only if supplied               |
| Salary market and currency   | Optional | Only when salary guidance is requested           |
| Trim review                  | Optional | Off by default                                   |

### Workflow

1. Confirm posting and evidence; choose language and report settings.
2. Apply only user-supplied gates.
3. Optional impact capture: up to five questions per role, one at a time.
4. Employment-gap review for gaps of three months or more.
5. Green/Red/Yellow keyword analysis with verifiability.
6. Skills match table and overall summary with a stated basis.
7. Optional relevance trim, confirmed line by line.
8. Clarifying questions only if they block the report.
9. Fit, risk, interview likelihood, recommendation.
10. Optional salary note for the configured market.
11. Hand off the evidence pack and keyword map.

### Outputs

- Fit report: gates, keyword analysis, match table, summary, strengths, gaps,
  risks, interview likelihood, recommendation, open items.
- Evidence pack: claims, answers, gates, fit, trim decisions, open items.
- Keyword map: term, colour, verifiability, placement.
- Optional trim list and salary note.

### Gates and stop conditions

- Posting and evidence present.
- Only user-defined gates; do not invent eligibility, language, or location
  rules.
- Missing language level is a fail; a declared level below the posting bar is a
  flag.
- No invented evidence, score, or guarantee.
- Do not write CV text or a cover letter.
- Stop if the gate rule is missing or the evidence is insufficient.

### Handoff

The evidence pack and keyword map are the only evidence source for
`zj-tailored-application`. Tailoring must stop if the pack is missing or stale.

### Example

[`../examples/zj-job-fit-evaluation/expected-output.md`](../examples/zj-job-fit-evaluation/expected-output.md)

### Full instructions

[`../zj-job-fit-evaluation/SKILL.md`](../zj-job-fit-evaluation/SKILL.md) and
[`../zj-job-fit-evaluation/references/`](../zj-job-fit-evaluation/references/).

## zj-tailored-application

**Purpose:** produce a tailored CV and cover letter for one posting from the
baseline and an approved evaluation, with a change log.

**Use when:** the evaluation says proceed and the candidate wants documents for
one specific posting.

**Do not use for:** baseline creation, re-evaluation, or inventing evidence.

### Inputs

| Input                        | Required | Notes                           |
| ---------------------------- | -------- | ------------------------------- |
| Baseline CV                  | Yes      | Source of material              |
| Approved evidence pack       | Yes      | Only approved claims            |
| Approved keyword map         | Yes      | Green/Red/Yellow decisions      |
| Posting text                 | Yes      | Target role and context         |
| Confirmed trim list          | Optional | Line-level removals only        |
| Template                     | Setting  | Or clean Markdown               |
| CV and cover-letter language | Setting  | May differ                      |
| Spelling convention          | Setting  | Never hardcoded                 |
| Document order               | Setting  | Default: CV, letter, change log |

### Workflow

1. Preflight: baseline, pack, keyword map, posting, languages.
2. Select roles and sections; log and confirm whole-role selection.
3. Apply only confirmed line trims.
4. Write the contribution paragraph.
5. Write the profile bullets.
6. Integrate the target role into at most one bullet per role.
7. Enhance flagged impact bullets one at a time.
8. Write the cover letter.
9. Check every claim against the pack and write the change log.

### Outputs

- Tailored CV.
- Cover letter.
- Change log: section, before, after, reason, evidence, confirmation.
- Open items.

### Gates and stop conditions

- Baseline, pack, keyword map, and posting present.
- Pack current and for this posting.
- Official job titles unchanged.
- At most one target-role adaptation per role.
- No new claims outside the pack.
- Role-level selection logged and confirmed; line-level trims require the
  confirmed list.
- No submission, email, or publish.

### Handoff

Consumes the evaluation's evidence pack and keyword map. Does not create a
second evidence set. If a new claim is needed, stop and ask the candidate, then
update the pack.

### Example

[`../examples/zj-tailored-application/expected-output.md`](../examples/zj-tailored-application/expected-output.md)

### Full instructions

[`../zj-tailored-application/SKILL.md`](../zj-tailored-application/SKILL.md) and
[`../zj-tailored-application/references/`](../zj-tailored-application/references/).

## Settings by skill

| Setting                | zj-baseline-cv | zj-job-fit-evaluation | zj-tailored-application |
| ---------------------- | ----------- | ------------------ | -------------------- |
| Working language       | Yes         | Yes                | Yes                  |
| Output language        | Yes         | Yes                | Yes                  |
| Spelling convention    | Yes         | No                 | Yes                  |
| Template               | Yes         | No                 | Yes                  |
| Target roles           | Yes         | No                 | No                   |
| Evidence tags          | Yes         | Yes                | Yes                  |
| Eligibility rule       | No          | Optional           | No                   |
| Language rule          | No          | Optional           | No                   |
| Location / travel rule | No          | Optional           | No                   |
| Scoring scheme         | No          | Optional           | No                   |
| Salary market          | No          | Optional           | No                   |
| Trim review            | No          | Optional           | Consumes result      |
| Document order         | No          | No                 | Yes                  |

## Shared rules

| File                    | Use                                                           |
| ----------------------- | ------------------------------------------------------------- |
| `shared/evidence.md`    | Source tags, confidence, conflicts, gaps, skill levels        |
| `shared/interaction.md` | Language, questions, impact capture, confirmations, fallbacks |
| `shared/keywords.md`    | Green/Red/Yellow, verifiability, match tables                 |
| `shared/gates.md`       | Entry gates, stop conditions, final checks                    |
| `shared/output.md`      | Output order, document order, change log, handoff             |
| `shared/style.md`       | CV, contribution, profile, cover letter, punctuation          |

## Handoff schema

```text
evidence_pack:
  claims[]:         claim, source_tag, confidence, role_or_project
  answers[]:        question, answer, confidence
  keywords[]:       term, colour, verifiability
  gates:            eligibility, language, location, other
  fit:              strengths[], gaps[], risks[], recommendation, optional score
  trim_decisions[]: line_id, decision
  open_items[]:     item, why it matters
```
