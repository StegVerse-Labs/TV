#!/usr/bin/env python3
# Legacy script kept for compatibility; prefer scripts/tv_badge_update.py
import os, json
from pathlib import Path
from datetime import datetime, timezone

REPORTS_DIR = Path("reports")
DOCS_DIR = Path("docs")
OUT_SVG = DOCS_DIR / "tv_status.svg"

def main():
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    OUT_SVG.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="160" height="20" role="img" aria-label="TV Audit: stale"><rect width="68" height="20" fill="#555"/><rect x="68" width="92" height="20" fill="#dfb317"/><g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11"><text x="34" y="14">TV Audit</text><text x="114" y="14">stale</text></g></svg>', encoding="utf-8")
    print(f"Wrote legacy badge to {OUT_SVG}")

if __name__ == "__main__":
    main()
