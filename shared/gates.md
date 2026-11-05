# Gates and stop conditions

Use these gates before, during, and after a workflow. A gate is not advisory. If
it fails, stop and say why.

## Entry gates

| Gate                                   | Applies to            | Pass condition                                                                                  |
| -------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------------- |
| Required documents present             | Baseline              | All required document groups are available, or the user explicitly accepts a partial set        |
| Posting and candidate evidence present | Evaluation, tailoring | Both the posting and a baseline or evidence profile exist                                       |
| Working language chosen                | All                   | The user has chosen the working language before output starts                                   |
| Output language chosen                 | All                   | Each document's output language is known                                                        |
| Documents readable                     | Baseline              | Every page needed for a fact is readable; otherwise name the exact file and part                |
| History is task-based                  | Project conversion    | The CV describes responsibilities rather than discrete projects; if already project-based, stop |
| Evaluation is current                  | Tailoring             | An approved evidence pack and keyword map exist for this posting                                |

## Stop conditions

Stop and ask, do not work around:

- a missing CV, posting, or baseline;
- an unreadable document, scan, password, or truncated page;
- a CV that is already project-based when conversion was requested;
- a tailoring request without an evaluation;
- an instruction to add a fact that has no source;
- a request to state a gap without confirmed wording;
- a request to submit or publish something the user has not approved.

## Human confirmation gates

Ask before:

- trimming or removing a CV line;
- condensing or omitting an entire role;
- rewriting a bullet with a new outcome;
- stating an employment gap;
- adapting an experience bullet for a target role;
- adding a salary expectation;
- moving from one role to the next in a project interview;
- treating a draft as final.

Default when a trim question is unanswered: keep the line. Details are in
[`interaction.md`](interaction.md).

## Final checks

Run these before presenting any document:

1. Every factual claim traces to a source tag or an explicit answer.
2. No invented number, date, tool, title, employer, or outcome.
3. Official job titles are unchanged.
4. At most one adapted experience bullet per role.
5. Role-level selection is logged and confirmed, and line-level trims are
   confirmed.
6. Every Green term in the CV is verifiable.
7. Every gap is named, not smoothed over.
8. Open items are listed, not hidden.
9. The keyword map was used, not re-created.
10. The change log explains every edit.
11. Language, spelling, and punctuation settings are respected.
12. The document is labelled as a working draft unless the user approves it as
    final.
13. No submission, email, or external publish has happened without explicit
    approval.

## Failure behaviour

When a gate fails:

- state the gate that failed;
- name the missing input or unsupported claim;
- offer the smallest safe next step;
- do not continue with a silent assumption.
