---
name: zj-job-fit-evaluation
description: Evaluate one job posting against a candidate's documented evidence and produce a fit report, keyword map, and evidence pack for application decisions. Use when the user asks whether to apply, wants a job match or fit assessment, an ATS or keyword analysis, a gap and risk review, or a shortlist score. Not for writing or tailoring a CV or cover letter; use zj-tailored-application for that.
---

# Job fit evaluation

Evaluate one posting against the candidate's documented evidence. The output is a
fit report, an approved keyword map, and an evidence pack for later tailoring.
This skill does not rewrite the CV and does not write a cover letter.

## Read before starting

Read these shared rules first:

- [`../shared/evidence.md`](../shared/evidence.md)
- [`../shared/interaction.md`](../shared/interaction.md)
- [`../shared/keywords.md`](../shared/keywords.md)
- [`../shared/gates.md`](../shared/gates.md)
- [`../shared/output.md`](../shared/output.md)

Detailed steps are in
[`references/evaluation-workflow.md`](references/evaluation-workflow.md). The
report skeleton is in
[`references/fit-report-template.md`](references/fit-report-template.md).

A fictional worked example, including the posting and the expected report, is in
[`../examples/zj-job-fit-evaluation/expected-output.md`](../examples/zj-job-fit-evaluation/expected-output.md).

If file reading is unavailable, ask the user to paste the referenced files. If
file writing is unavailable, return the fit report, evidence pack, and keyword
map in the conversation as Markdown.

## What this skill does not do

- It does not write or rewrite a CV.
- It does not write a cover letter.
- It does not invent evidence to improve a match.
- It does not apply weights, bands, locations, or hard gates that the user has
  not supplied.
- It does not submit, email, or publish anything.

## Inputs

Required:

- the posting text;
- the candidate's baseline CV or an equivalent evidence profile.

Optional:

- an existing skills list;
- an approved evidence pack from an earlier run;
- the candidate's preferences and constraints.

Settings, supplied as placeholders:

| Placeholder          | Meaning                                                          |
| -------------------- | ---------------------------------------------------------------- |
| `<working-language>` | Language used during the evaluation                              |
| `<output-language>`  | Language of the fit report                                       |
| `<eligibility-gate>` | Optional user-defined eligibility rules                          |
| `<language-gate>`    | Optional required-language rules, based on declared levels       |
| `<location-gate>`    | Optional commute, remote, or relocation rules                    |
| `<scoring-scheme>`   | Optional weights or bands; leave empty for a qualitative summary |
| `<salary-market>`    | Optional market for salary guidance                              |
| `<currency>`         | Optional currency for salary guidance                            |
| `<trim-review>`      | Whether to run the CV trim review                                |

Do not assume a country, city, market, currency, language, or scoring scheme.
Ask only for settings that affect the requested output.

## Workflow

1. **Documents and settings.** Confirm that both the posting and the candidate
   evidence exist. Confirm working language and report language. Ask whether
   impact capture and the trim review are wanted.
2. **Gates.** Apply only the gates the user has supplied: eligibility, language,
   location, or other hard constraints. Record pass, flag, or fail with the
   quoted posting evidence.
3. **Impact capture, optional.** Ask up to five questions per role, only where
   an outcome is missing. Record answers with confidence tags.
4. **Gap analysis.** Scan the timeline for gaps of three months or more, ask
   what happened, and propose handling. Do not infer reasons.
5. **Keyword analysis.** Classify posting terms as Green, Red, or Yellow. Record
   verifiability for every Green term.
6. **Match tables.** Produce the keyword list, skills match table, and match
   summary. Use the configured scoring scheme if supplied; otherwise use a
   qualitative summary with a stated basis.
7. **Relevance trim, optional.** Present CV lines one at a time with
   Keep/Trim/skip. Default to Keep when unanswered. Output the confirmed list;
   do not edit the CV.
8. **Clarifying questions.** Ask only what blocks the report.
9. **Fit and risk.** Assess strengths, gaps, risks, and interview likelihood with
   reasoning.
10. **Salary, optional.** Give a range for the configured market only if
    requested and derivable, with stated uncertainty.
11. **Handoff.** Produce the evidence pack and keyword map for tailoring.

## Gates

A gate is a pass, flag, or fail with quoted evidence. Do not invent a gate.

- **Eligibility:** only if the user defines a rule. Quote the posting's exact
  eligibility wording.
- **Language:** compare the posting's stated requirement for the role against the
  candidate's declared levels. A language absent from the profile is a fail; a
  declared language whose required level plausibly exceeds the declared level is
  a flag.
- **Location:** only if the user supplies a rule. Do not invent a commute radius
  or a list of acceptable cities.
- **Other:** any user-defined constraint, such as work mode, start date, or
  permit timing.

A failed gate is a reason not to apply. A flagged gate stays in the report with
a visible warning.

## Output contract

| Artifact              | Required contents                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Fit report            | Header, gates, keyword analysis, match table, summary, strengths, gaps, risks, interview likelihood, recommendation, open items |
| Evidence pack         | Claims used, source tags, confidence, answers from impact capture                                                               |
| Keyword map           | Green, Red, and Yellow terms with verifiability and proposed placement                                                          |
| Trim list, optional   | Confirmed Keep/Trim decisions for CV lines                                                                                      |
| Salary note, optional | Range, market, currency, reasoning, uncertainty                                                                                 |
| Gate results          | Pass, flag, or fail with quoted evidence                                                                                        |

Every report is a working assessment, not a guarantee. Do not state that an
interview or offer will happen.

## Report structure

Use the template in
[`references/fit-report-template.md`](references/fit-report-template.md). The
minimum sections are:

1. Posting summary.
2. Gate results.
3. Keyword analysis.
4. Skills match table.
5. Match summary and basis.
6. Strengths.
7. Gaps and risks.
8. Interview likelihood.
9. Recommendation and next step.
10. Open items.
11. Handoff summary.

## Recommendation

Use one of:

- proceed;
- proceed with named gaps or flags;
- do not apply, with the reason.

The recommendation must follow from the evidence and gates. Do not recommend an
application when a hard gate fails, and do not hide a gap to make the
recommendation look better.

## Handoff

The evidence pack and keyword map feed the `zj-tailored-application` skill. Use the
contract in [`../shared/output.md`](../shared/output.md). Do not let tailoring
invent claims outside the pack.

## Quality checklist

- Both inputs were present before the evaluation started.
- Every gate is user-defined or explicitly absent.
- Every Green term has a verifiability verdict.
- Every gap is named.
- The trim list, if produced, is confirmed and not applied.
- The match summary states its basis.
- The recommendation follows from the evidence.
- No CV text or cover letter was written.
- No fact or metric was invented.
- The report is labelled as a working assessment.

## Stop conditions

Stop and ask when:

- the posting or candidate evidence is missing;
- a gate needs a rule the user has not supplied;
- a required language has no declared level;
- the evidence pack conflicts with the CV;
- the user asks for a guarantee, a score without a basis, or a claim that cannot
  be evidenced.
