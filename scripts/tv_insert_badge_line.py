#!/usr/bin/env python3
import re
from pathlib import Path

README_PATH = Path("README.md")
BADGE_LINE = "![TV Audit Status](docs/tv_status.svg)\n"

def main():
    if not README_PATH.exists():
        print("README.md not found at repo root.")
        return

    text = README_PATH.read_text(encoding="utf-8")
    if "TV Audit Status" in text:
        print("Badge line already present; no change.")
        return

    # Insert below first H1 or at top if none
    lines = text.splitlines(keepends=True)
    new_lines = []
    inserted = False
    for line in lines:
        new_lines.append(line)
        if not inserted and re.match(r"^# ", line):
            new_lines.append(BADGE_LINE)
            inserted = True
    if not inserted:
        new_lines.insert(0, BADGE_LINE)

    README_PATH.write_text("".join(new_lines), encoding="utf-8")
    print("Inserted badge line into README.md")

if __name__ == "__main__":
    main()
