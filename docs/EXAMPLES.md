# Examples

Status: complete. The package includes a fictional candidate and posting so the
skills can be tested without personal data.

## Files

- [`../examples/shared/candidate-alex-morgan.md`](../examples/shared/candidate-alex-morgan.md):
  fictional candidate and source documents.
- [`../examples/shared/posting-senior-operations-analyst.md`](../examples/shared/posting-senior-operations-analyst.md):
  fictional posting.
- [`../examples/zj-baseline-cv/expected-output.md`](../examples/zj-baseline-cv/expected-output.md):
  baseline CV, skills list, verification report.
- [`../examples/zj-job-fit-evaluation/expected-output.md`](../examples/zj-job-fit-evaluation/expected-output.md):
  fit report, keyword map, evidence pack.
- [`../examples/zj-tailored-application/expected-output.md`](../examples/zj-tailored-application/expected-output.md):
  tailored CV, cover letter, change log.

## Run the example

1. Install the package into a skill path the agent discovers.
2. Ask the agent to run `zj-baseline-cv` on the fictional source documents.
3. Compare the output with the expected baseline.
4. Run `zj-job-fit-evaluation` on the baseline and the fictional posting.
5. Run `zj-tailored-application` with the baseline, evaluation, and posting.
6. Check the output contracts and the acceptance criteria.

Do not use a real CV for the first run. The fictional example exposes missing
steps without exposing personal data.

## Acceptance criteria

- Required sections and order are present.
- Every claim traces to a source or a recorded answer.
- Source tags and confidence labels are used.
- Conflicts are resolved or listed.
- Green terms have verifiability verdicts.
- Gaps are named.
- Only confirmed line trims are applied.
- Official titles are unchanged.
- At most one target-role adaptation per role.
- No invented facts, numbers, or outcomes.
- No real personal data appears in the output.

The examples are reference shapes, not golden files. Phrasing may differ; the
contract must hold.
