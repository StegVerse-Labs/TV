#!/usr/bin/env python3
import json, os, sys, csv, io, datetime
from pathlib import Path

# Optional dependency: reportlab for PDF
try:
    from reportlab.lib.pagesizes import LETTER
    from reportlab.pdfgen import canvas
    from reportlab.lib.units import inch
    HAVE_PDF = True
except Exception as e:
    HAVE_PDF = False

CHAINLOG = Path("data/summary/chainlog.jsonl")
REPORT_DIR = Path("reports")
REPORT_DIR.mkdir(parents=True, exist_ok=True)

now = datetime.datetime.utcnow()
year, week, _ = now.isocalendar()
stem = f"tv_audit_{year}-W{week:02d}"
csv_path = REPORT_DIR / f"{stem}.csv"
pdf_path = REPORT_DIR / f"{stem}.pdf"

entries = []
if CHAINLOG.exists():
    with CHAINLOG.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                entries.append(json.loads(line))
            except Exception:
                pass

# Basic stats
total = len(entries)
applies = sum(1 for e in entries if e.get("stage") == "apply")
verifies = sum(1 for e in entries if e.get("stage") == "verify")
last5 = entries[-5:] if total >= 5 else entries

# Write CSV snapshot
with csv_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["index","timestamp","stage","export_sha256","signature_kind","notes"])
    for i, e in enumerate(entries):
        w.writerow([i+1, e.get("timestamp",""), e.get("stage",""), e.get("export_sha256",""), e.get("signature_kind",""), e.get("notes","")])

print(f"Wrote CSV report to {csv_path}")

# Write PDF (if reportlab available)
if HAVE_PDF:
    c = canvas.Canvas(str(pdf_path), pagesize=LETTER)
    width, height = LETTER
    x_margin, y_margin = 0.75*inch, 0.75*inch
    y = height - y_margin

    def line(txt, dy=14):
        nonlocal y
        c.drawString(x_margin, y, txt)
        y -= dy

    c.setTitle(f"TV Weekly Audit Report {stem}")
    c.setFont("Helvetica-Bold", 16)
    line("StegVerse Token Vault — Weekly Audit Report")
    c.setFont("Helvetica", 10)
    line(f"Generated (UTC): {now.isoformat()}")
    line(f"Chainlog: {CHAINLOG}")
    line("")
    c.setFont("Helvetica-Bold", 12)
    line("Summary")
    c.setFont("Helvetica", 10)
    line(f"Total chainlog entries: {total}")
    line(f"Apply entries: {applies}")
    line(f"Verify entries: {verifies}")
    line("")

    c.setFont("Helvetica-Bold", 12)
    line("Most recent entries")
    c.setFont("Helvetica", 9)
    for e in last5[::-1]:
        line(f"- {e.get('timestamp','?')} | stage={e.get('stage','?')} | sha256={e.get('export_sha256','')[:12]}… | signed={e.get('signature_kind','')}")

    c.showPage()
    c.save()
    print(f"Wrote PDF report to {pdf_path}")
else:
    print("reportlab not available; PDF not generated. CSV still created.")

