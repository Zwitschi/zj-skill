# Output order and handoff

Fixed output order keeps the reasoning visible and prevents tailoring from
starting before the evidence is settled.

## Baseline output order

1. Language and settings confirmation.
2. Document inventory and readability result.
3. Fact base summary with source tags.
4. Conflicts, gaps, and open questions, with answers.
5. Skills list with levels and evidence.
6. Baseline CV in the agreed section order.
7. Verification report.
8. Optional project conversion: per-role CV short versions and the standalone
   project list.

## Evaluation output order

1. Language and settings confirmation.
2. Eligibility, language, location, and other configured gates.
3. Impact capture, if requested.
4. Employment-gap analysis, with confirmed handling.
5. Keyword analysis: Green, Red, Yellow, with verifiability.
6. Skills match table and overall match summary.
7. Relevance trim review, if requested, with confirmed decisions.
8. Clarifying questions, only if they block output.
9. Strengths, gaps, and risks.
10. Interview-likelihood assessment with reasoning.
11. Salary note, only if requested and derivable.
12. Evidence pack and keyword map for tailoring.

## Tailoring output order

1. Language and settings confirmation.
2. Contribution paragraph.
3. Profile bullets.
4. Experience section with target-role integration.
5. Impact enhancement, one bullet at a time.
6. Cover letter.
7. Change log.
8. Open items.

## Document order

When a bundle contains several documents, present them in this order:

1. Tailored CV.
2. Cover letter.
3. Change log.
4. Open items or verification notes.

The change log is never optional when a baseline fact or bullet was rewritten.

## Working drafts and overwrites

- Every generated document is a working draft until the user approves it.
- Do not overwrite a source document. Write a new draft or a clearly named
  variant.
- Preserve the baseline unchanged. Tailoring selects and reorders; it does not
  edit the baseline.

## Change log fields

For each edit, record:

- section and line or bullet;
- before and after;
- reason: keyword match, impact enhancement, clarity, role selection, trim, or
  target-role integration;
- evidence or source tag supporting the change;
- confirmation status.

## Handoff contract

The evaluation skill produces, and the tailoring skill consumes:

```text
evidence_pack:
  claims[]:         claim, source_tag, confidence, role_or_project
  answers[]:        question, answer, confidence
  keywords[]:       term, colour (green/red/yellow), verifiability
  gates:            eligibility, language, location, other
  fit:              strengths[], gaps[], risks[], recommendation, optional score
  trim_decisions[]: line_id, decision (keep/trim)
  open_items[]:     item, why it matters
```

The tailoring skill must not add claims outside this pack without asking the
candidate. If the pack is missing, stale, or for a different posting, stop and
request an evaluation first.

## Format

Use the user's configured template and file format. If none is configured,
produce clean Markdown with stable headings. Do not add rendering, PDF, or
layout-engine steps to the skill.
