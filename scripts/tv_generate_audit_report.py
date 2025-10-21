#!/usr/bin/env python3
import argparse, json, csv, os, sys
from datetime import datetime, timezone
from pathlib import Path

def load_chainlog(path):
    entries = []
    if not Path(path).exists():
        return entries
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except Exception:
                # tolerate corrupt lines but continue
                continue
    return entries

def summarize(entries):
    out = {
        "total_entries": len(entries),
        "apply": 0,
        "verify": 0,
        "status_ok": 0,
        "status_fail": 0,
        "sig_sigstore": 0,
        "sig_hmac": 0,
        "first_ts": None,
        "last_ts": None,
    }
    for e in entries:
        action = e.get("action") or e.get("event") or ""
        status = (e.get("status") or "").lower()
        sigtype = (e.get("signature_type") or e.get("sig_type") or "").lower()
        ts = e.get("timestamp") or e.get("time") or None
        if action == "apply":
            out["apply"] += 1
        if action == "verify":
            out["verify"] += 1
        if status in ("ok","success","passed","valid","verified"):
            out["status_ok"] += 1
        elif status:
            out["status_fail"] += 1
        if sigtype == "sigstore":
            out["sig_sigstore"] += 1
        elif sigtype == "hmac":
            out["sig_hmac"] += 1
        if ts:
            try:
                dt = datetime.fromisoformat(ts.replace("Z","+00:00"))
            except Exception:
                dt = None
            if dt:
                if out["first_ts"] is None or dt < out["first_ts"]:
                    out["first_ts"] = dt
                if out["last_ts"] is None or dt > out["last_ts"]:
                    out["last_ts"] = dt
    # Render timestamps as ISO
    if out["first_ts"]: out["first_ts"] = out["first_ts"].astimezone(timezone.utc).isoformat()
    if out["last_ts"]: out["last_ts"] = out["last_ts"].astimezone(timezone.utc).isoformat()
    return out

def write_csv(summary, mode, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    now = datetime.now(timezone.utc)
    if mode == "daily":
        stamp = now.strftime("%Y%m%d")
        filename = f"tv_audit_daily_{stamp}.csv"
    else:
        stamp = f"{now.year}-{now.strftime('%W')}"
        filename = f"tv_audit_{stamp}.csv"
    out_path = Path(out_dir) / filename
    # flat CSV
    fields = ["period","total_entries","apply","verify","status_ok","status_fail","sig_sigstore","sig_hmac","first_ts","last_ts"]
    row = {
        "period": filename.replace(".csv",""),
        **summary
    }
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerow(row)
    return str(out_path)

def write_pdf(summary, csv_path, out_dir):
    # optional PDF if reportlab is available
    try:
        from reportlab.lib.pagesizes import LETTER
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import inch
    except Exception:
        return None
    os.makedirs(out_dir, exist_ok=True)
    pdf_path = Path(out_dir) / (Path(csv_path).stem + ".pdf")
    c = canvas.Canvas(str(pdf_path), pagesize=LETTER)
    width, height = LETTER
    y = height - 1*inch
    c.setFont("Helvetica-Bold", 14)
    c.drawString(1*inch, y, "StegVerse Token Vault — Audit Report")
    y -= 0.4*inch
    c.setFont("Helvetica", 11)
    for k in ["total_entries","apply","verify","status_ok","status_fail","sig_sigstore","sig_hmac","first_ts","last_ts"]:
        c.drawString(1*inch, y, f"{k}: {summary.get(k)}")
        y -= 0.25*inch
    c.drawString(1*inch, y, f"CSV: {os.path.basename(csv_path)}")
    c.showPage()
    c.save()
    return str(pdf_path)

def write_summary_json(summary, csv_path, pdf_path, out_dir):
    path = Path(out_dir) / (Path(csv_path).stem + "_summary.json")
    data = {
        "csv": os.path.basename(csv_path),
        "pdf": os.path.basename(pdf_path) if pdf_path else None,
        **summary
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return str(path)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chainlog", default="data/summary/chainlog.jsonl")
    ap.add_argument("--out_dir", default="reports")
    ap.add_argument("--mode", choices=["weekly","daily"], default="weekly")
    ap.add_argument("--no_pdf", action="store_true")
    args = ap.parse_args()

    entries = load_chainlog(args.chainlog)
    summary = summarize(entries)
    csv_path = write_csv(summary, args.mode, args.out_dir)
    pdf_path = None
    if not args.no_pdf:
        pdf_path = write_pdf(summary, csv_path, args.out_dir)
    summary_path = write_summary_json(summary, csv_path, pdf_path, args.out_dir)
    print(json.dumps({"csv": csv_path, "pdf": pdf_path, "summary": summary_path, **summary}, indent=2))

if __name__ == "__main__":
    main()
