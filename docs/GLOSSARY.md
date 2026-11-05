# Glossary

Terms used across the package. Binding definitions live in the linked files.

## Baseline

The complete master CV built from all candidate documents. It is deliberately
long; tailoring selects and reorders from it. See
[`zj-baseline-cv/SKILL.md`](../zj-baseline-cv/SKILL.md).

## Fact base

The source-tagged inventory of roles, dates, responsibilities, achievements,
technologies, and evidence extracted before any CV text is written.

## Selection pool

Baseline-only material kept after the CV sections: headline options, full skills
list, company one-liners, quoted strengths, projects, courses, and reference
signatories. It is not part of the final CV.

## Source tag

A marker on a fact showing where it came from: third-party verified, credential,
self-reported only, or both. The default vocabulary is in
[`shared/evidence.md`](../shared/evidence.md).

## Confidence

A label on a number or date: exact, estimated, or approximate. It travels with
the claim into later documents.

## Open item

A fact, decision, or wording that still needs the candidate's confirmation. Open
items are listed, not hidden.

## Verification report

The baseline output that lists documents used, conflicts and resolutions,
single-source claims, and open items.

## Evidence pack

The approved set of claims, answers, keyword verdicts, gates, fit notes, trim
decisions, and open items produced by evaluation and consumed by tailoring.
Schema in [`shared/output.md`](../shared/output.md).

## Keyword map

The evaluation output that classifies posting terms as Green, Red, or Yellow and
records verifiability and proposed placement.

### Green

Specific technical terms, named methods, systems, certifications, and industry
vocabulary. Highest priority and must be verifiable.

### Red

General working style, communication, teamwork, and independence. Support only;
never displace Green.

### Yellow

Company values, leadership culture, work environment, and motivation language.
Cover letter only.

## Verifiability

For a Green term: yes, partially, or no. A "no" is a gap, not a reason to add the
term anyway.

## Gate

A pass, flag, or fail check based on user-supplied evidence, such as eligibility,
language, location, or travel. A gate is not a scoring dimension.

## Trim

Removing individual CV lines inside an included role. Line-level trims need the
evaluation's confirmed trim list.

## Role selection

Choosing, condensing, or omitting whole roles or sections during tailoring. It is
allowed, but it must be logged and confirmed. It is not a line-level trim.

## Fit report

The evaluation output with gates, keyword analysis, skills match, summary,
strengths, gaps, risks, interview likelihood, and recommendation.

## Match summary

The overall fit statement. It uses the user's scoring scheme when supplied;
otherwise it is qualitative and states its basis.

## Handoff

The defined transfer of the evidence pack and keyword map from evaluation to
tailoring. Tailoring stops if the handoff is missing or stale.

## Impact capture

The optional interview step that collects missing outcomes and confidence labels
before evaluation or baseline work.

## Change log

The tailoring output that records each edit: section, before, after, reason,
evidence, and confirmation status.

## Working draft

A generated document that the candidate has not approved as final. Every package
output starts as a working draft.

## Project overlay

A local file, outside the general package, that supplies project paths and
conventions. It may configure settings but must not weaken evidence rules or
gates.

## Support tier

The compatibility level for an agent: native skill discovery, rules-file
fallback, manual copy-paste, or unsupported. See
[`COMPATIBILITY.md`](COMPATIBILITY.md).

## Capability fallback

What to do when an agent lacks file reading, file writing, questions, network,
shell, or subagents. See [`shared/interaction.md`](../shared/interaction.md).

## Bundle

A generated single-file prompt built by `scripts/build_bundle.py` for agents
without skill discovery. Bundles are not committed.
