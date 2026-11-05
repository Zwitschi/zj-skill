#!/usr/bin/env python3
"""Build single-file prompt bundles for agents without skill discovery.

Each bundle contains the skill body, its references, and the shared rules, so a
chat-only agent or a rules-file agent can use the workflow from one pasted file.

Usage:
    python3 scripts/build_bundle.py
    python3 scripts/build_bundle.py --skill zj-baseline-cv
    python3 scripts/build_bundle.py --skill zj-job-fit-evaluation --skill zj-tailored-application

Bundles are written to dist/ and are intentionally not committed. Edit the
source files, then rebuild.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED_FILES = (
    "shared/evidence.md",
    "shared/interaction.md",
    "shared/keywords.md",
    "shared/gates.md",
    "shared/output.md",
    "shared/style.md",
)
SKILL_FILES = {
    "zj-baseline-cv": (
        "zj-baseline-cv/SKILL.md",
        "zj-baseline-cv/references/baseline-phases.md",
        "zj-baseline-cv/references/project-conversion.md",
    ),
    "zj-job-fit-evaluation": (
        "zj-job-fit-evaluation/SKILL.md",
        "zj-job-fit-evaluation/references/evaluation-workflow.md",
        "zj-job-fit-evaluation/references/fit-report-template.md",
    ),
    "zj-tailored-application": (
        "zj-tailored-application/SKILL.md",
        "zj-tailored-application/references/tailoring-workflow.md",
        "zj-tailored-application/references/document-patterns.md",
    ),
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8").rstrip() + "\n"


def version() -> str:
    try:
        return (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    except OSError:
        return "unknown"


def build(skill: str) -> str:
    files = list(SKILL_FILES[skill]) + list(SHARED_FILES)
    title = f"# Job Application Skills Bundle: {skill}"
    parts = [
        title,
        "",
        f"Generated from `skills-public` version {version()}.",
        "Do not edit this bundle. Edit the source files and rebuild it.",
        "Relative links in the sections below point to source files; the content",
        "is included in this bundle, so the links are informational only.",
        "",
        "## Contents",
        "",
    ]
    for path in files:
        parts.append(f"- `{path}`")
    parts.append("")
    for path in files:
        parts.extend(
            [
                "---",
                "",
                f"<!-- source: {path} -->",
                "",
                read(path),
            ]
        )
    return "\n".join(parts).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skill",
        action="append",
        choices=sorted(SKILL_FILES),
        help="Skill to bundle; repeatable. Defaults to all three.",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=ROOT / "dist",
        help="Output directory (default: dist/)",
    )
    args = parser.parse_args()

    skills = args.skill or list(SKILL_FILES)
    args.outdir.mkdir(parents=True, exist_ok=True)
    for skill in skills:
        target = args.outdir / f"{skill}.md"
        content = build(skill)
        target.write_text(content, encoding="utf-8")
        print(f"{target.relative_to(ROOT)}  {len(content):,} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
