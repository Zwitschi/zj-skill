# FAQ

Status: complete.

## Is this open source?

No. The package uses a Personal Use License: personal, private, non-commercial
use only, with no redistribution or derivative works. See
[`BOUNDARIES.md`](BOUNDARIES.md) and [`../LICENSE`](../LICENSE).

## Does it work with Claude Code, Codex, Pi, and other agents?

See [`COMPATIBILITY.md`](COMPATIBILITY.md). Native skill discovery is supported
by Claude Code, Codex, Hermes, Pi, Gemini, Cursor, Windsurf/Devin Local, Cline,
OpenHands, and Goose. Aider uses the rules-file fallback.

## Does it store or send my CV?

The package contains no candidate data and no telemetry. Inputs stay in the files
and conversation you provide. Your agent provider may process the conversation
according to its own terms.

## Can it submit applications?

No. It produces documents and reports. Submission, email, and recruiter outreach
are out of scope and require explicit approval outside the skills.

## Does it invent experience or metrics?

No. Every claim must trace to a document or an explicit answer. Missing evidence
is named as a gap.

## Does it decide whether I should apply?

It produces a fit report and a recommendation. The decision stays with you.

## Why three skills instead of one?

The source prompt combines evaluation and tailoring. Splitting them keeps the
evidence and keyword decisions explicit, and lets each skill run alone.

## Can I use my own CV template?

Yes. A template or layout description is a setting.

## Can I write in German, English, or both?

Yes. Working language, output language, and spelling convention are settings.

## Where do I install it?

The broadest project path is `.agents/skills/`. Per-agent paths are in
[`INSTALL.md`](INSTALL.md).

## How do I update?

Replace the skill folders, `shared/`, and `examples/` with the new release. Keep
local overlays outside the package.

## Can I use it commercially?

No. The license limits use to personal, private, non-commercial purposes.

## Can I contribute?

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Contributions must stay generic and
must not include personal data.
