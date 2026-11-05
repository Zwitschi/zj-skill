# Configuration

Settings are supplied by the user in conversation or by a local project overlay.
The package is instruction-only: it does not parse a configuration file. A
setting is never hardcoded.

## Where settings come from

1. Explicit user instruction for the current task.
2. The skill's stated setting placeholders.
3. Shared defaults.

A local project overlay may supply paths and configuration. It must not weaken
evidence rules, gates, or confirmation requirements.

## Settings

| Setting               | Used by             | Required when                   | Default                | Example                           |
| --------------------- | ------------------- | ------------------------------- | ---------------------- | --------------------------------- |
| Working language      | All                 | Always                          | Ask                    | `English`                         |
| Output language       | All                 | Always                          | Ask                    | `German`                          |
| Cover-letter language | Tailoring           | If different from CV            | CV language            | `English`                         |
| Spelling convention   | Baseline, tailoring | Always                          | Ask                    | `UK`, `US`, or another convention |
| CV template           | Baseline, tailoring | Always                          | Clean fallback         | `<path or layout description>`    |
| Target roles          | Baseline            | Always                          | Ask                    | One to three role types           |
| Evidence tags         | Baseline            | Always                          | Shared defaults        | Map an existing scheme            |
| Eligibility rule      | Evaluation          | If the user has one             | None                   | `EU work authorisation`           |
| Language rule         | Evaluation          | Always                          | Declared levels        | `German B2`, `English C1`         |
| Location rule         | Evaluation          | If the user has one             | None                   | `Commute area or remote`          |
| Travel rule           | Evaluation          | If the user has one             | None                   | `Occasional travel allowed`       |
| Scoring scheme        | Evaluation          | If the user has one             | Qualitative            | Weights and bands                 |
| Salary market         | Evaluation          | If salary guidance is requested | None                   | `<country or region>`             |
| Salary currency       | Evaluation          | With salary market              | None                   | `<currency>`                      |
| Trim review           | Evaluation          | If line trims are wanted        | Off                    | `on`                              |
| Output format         | All                 | Always                          | Markdown               | `Markdown`, `docx`, or template   |
| Document order        | Tailoring           | If not default                  | CV, letter, change log | CV, letter, log                   |

## Language

- Ask for the working language before producing output.
- Ask for each document's output language separately. CV and cover letter may
  differ.
- Translate source documents faithfully. Do not summarise or embellish while
  translating.
- Keep product and technology names unchanged.
- One language per document unless bilingual output was requested.

## Spelling

- Treat spelling as a setting: US, UK, another convention, or a named house
  style.
- Apply it consistently across the document.
- Do not infer a country from a name, address, or employer.

## Salary market

- Produce salary guidance only when the user requests it and supplies a market
  and currency.
- Give a range, state the basis, and state the uncertainty.
- Do not import a benchmark dataset or invent a precise offer.
- If the posting and profile do not support a range, say so and omit it.

## Gates

A gate is pass, flag, or fail with quoted evidence. Do not invent one.

| Gate        | Pass                                                            | Flag                                           | Fail                                                       |
| ----------- | --------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------- |
| Eligibility | Explicit acceptance, or the candidate meets a named requirement | Posting is silent and the rule is unverified   | Posting names a requirement the candidate does not meet    |
| Language    | Requirement at or below the declared level                      | Requirement plausibly above the declared level | Required language is absent from the profile               |
| Location    | Within the user's commute or remote rule                        | Borderline, hybrid, or travel-heavy            | Relocation required, or outside the rule                   |
| Travel      | Within the user's limit                                         | Occasional travel with no stated limit         | The user made frequent travel or relocation a deal-breaker |
| Other       | Meets the user-defined constraint                               | Needs clarification                            | Contradicts the constraint                                 |

Silence in a posting is not permission. Mark it unverified and say what needs
checking.

## Scoring

If the user supplies weights and bands:

- state the weights;
- show the per-dimension values and the arithmetic;
- map the total to the supplied bands.

If not, use a qualitative summary and state the basis. Do not import weights,
bands, or a score from another framework.

## Evidence tags

| Default tag         | Meaning                                            |
| ------------------- | -------------------------------------------------- |
| `[VERIFIED]`        | Confirmed by a third-party document                |
| `[CREDENTIAL]`      | Confirmed by a diploma, transcript, or certificate |
| `[SELF]`            | Stated only in the candidate's own materials       |
| `[VERIFIED / SELF]` | Stated in both                                     |

Map an existing tag scheme to these meanings. Keep the tag in the working copy;
remove it only when producing a final submission copy.

Confidence labels for numbers and dates:

- exact;
- estimated;
- approximate.

## Template and output

- A template is a file or a layout description. If none is supplied, use a clean
  Markdown layout.
- Do not edit the original template. Fill a copy or produce a new document.
- Output format is Markdown by default. A user may request a template format or a
  rendered document.
- Document order: tailored CV, cover letter, change log, open items. The user may
  change it.
- Output paths are supplied by the user or a project overlay. Skill bodies must
  not contain absolute paths.

## Example setup

Illustrative only. There is no parser; put these values in the conversation or a
project overlay.

```yaml
working_language: English
output_language: English
cover_letter_language: English
spelling: UK
template: <path or layout description>
target_roles:
  - <role type>
  - <role type>
evidence_tags: default
gates:
  eligibility: <rule or none>
  language: <declared levels>
  location: <commute or remote rule>
  travel: <rule or none>
scoring: qualitative
salary_market: null
salary_currency: null
trim_review: false
output_format: markdown
document_order:
  - cv
  - cover_letter
  - change_log
```

## Validation

- Missing required setting: ask before producing output.
- Unknown or invalid value: explain the valid range and ask again.
- Unset optional setting: omit the feature and say so.
- Never assume a country, city, language, currency, or spelling convention.
- Never weaken a gate because a setting is missing.

## What not to configure

- Do not configure the package to invent facts.
- Do not disable confirmation gates silently.
- Do not set a location list the user has not approved.
- Do not put personal data, secrets, or private URLs in a public configuration or
  example.
