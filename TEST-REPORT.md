# Skill test report

Contract walkthrough for the three public skills against the fictional examples.
The test applies each `SKILL.md` and its references to the example inputs, then
checks the result against the expected output and the skill's output contract.

Tested 2026-11-05.

## Scope and method

- Inputs: [`examples/shared/candidate-alex-morgan.md`](examples/shared/candidate-alex-morgan.md)
  and [`examples/shared/posting-senior-operations-analyst.md`](examples/shared/posting-senior-operations-analyst.md).
- Expected outputs: one per skill under [`examples/`](examples/).
- Method: section-by-section contract check, cross-skill consistency check, and
  structural checks for tags, titles, numbers, links, and style.
- This is a walkthrough, not an automated model run. Phrasing may vary in a real
  run; the contract must still hold.

## Baseline CV

| Contract item                            | Result | Note                                                             |
| ---------------------------------------- | ------ | ---------------------------------------------------------------- |
| Required inputs requested in one message | Pass   | Skill instructs one intake message                               |
| Inventory and readability stop           | Pass   | Inventory table and exact-file stop rule present                 |
| Fact base with source tags               | Pass   | All experience bullets carry tags                                |
| Conflict handling                        | Pass   | CV 03/2021 vs reference 04/2021; official document wins          |
| Questions limited and batched            | Pass   | Conflict questions capped at ten in one message                  |
| Skills list with scale and evidence      | Pass   | Scale definitions and evidence column present                    |
| Section order complete                   | Pass   | All baseline sections present                                    |
| Selection pool separated                 | Pass   | Present and labelled baseline-only                               |
| Verification report                      | Pass   | Documents, conflicts, single-source claims, open items, reminder |
| Output contract met                      | Pass   | Baseline, skills list, verification report produced              |

## Job fit evaluation

| Contract item                           | Result | Note                                                     |
| --------------------------------------- | ------ | -------------------------------------------------------- |
| Posting and evidence present            | Pass   | Both inputs used                                         |
| Gates user-defined                      | Pass   | Location rule stated; eligibility and salary not applied |
| Language gate                           | Pass   | English requirement matches native level                 |
| Impact capture optional                 | Pass   | Recorded answers used, confidence tagged                 |
| Gap analysis                            | Pass   | Three-month rule and confirmed handling                  |
| Green/Red/Yellow classification         | Pass   | All eight Green terms have verdicts                      |
| Skills match table                      | Pass   | Requirement, evidence, verdict, note                     |
| Match summary with basis                | Pass   | Qualitative summary, counts, uplift basis                |
| Trim review optional                    | Pass   | Not requested; no removals                               |
| Clarifying questions only when blocking | Pass   | None needed in the example                               |
| Fit and risk assessment                 | Pass   | Strengths, gaps, risks, interview likelihood             |
| Salary optional and configured          | Pass   | Not requested, no range invented                         |
| Handoff pack                            | Pass   | Evidence pack, keyword map, gates, open items            |
| No CV or cover letter written           | Pass   | Report only                                              |

## Tailored application

| Contract item                             | Result | Note                                                                     |
| ----------------------------------------- | ------ | ------------------------------------------------------------------------ |
| Preconditions met                         | Pass   | Baseline, evidence pack, keyword map, posting present                    |
| Baseline used, not an earlier tailored CV | Pass   | Source is the baseline                                                   |
| Contribution structure                    | Pass   | First person, prose, about six lines, approved results                   |
| Profile structure                         | Pass   | Five positioning bullets, no results                                     |
| Official titles unchanged                 | Pass   | Both titles match the baseline                                           |
| At most one adapted bullet per role       | Pass   | One adaptation per role; one separate impact rewrite                     |
| Impact enhancement confirmed              | Pass   | Power BI bullet uses a recorded answer                                   |
| Cover letter Yellow-led                   | Pass   | Customer-first, continuous improvement, sustainability, ownership        |
| No invented employer connection           | Pass   | No claim beyond the posting and evidence                                 |
| Role selection and line trims             | Pass   | Role selection is logged and confirmed; line trims need a confirmed list |
| Change log complete                       | Pass   | Section, before, after, reason, evidence, confirmation                   |
| Handoff pack respected                    | Pass   | Every number traces to the pack                                          |
| No submission                             | Pass   | Draft only                                                               |

## Cross-skill consistency

| Check                                                                                                                       | Result |
| --------------------------------------------------------------------------------------------------------------------------- | ------ |
| Official job titles identical in baseline and tailored CV                                                                   | Pass   |
| Key numbers (18%, 10 hours, 12% to 3%, eight coordinators, 120 SKUs) appear in the evidence pack and the tailored documents | Pass   |
| Cover letter contains none of the banned clichés tested (passionate, perfect fit, dream role, unique opportunity, thrilled) | Pass   |
| No em dashes in the example outputs                                                                                         | Pass   |
| No real personal data outside `LICENSE`                                                                                     | Pass   |
| Relative links resolve                                                                                                      | Pass   |
| YAML frontmatter valid                                                                                                      | Pass   |

## Findings and fixes

| Finding                                                                                     | Fix                                                                                               |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Baseline skills list stated levels but not the 1 to 5 scale definitions                     | Added the scale definitions above the table                                                       |
| Evaluation assumed a location rule without showing it as a configured setting               | Added a "Configured settings" block before the posting summary                                    |
| Change-log reason "Target-role positioning" did not match the allowed reason vocabulary     | Changed to "Target-role integration"                                                              |
| Role-level selection versus line-level trimming was ambiguous (found in an end-to-end test) | Clarified in `zj-tailored-application` and the shared gates/output rules; re-ran this contract check |

## Residual risks

- A real agent run may phrase sections differently. The contract checks structure
  and evidence, not exact wording.
- The evaluation's qualitative summary depends on judgement; the examples show
  the basis, not a reproducible score.
- The tailored example contains one impact rewrite in addition to one target-role
  adaptation per role. The skill allows both, but a strict reviewer may count
  edits rather than purposes. The change log separates the reasons.
- No install test or public repository test has been run yet.

## Verdict

All three skills meet their output contracts on the fictional example. No
contract blocker remains for publication preparation. A real end-to-end agent
run is still recommended after installation.
