# Contributing

Status: complete. Contributions must keep the package generic and evidence-based.

## Scope

- General, project-agnostic skills derived from the discovered prompt families.
- No candidate, employer, location, or workspace data.
- No scraping, portal integration, submission, company research, or interview
  preparation.
- No compatibility claim without a source and a test status.

## Edit the source, not generated output

- Edit `SKILL.md`, `shared/`, `docs/`, or `examples/`.
- Do not edit `dist/`. Rebuild it with `scripts/build_bundle.py`.
- Do not edit an installed copy in an agent's skill directory. Change the source
  and reinstall.

## Keep the rules single-sourced

- Put cross-skill rules in `shared/`.
- Link to the shared file instead of copying the rule into a skill.
- Put skill-specific detail in `references/`.
- Keep the skill body short enough for progressive disclosure.

## Checks

Before a change is accepted:

```bash
python3 scripts/check.py
python3 scripts/build_bundle.py
python3 -m py_compile scripts/build_bundle.py
npx prettier --check "**/*.md"   # if the workspace has Prettier
```

Also run:

- frontmatter validation for every `SKILL.md`;
- relative-link check, excluding generated `dist/`;
- leak scan with a private denylist;
- the fictional example contract check;
- the relevant agent smoke test, if a CLI is installed.

Do not commit `dist/`, local caches, or personal data.

## Versioning

- Follow semantic versioning.
- Update `VERSION` and `CHANGELOG.md`.
- Amend or create the release commit and tag only when the package is ready.
- Record tested agent versions and dates in `docs/COMPATIBILITY.md`.

## Style

- Markdown only.
- ASCII diagrams, not Mermaid-only.
- No em dashes. Use commas, colons, or a new sentence.
- No absolute paths in skill bodies.
- Use capability-neutral language, not agent-specific tool names.

## License

By contributing, you confirm that the contribution can be distributed under the
package's Personal Use License. Do not add third-party material with
incompatible terms.
