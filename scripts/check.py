#!/usr/bin/env python3
"""Lightweight public checks for the skill package.

Runs without secrets, personal data, or a private denylist:

* version and changelog sanity
* skill frontmatter
* relative links
* absolute paths, personal email addresses, and secret patterns
* tracked generated files
* example contract shape
* bundle generation

Usage:
    python3 scripts/check.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_NAMES = ("zj-baseline-cv", "zj-job-fit-evaluation", "zj-tailored-application")
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".txt", ""}
SKIP_DIRS = {".git", "dist", "__pycache__"}

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return files


def check_version() -> None:
    path = ROOT / "VERSION"
    if not path.is_file():
        fail("VERSION missing")
        return
    version = path.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail(f"VERSION is not semver: {version!r}")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if f"## [{version}]" not in changelog:
        fail(f"CHANGELOG has no section for {version}")


def check_skills() -> None:
    found = sorted(ROOT.glob("*/SKILL.md"))
    names = {path.parent.name for path in found}
    for name in SKILL_NAMES:
        if name not in names:
            fail(f"missing skill folder: {name}")
    for skill in found:
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            fail(f"{skill}: frontmatter must start on the first line")
            continue
        try:
            frontmatter = text.split("---\n", 2)[1]
        except IndexError:
            fail(f"{skill}: unterminated frontmatter")
            continue
        name_match = re.search(r"^name:\s*(\S+)\s*$", frontmatter, re.M)
        desc_match = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
        if not name_match:
            fail(f"{skill}: missing name")
        elif name_match.group(1) != skill.parent.name:
            fail(f"{skill}: name {name_match.group(1)!r} does not match folder")
        elif not name_match.group(1).startswith("zj-"):
            fail(f"{skill}: name must use the zj- prefix")
        if not desc_match:
            fail(f"{skill}: missing description")
        elif len(desc_match.group(1)) > 1024:
            fail(f"{skill}: description exceeds 1024 characters")


def check_links() -> None:
    pattern = re.compile(r"\]\(([^)]+)\)")
    for page in ROOT.rglob("*.md"):
        if "dist" in page.parts:
            continue
        for target in pattern.findall(page.read_text(encoding="utf-8")):
            if target.startswith(("http", "#", "mailto:")):
                continue
            path = target.split("#", 1)[0]
            if not (page.parent / path).exists():
                fail(f"{page}: broken link {target}")


def check_public_content() -> None:
    absolute = re.compile(r"(/home/|/Users/|/run/media/|(?<![A-Za-z0-9])[A-Za-z]:\\)")
    email = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
    secret = re.compile(
        r"(BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|"
        r"AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,})"
    )
    old_names = re.compile(
        r"(?<!zj-)\b(baseline-cv|job-fit-evaluation|tailored-application)\b"
    )
    this_file = Path(__file__).resolve()
    for path in text_files():
        if path.name == "LICENSE" or path.resolve() == this_file:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if absolute.search(text):
            fail(f"{path}: absolute path")
        for match in email.finditer(text):
            if not match.group(0).endswith("@example.test"):
                fail(f"{path}: non-example email address")
        if secret.search(text):
            fail(f"{path}: possible secret")
        if old_names.search(text):
            fail(f"{path}: old skill name without zj- prefix")
    if (ROOT / "DESIGN.md").exists():
        fail("DESIGN.md must stay out of the public package")
    for path in ROOT.rglob("*"):
        if path.is_file() and path.stat().st_size > 1_000_000:
            fail(f"{path}: file larger than 1 MB")


def check_tracked() -> None:
    if not (ROOT / ".git").exists():
        return
    result = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=False
    )
    if result.returncode != 0:
        fail("git ls-files failed")
        return
    for line in result.stdout.splitlines():
        if line.startswith("dist/"):
            fail(f"generated file is tracked: {line}")
        if line == "DESIGN.md":
            fail("DESIGN.md is tracked")
    if "private-denylist" in result.stdout:
        fail("private denylist is tracked")


def check_examples() -> None:
    baseline = (ROOT / "examples/zj-baseline-cv/expected-output.md").read_text(
        encoding="utf-8"
    )
    tailored = (
        ROOT / "examples/zj-tailored-application/expected-output.md"
    ).read_text(encoding="utf-8")
    section = baseline.split("### Business experience")[1].split(
        "### Professional development"
    )[0]
    bullets = [line for line in section.splitlines() if line.startswith("- ")]
    if not bullets:
        fail("baseline example has no experience bullets")
    for bullet in bullets:
        if not re.search(r"`\[[^\]]+\]`$", bullet.strip()):
            fail(f"baseline example bullet has no source tag: {bullet[:60]}")
    for number in ("18%", "10 hours", "12%", "3%", "eight", "120"):
        if number.lower() not in tailored.lower():
            fail(f"tailored example is missing {number}")
    for name, text in (("baseline", baseline), ("tailored", tailored)):
        if "\u2014" in text:
            fail(f"{name} example contains an em dash")


def check_bundles() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/build_bundle.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        fail(f"bundle build failed: {result.stderr.strip()[:200]}")
        return
    for name in SKILL_NAMES:
        bundle = ROOT / "dist" / f"{name}.md"
        if not bundle.is_file() or bundle.stat().st_size == 0:
            fail(f"missing bundle: {bundle}")


def main() -> int:
    check_version()
    check_skills()
    check_links()
    check_public_content()
    check_tracked()
    check_examples()
    check_bundles()
    if errors:
        print("Checks failed:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print("All public checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
