# Architecture and scope

Public description of how the three skills fit together, what each one produces,
and what the package deliberately does not do. Internal design notes are not part
of the package.

## Principles

- Generic by default: no candidate, employer, location, or workspace specifics.
- Evidence first: every claim traces to a document or an explicit answer.
- Configured, not hardcoded: language, spelling, salary market, template, and
  output format are settings.
- Human confirmation: the skills ask before trimming, rewriting, or stating a
  gap.
- No invented facts, numbers, dates, or outcomes.

## Skill contracts

### `zj-baseline-cv`

Builds or updates one complete baseline CV, a skills list, and a verification
report from all candidate documents. It also converts a task-based history into
project-based material.

Inputs: CV versions, reference letters and employment confirmations, diplomas
and certificates, optional skills list and project notes, template, output
language, spelling convention, and target roles.

Outputs: baseline CV, skills list, verification report, and an optional project
variant with a project list. Every factual item carries a source tag.

### `zj-job-fit-evaluation`

Evaluates one posting against the documented evidence. It produces a fit report,
an approved keyword map, and an evidence pack. It does not rewrite the CV or
write a cover letter.

Inputs: posting, baseline or evidence profile, optional preferences, and
optional gates for eligibility, language, location, travel, or other hard
constraints.

Outputs: fit report, evidence pack, keyword map, optional trim list, optional
salary note, gate results, and a recommendation. Weights and bands are
configuration, not package defaults.

### `zj-tailored-application`

Produces a tailored CV and cover letter for one posting from the baseline and the
approved evaluation. It does not re-evaluate the posting or invent evidence.

Inputs: baseline, approved evidence pack, approved keyword map, posting, optional
confirmed trim list, template, output language, and spelling convention.

Outputs: tailored CV, cover letter, change log, and open items. Role-level
selection is allowed but must be logged and confirmed; line-level trimming
requires the evaluation's confirmed list.

## Diagrams

### Components

```text
+-------------------+
| User or agent CLI |
+---------+---------+
          |
          | reads
          v
+-------------------+
| AGENTS.md router  |
+---------+---------+
          |
          | routes to one skill
          v
+--------------------------------------+
| SKILL.md + references/               |
| zj-baseline-cv | job-fit | tailored    |
+---------+----------------------------+
          |
          | reads
          v
+--------------------------------------+
| shared/ evidence interaction keywords|
| gates output style                   |
+---------+----------------------------+
          |
          | produces
          v
+--------------------------------------+
| CV | fit report | cover letter | log |
+--------------------------------------+
```

### Handoff

```text
source documents
       |
       v
+-------------+   baseline CV, skills list, verification report
| zj-baseline-cv | ------------------------------------------------+
+-------------+                                                 |
                                                                v
job posting + baseline evidence --> +--------------------+   fit report
                                     | zj-job-fit-evaluation |   evidence pack
                                     +----------+---------+   keyword map
                                                |
                                                v
                                     +----------------------+
                                     | zj-tailored-application |
                                     +----------+-----------+
                                                |
                                                v
                                     CV + cover letter + change log
```

### Decision path

```text
posting + evidence
        |
        v
    [ gates ] -- fail --> do not apply
        |
     pass or flag
        |
        v
keyword analysis --> match summary --> fit and risk --> recommendation
                                                              |
                                                         proceed
                                                              v
                                                          tailoring
```

A gate failure stops the application path. A flag stays in the report with a
visible warning.

## Shared rules

The skills reference one rule set in `shared/`:

- `evidence.md`: no-invention rule, source tags, confidence, conflicts, gaps.
- `interaction.md`: language, question protocol, impact capture, confirmations.
- `keywords.md`: Green, Red, and Yellow classification and verifiability.
- `gates.md`: entry gates, stop conditions, final checks.
- `output.md`: output order, document order, change log, handoff contract.
- `style.md`: CV, contribution, profile, cover-letter, and punctuation style.

A skill must link to the shared files it needs. Rules are edited once, not copied
into each skill.

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

Tailoring must not add claims outside this pack without asking the candidate. If
the pack is missing or stale, tailoring stops and requests an evaluation.

## Scope

In scope:

- evidence-based baseline CV building and updates;
- project-based CV conversion;
- posting evaluation, keyword analysis, and fit reports;
- tailored CVs and cover letters with a change log;
- configurable gates, weights, language, spelling, and salary market.

Out of scope:

- candidate identities, contact details, employment history, metrics, and
  documents;
- employer names, locations, target cities, commute rules, and market-specific
  deal-breakers;
- workspace folder layouts, file naming, canonical data stores, trackers, and
  state files;
- job-board scraping, portal CLIs, URL fetching, posting guards, and
  deduplication;
- application submission, email, ATS accounts, and recruiter outreach;
- company research, web research, and news monitoring;
- interview preparation, negotiation, and visa or immigration advice;
- PDF rendering engines, LaTeX, WeasyPrint, and layout implementation;
- automated translation beyond the output-language setting;
- scoring weights, verdict bands, and salary datasets that the user does not
  supply;
- legal, tax, and compliance advice.

What the package is not, the license, and the usage boundaries are in
[`BOUNDARIES.md`](BOUNDARIES.md).

## Support model

The skills are written for agent CLIs that can read repository instructions and
work with files. Capability requirements:

- read files and follow relative links;
- write a document or return it in the conversation;
- ask the user questions and wait for answers.

Optional capabilities improve the experience but are not required: shell access,
web fetch, subagents, and structured output. If a capability is missing, a skill
must say what it cannot do and offer a manual fallback instead of inventing
output.

The compatibility dimensions, support tiers, portable conventions, and agent
matrix are in [`COMPATIBILITY.md`](COMPATIBILITY.md). Installation paths and
fallbacks are in [`INSTALL.md`](INSTALL.md).
