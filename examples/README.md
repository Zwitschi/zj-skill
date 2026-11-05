# Fictional worked examples

These examples test the three skills without using any real candidate or
employer. Every person, company, school, address, email, and phone number is
invented. The `.test` domain and `555` phone range are reserved for examples.

## Test flow

1. Run `zj-baseline-cv` on the source documents in
   [`shared/candidate-alex-morgan.md`](shared/candidate-alex-morgan.md).
   Compare the result with
   [`zj-baseline-cv/expected-output.md`](zj-baseline-cv/expected-output.md).
2. Run `zj-job-fit-evaluation` on the baseline result and
   [`shared/posting-senior-operations-analyst.md`](shared/posting-senior-operations-analyst.md).
   Compare with
   [`zj-job-fit-evaluation/expected-output.md`](zj-job-fit-evaluation/expected-output.md).
3. Run `zj-tailored-application` on the baseline, the evaluation output, and the
   posting. Compare with
   [`zj-tailored-application/expected-output.md`](zj-tailored-application/expected-output.md).

The examples are sequential: the evaluation uses the baseline evidence, and
tailoring uses the evaluation's evidence pack and keyword map.

## Acceptance criteria

A run passes when:

- the required sections and order are present;
- every claim traces to the fictional source documents or a recorded answer;
- source tags and confidence labels are used;
- conflicts are resolved or listed;
- Green terms have verifiability verdicts;
- gaps are named, not smoothed over;
- confirmed trims are the only removals;
- official job titles are unchanged;
- at most one experience bullet per role is adapted;
- no new fact, metric, employer, or tool is invented;
- no real personal data appears in the output.

## Files

| File                                                                                         | Purpose                                                     |
| -------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| [`shared/candidate-alex-morgan.md`](shared/candidate-alex-morgan.md)                         | Fictional candidate, source documents, and recorded answers |
| [`shared/posting-senior-operations-analyst.md`](shared/posting-senior-operations-analyst.md) | Fictional posting                                           |
| [`zj-baseline-cv/expected-output.md`](zj-baseline-cv/expected-output.md)                           | Expected baseline CV, skills list, verification report      |
| [`zj-job-fit-evaluation/expected-output.md`](zj-job-fit-evaluation/expected-output.md)             | Expected fit report, keyword map, evidence pack             |
| [`zj-tailored-application/expected-output.md`](zj-tailored-application/expected-output.md)         | Expected tailored CV, cover letter, change log              |

## Note on output variance

The expected outputs are reference shapes. A valid run may phrase sentences
differently, but it must not add facts or skip sections. The examples are not a
golden file comparison; use them to check structure, evidence discipline, and
gate handling.
