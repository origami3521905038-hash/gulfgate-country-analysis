#!/usr/bin/env python3
"""Offline release checks for the GulfGate country-analysis skill."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


def check_frontmatter() -> str:
    text = SKILL.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise AssertionError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise AssertionError("SKILL.md frontmatter is not closed")
    frontmatter = text[4:end]
    name = re.search(r"^name:\s*(\S+)\s*$", frontmatter, re.MULTILINE)
    description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
    if not name or name.group(1) != "gulfgate-country-analysis":
        raise AssertionError("unexpected skill name")
    if not description or len(description.group(1).strip()) < 80:
        raise AssertionError("description is missing or too short")
    return name.group(1)


def check_links() -> int:
    checked = 0
    missing: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".txt", ".html"}:
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            checked += 1
            if not (path.parent / target).resolve().exists():
                missing.append(f"{path.relative_to(ROOT)} -> {target}")
    if missing:
        raise AssertionError("broken local links:\n" + "\n".join(missing))
    return checked


def check_data() -> tuple[int, int]:
    records_path = ROOT / "references/knowledge/records.jsonl"
    records = [
        json.loads(line)
        for line in records_path.read_text(encoding="utf-8-sig").splitlines()
        if line.strip()
    ]
    terms_path = ROOT / "assets/terms.csv"
    term_lines = sum(1 for line in terms_path.read_text(encoding="utf-8-sig").splitlines() if line)
    if len(records) < 500:
        raise AssertionError("structured record set is unexpectedly small")
    if term_lines < 1_500:
        raise AssertionError("term set is unexpectedly small")
    return len(records), term_lines - 1


def check_lookup() -> int:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/lookup.py"), "record", "C-AE-M2-01", "--limit", "1"],
        check=True,
        capture_output=True,
        text=True,
    )
    payload = json.loads(result.stdout)
    if payload.get("matches") != 1:
        raise AssertionError("record lookup smoke test failed")
    return payload["returned"]


def main() -> None:
    name = check_frontmatter()
    links = check_links()
    records, terms = check_data()
    returned = check_lookup()
    print(
        json.dumps(
            {
                "status": "passed",
                "skill": name,
                "local_links": links,
                "structured_records": records,
                "terms": terms,
                "lookup_results": returned,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

