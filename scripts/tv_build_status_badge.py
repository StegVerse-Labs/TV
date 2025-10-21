#!/usr/bin/env python3
import os, glob, json, time
from pathlib import Path
from datetime import datetime, timezone, timedelta

REPORTS_DIR = Path("reports")
OUT_SVG = Path("docs/tv_status.svg")
STALE_AFTER_DAYS = int(os.getenv("TV_STATUS_STALE_DAYS", "2"))

def find_latest_summary():
    if not REPORTS_DIR.exists():
        return None, None
    summaries = sorted(REPORTS_DIR.glob("*_summary.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not summaries:
        return None, None
    latest = summaries[0]
    try:
        data = json.loads(latest.read_text(encoding="utf-8"))
    except Exception:
        data = {}
    return latest, data

def pick_status(data):
    now = datetime.now(timezone.utc)
    last_ts = data.get("last_ts")
    if last_ts:
        try:
            last_dt = datetime.fromisoformat(last_ts.replace("Z","+00:00"))
        except Exception:
            last_dt = None
    else:
        last_dt = None

    stale_cutoff = now - timedelta(days=STALE_AFTER_DAYS)
    is_stale = True
    if last_dt:
        is_stale = last_dt < stale_cutoff

    total = int(data.get("total_entries") or 0)
    ok = int(data.get("status_ok") or 0)
    fail = int(data.get("status_fail") or 0)

    if total == 0:
        label = "stale"
        color = "#9f9f9f"
        message = "No chainlog entries"
    elif fail > 0:
        label = "attention"
        color = "#E05D44"
        message = f"Fail {fail} / OK {ok}"
    elif is_stale:
        label = "stale"
        color = "#dfb317"
        message = "Audit stale"
    else:
        label = "passing"
        color = "#4c1"
        message = f"OK {ok}"

    ts_label = data.get("last_ts") or "n/a"
    return label, color, message, ts_label

def build_svg(label, color, message, ts_label):
    left_text = "TV Audit"
    right_text = f"{label}"
    width_left = 68
    width_right = max(90, 8 * len(right_text))
    total_w = width_left + width_right
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="20" role="img" aria-label="{left_text}: {right_text}">
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="m">
    <rect width="{total_w}" height="20" rx="3" fill="#fff"/>
  </mask>
  <g mask="url(#m)">
    <rect width="{width_left}" height="20" fill="#555"/>
    <rect x="{width_left}" width="{width_right}" height="20" fill="{color}"/>
    <rect width="{total_w}" height="20" fill="url(#s)"/>
  </g>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
    <text x="{width_left/2}" y="15" fill="#010101" fill-opacity=".3">{left_text}</text>
    <text x="{width_left/2}" y="14">{left_text}</text>
    <text x="{width_left + width_right/2}" y="15" fill="#010101" fill-opacity=".3">{right_text}</text>
    <text x="{width_left + width_right/2}" y="14">{right_text}</text>
  </g>
  <!-- meta: {message} | last={ts_label} -->
</svg>'''
    return svg

def main():
    OUT_SVG.parent.mkdir(parents=True, exist_ok=True)
    latest_path, data = find_latest_summary()
    if not data:
        data = {}
    label, color, message, ts_label = pick_status(data)
    svg = build_svg(label, color, message, ts_label)
    OUT_SVG.write_text(svg, encoding="utf-8")
    print(f"Wrote {OUT_SVG} (label={label}, message={message}, last={ts_label})")

if __name__ == "__main__":
    main()
