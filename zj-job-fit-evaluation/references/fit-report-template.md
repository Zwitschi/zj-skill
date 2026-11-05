# Fit report template

Use this skeleton for the evaluation output. Replace bracketed placeholders.
Delete sections that do not apply, but keep the order.

```markdown
# Fit report: <role> at <employer>

- Source: <posting URL or "pasted text">
- Evaluated: <date>
- Report language: <language>
- Evidence base: <baseline version or evidence profile version>
- Scoring basis: <configured scheme with weights, or "qualitative">

## Posting summary

<Three to six sentences: role, level, domain, core requirements, work mode,
location if relevant, and anything unusual.>

## Gate results

| Gate        | Rule                       | Posting evidence            | Verdict                          | Note   |
| ----------- | -------------------------- | --------------------------- | -------------------------------- | ------ |
| Eligibility | <rule or "not configured"> | <quoted text or "silent">   | pass / flag / fail / not applied | <note> |
| Language    | <rule or "not configured"> | <quoted requirement>        | pass / flag / fail / not applied | <note> |
| Location    | <rule or "not configured"> | <quoted location/work mode> | pass / flag / fail / not applied | <note> |
| <other>     | <rule>                     | <quoted text>               | pass / flag / fail / not applied | <note> |

## Keyword analysis

### Green terms

| Term   | Verifiability        | Evidence           | Proposed placement                     |
| ------ | -------------------- | ------------------ | -------------------------------------- |
| <term> | yes / partially / no | <source or "none"> | CV body / contribution / profile / gap |

### Red terms

<Short list or table with placement.>

### Yellow terms

<Short list reserved for the cover letter.>

### Gaps

- <Term X is a specific requirement in the posting but is not evidenced in the
  candidate's documents.>

## Skills match

| Requirement   | Posting wording | Candidate evidence   | Verdict                      | Note   |
| ------------- | --------------- | -------------------- | ---------------------------- | ------ |
| <requirement> | <quote>         | <evidence or "none"> | strong / partial / gap / n/a | <note> |

## Match summary

<If a scoring scheme is configured: show weights, per-dimension values, total,
and band. If not: qualitative summary with basis.>

**Basis:** <how many Green terms are evidenced, which critical gaps remain,
which gates are flagged.>

**Uplift potential:** <how much coverage could improve by rewording existing
evidence only; no new claims.>

## Strengths

- <Strength, with evidence reference.>

## Gaps and risks

- <Gap or risk, with why it matters.>

## Interview likelihood

<Qualitative assessment and reasoning. Do not invent a percentage.>

## Recommendation

<proceed / proceed with named gaps or flags / do not apply>

<Reason tied to gates and evidence. State the smallest useful next step.>

## Salary note (optional)

- Market: <market>
- Currency: <currency>
- Range: <range>
- Basis: <role level, domain, posting signal, benchmark if supplied>
- Uncertainty: <what is missing>

## Open items

- <Item the candidate must confirm or supply.>

## Handoff

- Evidence pack: <path or inline summary>
- Keyword map: <path or inline summary>
- Trim list: <path, inline summary, or "not requested">
```

## Rules for the report

- Quote gate evidence; do not paraphrase away a requirement.
- Do not use a numeric score without a configured basis.
- Do not use verdict labels that imply a guarantee.
- Keep gaps explicit and specific.
- Do not include personal data beyond what the evaluation needs.
- Do not include CV text or cover-letter drafts.
