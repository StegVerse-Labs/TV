#!/usr/bin/env python3
import os, json, hmac, hashlib
from pathlib import Path
from datetime import datetime, timezone, timedelta

REPORTS_DIR = Path("reports")
DOCS_DIR = Path("docs")
BADGE_PATH = DOCS_DIR / "tv_status.svg"
SIG_PATH = DOCS_DIR / "tv_status.svg.sig"
META_PATH = DOCS_DIR / "tv_status.meta.json"

STALE_AFTER_DAYS = int(os.getenv("TV_STATUS_STALE_DAYS", "2"))
HMAC_KEY_ENV = "TV_BADGE_HMAC_KEY"

def latest_summary():
    if not REPORTS_DIR.exists():
        return None, None
    summaries = sorted(REPORTS_DIR.glob("*_summary.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not summaries: return None, None
    p = summaries[0]
    try: data = json.loads(p.read_text(encoding="utf-8"))
    except Exception: data = {}
    return p, data

def pick_status(data):
    now = datetime.now(timezone.utc)
    total = int(data.get("total_entries") or 0); ok = int(data.get("status_ok") or 0); fail = int(data.get("status_fail") or 0)
    last_ts = data.get("last_ts"); last_dt = None
    if last_ts:
        try: last_dt = datetime.fromisoformat(last_ts.replace("Z","+00:00"))
        except Exception: last_dt = None
    stale = True
    if last_dt: stale = last_dt < (now - timedelta(days=STALE_AFTER_DAYS))
    if total == 0: return "stale","#9f9f9f","no-data", last_ts or "n/a"
    if fail > 0:  return "attention","#E05D44",f"fail {fail}", last_ts or "n/a"
    if stale:     return "stale","#dfb317","stale", last_ts or "n/a"
    return "passing","#4c1",f"ok {ok}", last_ts or "n/a"

def build_svg(label, color, _msg, ts_label):
    left_text = "TV Audit"; right_text = f"{label}"
    width_left = 68; width_right = max(90, 8 * len(right_text)); total_w = width_left + width_right
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="20" role="img" aria-label="{left_text}: {right_text}">
  <linearGradient id="s" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient>
  <mask id="m"><rect width="{total_w}" height="20" rx="3" fill="#fff"/></mask>
  <g mask="url(#m)"><rect width="{width_left}" height="20" fill="#555"/><rect x="{width_left}" width="{width_right}" height="20" fill="{color}"/><rect width="{total_w}" height="20" fill="url(#s)"/></g>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
    <text x="{width_left/2}" y="15" fill="#010101" fill-opacity=".3">{left_text}</text><text x="{width_left/2}" y="14">{left_text}</text>
    <text x="{width_left + width_right/2}" y="15" fill="#010101" fill-opacity=".3">{right_text}</text><text x="{width_left + width_right/2}" y="14">{right_text}</text>
  </g>
  <!-- meta: last={ts_label} -->
</svg>'''

def main():
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    p, data = latest_summary(); 
    if not data: data = {}
    label, color, msg, ts_label = pick_status(data)
    svg = build_svg(label, color, msg, ts_label); BADGE_PATH.write_text(svg, encoding="utf-8")
    meta = {"generated_at": datetime.now(timezone.utc).isoformat(),"label": label,"message": msg,"last_ts": ts_label,"stale_after_days": STALE_AFTER_DAYS}
    META_PATH.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    key = os.getenv(HMAC_KEY_ENV, "").strip()
    if key:
        try: key_bytes = bytes.fromhex(key)
        except ValueError: key_bytes = key.encode("utf-8")
        sig = hmac.new(key_bytes, BADGE_PATH.read_bytes(), hashlib.sha256).hexdigest()
        SIG_PATH.write_text(sig + "\n", encoding="utf-8")
    print(f"Wrote badge: {BADGE_PATH}")

if __name__ == "__main__":
    main()
