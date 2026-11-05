# Workflows

Status: complete. This page describes the end-to-end sequence and the decision
points between the three skills. The binding rules are in the skill files and
`shared/`.

## Choose a starting point

| Situation                                          | Start with                          |
| -------------------------------------------------- | ----------------------------------- |
| No baseline, or new documents to add               | `zj-baseline-cv`                    |
| A posting to assess                                | `zj-job-fit-evaluation`             |
| An approved evaluation and a request for documents | `zj-tailored-application`           |
| A task-based CV for contracting                    | `zj-baseline-cv` project conversion |

## Baseline flow

1. Confirm settings: working language, output language, spelling, template,
   target roles.
2. Collect CV versions, references, certificates, and optional project material.
3. Inventory and check readability. Stop on unreadable pages.
4. Build the tagged fact base.
5. Resolve conflicts and open questions.
6. Build or reconcile the skills list.
7. Write the baseline and selection pool.
8. Produce the verification report.
9. Optionally convert to a project-based CV and project list.

Output: baseline CV, skills list, verification report, open items.

## Evaluation flow

1. Confirm the posting and baseline exist.
2. Apply only the configured gates.
3. Optional impact capture.
4. Employment-gap review.
5. Green/Red/Yellow keyword analysis with verifiability.
6. Match table and summary with a stated basis.
7. Optional relevance trim, confirmed line by line.
8. Clarifying questions only if they block the report.
9. Fit, risk, interview likelihood, recommendation.
10. Optional salary note for the configured market.
11. Hand off the evidence pack and keyword map.

Output: fit report, evidence pack, keyword map, optional trim list, recommendation.

## Tailoring flow

1. Confirm the baseline, approved evidence pack, keyword map, and posting.
2. Select roles and sections; log and confirm whole-role selection.
3. Apply only confirmed line trims.
4. Write the contribution paragraph.
5. Write the profile bullets.
6. Integrate the target role into at most one bullet per role.
7. Enhance flagged impact bullets one at a time.
8. Write the cover letter.
9. Check every claim against the pack and write the change log.

Output: tailored CV, cover letter, change log, open items.

## Handoff

```text
zj-baseline-cv
  └─ baseline CV, skills list, verification report
       └─ zj-job-fit-evaluation
            └─ fit report, evidence pack, keyword map, trim list
                 └─ zj-tailored-application
                      └─ tailored CV, cover letter, change log
```

Tailoring without an approved evaluation is a stop condition. Re-run the
evaluation if the posting changed materially or the pack is stale.

## Standalone use

Each skill can run alone. If the evaluation is skipped, tailoring must say that
the evidence pack is missing and ask for an evaluation. If the baseline is
skipped, evaluation must use an equivalent evidence profile and state that the
baseline is not available.

## Fallbacks

- No file access: paste the skill, shared rules, and source documents.
- No file writing: return Markdown in the conversation.
- No interactive questions: state assumptions and open items.
- No network: skip web-dependent steps; the package does not require them.
