# Evaluation workflow

Detailed steps for the `zj-job-fit-evaluation` skill. Read the shared evidence,
interaction, keyword, gate, and output rules first. This file covers the
evaluation-specific work only.

## Step 0: Settings and documents

Confirm:

- the posting text is available;
- the candidate's baseline CV or evidence profile is available;
- working language;
- report language;
- whether impact capture is wanted;
- whether the trim review is wanted;
- which gates the user wants applied;
- whether salary guidance is wanted, and for which market and currency;
- whether a scoring scheme exists. If not, plan a qualitative summary.

If the CV or posting is missing, stop and ask. Do not evaluate from a job title
alone.

## Step 1: Gates

Apply only user-supplied gates. For each, quote the posting evidence and record
pass, flag, or fail.

### Eligibility

- Quote the posting's eligibility, work-rights, or clearance wording verbatim.
- If the user supplied an eligibility rule, compare it to the candidate's
  documented status.
- Silence in the posting is not permission. Mark it unverified and say what
  needs checking.
- Do not infer citizenship, permits, or clearance from a name or location.

### Language

- Read the language requirement for the role, not the language the ad is written
  in.
- Compare each required language to the candidate's declared level.
- Absent from the profile: fail.
- Declared but plausibly below the posting's stated bar: flag, with both levels
  quoted.
- At or above the declared level: pass.

### Location

- Apply only the user's rule, such as a commute area, remote-only, or no
  relocation.
- Do not invent a city list or radius.
- A location that requires relocation is a fail only if the user defined
  relocation as a deal-breaker.

### Other gates

User-defined constraints such as work mode, start date, permit timing, travel,
or on-call. Quote the posting and apply the rule as written.

## Step 2: Impact capture, optional

Ask first whether impact capture is needed. If yes:

- Go through each role and ask up to five questions, only where the bullet lacks
  a measurable or inferable outcome.
- State the total number of questions before the first one.
- Ask one at a time and wait for an answer or a skip.
- Cover scale, before and after, timeframe, method, and confidence.
- Skip roles that already contain a clear, quantified outcome.
- Record answers with a confidence tag: exact, estimated, or approximate.
- Do not fill a skipped question later.

Add the answers to the evidence pack as new claims, clearly marked as collected
in this run.

## Step 3: Gap analysis

- Scan the timeline for gaps of three months or more, including before the first
  role when a start or education date is visible.
- Ask what happened. Do not guess.
- Classify the answer in the candidate's own words.
- Offer handling options: a short factual CV line, month-level dates, a
  cover-letter mention, or no action.
- Record the confirmed decision.
- Do not state a gap in a document from this skill. The decision is handed to
  tailoring.

## Step 4: Keyword analysis

Classify posting terms using the shared keyword rules.

### Green

Specific technical terms, named methods, systems, certifications, and industry
vocabulary that appear exactly or near-exactly in the posting. Highest priority.

For each Green term record:

- term as written in the posting;
- whether it is evidenced: yes, partially, or no;
- where the evidence sits, if any;
- a proposed placement: CV body, contribution, profile, or gap.

### Red

General working style, communication, teamwork, independence, and cross-role
soft skills. Use in support, never at the expense of Green.

### Yellow

Company values, leadership culture, work environment, vision, and
motivation-level language. Reserve for the cover letter.

### Output

Produce one table ordered by class:

| Term | Class | Verifiability | Evidence | Placement |
| ---- | ----- | ------------- | -------- | --------- |

Then a short "Gaps" list naming every Green term with no evidence. Use the exact
sentence: "Term X is a specific requirement in the posting but is not evidenced
in the candidate's documents."

## Step 5: Skills match table

Map each significant requirement to the candidate's evidence:

| Requirement | Posting wording | Candidate evidence | Verdict | Note |
| ----------- | --------------- | ------------------ | ------- | ---- |

Verdicts: strong, partial, gap, or not applicable.

Do not force a requirement into a match. A partial match is not a strong match.

## Step 6: Match summary

Use the configured scoring scheme if one exists. State the weights and bands and
show the arithmetic. If no scheme exists, produce:

- a qualitative summary: strong, mixed, or weak;
- the basis: how many Green terms are evidenced, which critical gaps remain,
  which gates are flagged;
- an uplift estimate showing how much coverage could improve by rewording
  existing evidence only.

Do not invent a numeric score, weights, or bands. Do not compare the candidate to
an imaginary ideal candidate.

## Step 7: Relevance trim, optional

Run only if the user asked for it.

- Using the keyword analysis, flag CV lines that have no Green or Red relevance
  and add no unique differentiator, continuity signal, or context.
- State the total number of flagged lines.
- Present one line at a time: line, section, why flagged.
- Ask for Keep, Trim, or skip.
- Default unanswered to Keep.
- Output only the confirmed list.

Do not edit the CV. The trim list is an input for tailoring.

## Step 8: Clarifying questions

Ask only questions that block the report. If the report can be produced with a
stated assumption, state the assumption and continue. If several questions are
needed, state the total and ask one at a time.

## Step 9: Fit and risk

Produce:

- **Strengths:** where the match is particularly strong, with evidence.
- **Gaps and risks:** missing Green terms, thin evidence, gate flags, domain
  changes, seniority mismatch, or recruiter concerns.
- **Interview likelihood:** a qualitative assessment with reasoning. Do not give
  a false percentage.
- **Recommendation:** proceed, proceed with named gaps or flags, or do not
  apply, with the reason.

## Step 10: Salary, optional

Only if requested and derivable from the posting and profile:

- state the market and currency;
- give a range, not a single number;
- explain the basis: role level, domain, location if supplied, and any posting
  signal;
- state uncertainty and missing data;
- do not invent a benchmark dataset or a precise offer.

If the posting does not provide enough signal and the user has no benchmark,
say so and omit the range.

## Step 11: Handoff

Produce the evidence pack and keyword map in the shared output format:

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

The pack is the only evidence tailoring may use. If a new claim is needed later,
tailoring must ask the candidate and update the pack.

## Quality checks

- The posting was read, not inferred from the title.
- Every gate is user-defined or explicitly absent.
- Every Green term has a verdict.
- Every gap is named.
- The summary states its basis.
- The recommendation follows from the gates and evidence.
- No CV or cover letter was written.
- The evidence pack is complete enough for tailoring.
