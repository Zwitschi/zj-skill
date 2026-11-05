# Baseline phases

Detailed instructions for the `zj-baseline-cv` skill. Read the shared evidence,
interaction, gate, output, and style rules first. This file describes the
baseline-specific work only.

## Phase 0: Settings

Ask in one message:

- working language;
- output language, which may differ from the working language;
- spelling convention;
- CV template or layout description, or permission to use the clean fallback;
- one to three target role types;
- whether the candidate has an existing evidence-tag scheme.

Do not infer a country, market, spelling, or language from a document. Ask.

## Phase 1: Intake

Request the documents in one message, grouped as required and optional.

Required groups:

1. All CV versions, including older versions.
2. Reference letters, interim references, and employment confirmations.
3. Diplomas, transcripts, course certificates, and certification certificates.

Optional groups:

- existing skills list or matrix;
- cover letters, profile export, portfolio or repository links;
- existing project list or project notes.

State that unreadable documents must be replaced, not guessed around.

## Phase 2: Inventory and readability

Build a table with these columns:

| Document | Type | Date or version | Readable? |
| -------- | ---- | --------------- | --------- |

For each document, record whether it is fully readable, partly readable, or not
readable. If any part is not readable:

- name the exact file and the exact part;
- stop;
- ask for a better copy;
- continue only when the document is readable or the candidate explicitly
  accepts proceeding without it.

## Phase 3: Fact base

Extract facts before writing CV text. For each role, record:

- employer legal or trading name;
- location;
- all job titles used across the documents;
- start and end dates as stated in each source;
- responsibilities;
- achievements, with every number and metric exactly as stated;
- technologies, tools, and methods;
- source document and source tag for each item.

Merge rules:

- keep the most specific wording when versions overlap;
- keep facts that appear in only one version;
- do not average dates or metrics;
- do not rewrite a fact while extracting it.

Tag each item using the shared evidence vocabulary, or the candidate's existing
scheme mapped to it.

## Phase 4: Conflicts and questions

Check for:

- different dates for the same role, degree, or certificate;
- different titles for the same role;
- duplicate bullets that describe the same thing;
- skills or claims in only one document and not linked to a role or project;
- timeline gaps longer than three months;
- overlapping roles;
- roles that may be voluntary, freelance, or community work rather than
  employment.

Resolution order:

1. Official or third-party document wins over the candidate's own CV.
2. Reference letter title wins over a CV title.
3. If the conflict remains, keep both versions, flag the difference, and list it
   as an open item.

Then ask all open questions in one numbered message, at most ten. Examples:

- Where was this tool used?
- Which project evidences this skill?
- Was this role paid, voluntary, or freelance?
- Which date is correct?

Wait for answers. Anything unanswered stays in the fact base, tagged, and is
listed as an open item.

## Phase 5: Skills list

If a list exists, reconcile it with the fact base and note differences. If not,
build one.

Suggested categories:

- programming languages;
- frameworks and libraries;
- backend and integration;
- data and analytics;
- cloud and infrastructure;
- DevOps and quality;
- AI and automation;
- tools and platforms;
- domains and responsibilities;
- personal and working skills;
- languages.

For each skill record:

- skill name;
- level;
- evidence;
- candidate-only marker.

Use a 1 to 5 scale with written definitions. A high level needs at least one
piece of evidence. Rate conservatively.

## Phase 6: Build the baseline

Use the template from Phase 0. If the tool can edit the template, fill it and
preserve its styles. If not, output clean text in the same section order, ready
to paste.

### Personal data

Name, full address, phone, email, professional links, date of birth,
nationality, and work permit. Photo only if the template has a photo field.
Marital status only if the candidate provided it.

### Value proposition

Contribution paragraph:

- first person, prose, about six lines;
- opens with a variation of "with X years of experience in ...";
- states who I am, what I do, how I do it, and what results I achieve;
- includes two or three of the strongest verified results;
- no education list, no repetition of the profile.

Profile bullets:

- eight to twelve in the baseline;
- education, years of experience, core technical areas, strengths, community or
  awards, and languages;
- no results or value claims.

### Business experience

- reverse chronological;
- one line per role: dates, official title, employer, location;
- one flat bullet list per role;
- strongest impact first, then responsibilities from the reference letter;
- no subheadings inside a role;
- every bullet carries its tag in the working copy.

### Professional development

Courses and certifications, only if documented. Otherwise omit the section and
record an open item.

### Education

Years, qualification, institution, place. Specialisation and grade only if
documented.

### Languages

Each language with a common reference level or "mother tongue".

### Hobbies

Only if provided. Otherwise a placeholder note.

### References

"Upon request", unless the candidate asks for a different wording.

### Selection pool

After a page break, label it clearly as baseline-only and not part of the CV.
Include:

- headline options;
- availability, workload, permit validity, contract types;
- full skills keyword source;
- technologies per role;
- one-line company descriptions;
- projects, awards, hackathons, community work, talks;
- quoted strengths from reference letters, attributed;
- relevant courses;
- reference signatories and open contact details.

## Phase 7: Verification report

Produce a short report with:

1. Documents used and anything unreadable.
2. Conflicts and how they were resolved.
3. Claims supported only by the candidate's own materials, most important first.
4. Open items the candidate must complete.
5. A reminder that tailored CVs come from this baseline only, by selecting and
   reordering, never from a previously tailored copy.

## Phase 8: Updating a baseline

When a baseline exists:

1. Inventory new and changed documents.
2. Extract new facts and changes only.
3. Merge into the fact base without dropping single-source facts.
4. Re-run the conflict check.
5. Present a diff summary: new roles, changed dates, new certificates, new
   skills, removed claims, open items.
6. Ask before rewriting approved sections.
7. Re-run the verification report.
8. Keep the previous version and record the new version.

Never replace a baseline silently.

## Output format

- One output language throughout.
- Product and technology names unchanged.
- No page limit; completeness first.
- Dates: month/year for roles, years for education.
- Bullets: strong verb, past tense for past roles, present for the current role,
  one idea per bullet, result first where one exists.
- No em dashes; en dash only between dates.
- Apply the configured spelling convention.
