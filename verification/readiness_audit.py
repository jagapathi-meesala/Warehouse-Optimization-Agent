"""Repository readiness and explainability audit."""
from __future__ import annotations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = ["agent.yaml","SOUL.md","README.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md",".env.example",".gitignore","requirements.txt","pytest.ini"]
REQUIRED_DIRS = ["adapters","config","contracts","core","skills","tools","tests","verification"]
HEADINGS = ["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]
BAD = ["## Inputs","## Decision","## Limits"]

def section(text: str, heading: str) -> str:
    start = text.index(heading) + len(heading)
    rest = text[start:]
    next_heading = re.search(r"\n## ", rest)
    return rest[:next_heading.start()] if next_heading else rest

def main() -> int:
    errors=[]
    for f in REQUIRED_FILES:
        if not (ROOT/f).is_file(): errors.append(f"missing file: {f}")
    for d in REQUIRED_DIRS:
        if not (ROOT/d).is_dir(): errors.append(f"missing directory: {d}")
    exp=(ROOT/"EXPLAINABILITY.md").read_text(encoding="utf-8") if (ROOT/"EXPLAINABILITY.md").exists() else ""
    for h in HEADINGS:
        if exp.count(h) != 1: errors.append(f"heading count must be 1: {h}")
        elif len([s for s in re.split(r"(?<=[.!?])\s+", section(exp,h).strip()) if s]) < 2: errors.append(f"section needs two sentences: {h}")
    for h in BAD:
        if re.search(rf"^{re.escape(h)}$", exp, re.MULTILINE): errors.append(f"conflicting heading: {h}")
    if errors:
        print("READINESS: FAIL")
        print("\n".join(f"- {e}" for e in errors)); return 1
    print("READINESS: PASS")
    print(f"Checked {len(REQUIRED_FILES)} required files and {len(REQUIRED_DIRS)} required directories.")
    return 0

if __name__ == "__main__": raise SystemExit(main())
