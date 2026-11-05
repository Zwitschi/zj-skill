# Interaction protocol

How the skills ask questions, confirm decisions, and handle language. Apply this
protocol in every phase unless a skill explicitly says otherwise.

## Language

1. Ask which working language to use before producing output. Offer one
   language or bilingual output.
2. Ask for the output language of each document separately when it can differ
   from the working language.
3. Translate source documents faithfully. Do not improve, summarise, or embellish
   while translating.
4. Keep product and technology names unchanged.
5. Treat spelling convention as a setting. Do not hardcode one country's
   spelling.

The bilingual Word copies in the source material add one rule: ask the working
language, then follow only that language edition and ignore the other. Apply the
same discipline to any bilingual source.

## Question protocol

When a step needs more than one question:

1. State the total number of questions before the first one.
2. Ask one question at a time.
3. Wait for an answer or an explicit skip before the next question.
4. Allow the candidate to skip any question.
5. Do not infer completion, agreement, or a fact from silence.

Exception: a conflict or open-items review may be presented as one numbered
batch of at most ten questions when the skill explicitly calls for it.

## Impact capture

Use impact capture only where the evidence lacks a measurable or inferable
outcome.

- Ask up to five questions per role.
- Skip roles that already contain a clear, quantified outcome.
- Cover these dimensions:
  - scale: team size, budget, volume, user base, vendor count, system count;
  - before and after: what changed, even approximately;
  - timeframe: over what period;
  - method: which approach, framework, or tool drove the change;
  - confidence: is the figure exact, estimated, or approximate.
- Record a skip as a skip. Do not fill it later.
- Never ask again for a figure that is already captured and tagged.

## Gap analysis

- Scan the timeline for gaps of three months or more, including before the first
  role when a start or education date is visible.
- Ask what happened. Do not guess or infer a reason.
- Classify the answer in the candidate's own words.
- Offer one concrete handling option at a time: a short factual CV line,
  month-level dates, a cover-letter mention, or no action.
- Never state a gap in a document without the candidate's explicit confirmation
  of the wording.
- Record the confirmed decisions in a short table.

## Confirmation gates

Ask before any of these actions:

- removing or trimming a CV line;
- rewriting a bullet with a new outcome;
- stating an employment gap;
- adapting an experience bullet for a target role;
- adding a salary expectation to a document;
- moving from one role to the next in a project interview;
- treating a working draft as final.

Default when the candidate does not answer a trim question: keep the line. Never
trim silently.

## Capability fallback

Use the equivalent capability the agent has. Do not require a named tool.

- No file reading: ask the user to paste the referenced files or the relevant
  sections.
- No file writing: return the documents in the conversation as Markdown and mark
  them as drafts.
- No interactive questions: state the assumptions and list the open items
  instead of guessing.
- No network, shell, or subagents: continue without them. Do not invent the
  result they would have produced.
- Unsupported frontmatter or discovery: fall back to reading the `SKILL.md` body
  directly or to the manual prompt bundle.
