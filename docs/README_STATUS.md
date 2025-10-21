# TV Status Badge

This pack adds an auto-updating **status badge** that reflects the latest audit result.

## Files
- `.github/workflows/tv_status_badge.yml` — builds a small SVG after audits
- `scripts/tv_build_status_badge.py` — reads the most recent `reports/*_summary.json` and writes `docs/tv_status.svg`

## How it works
- Triggers automatically after **TV Report (Daily Mini-Audit)** and **TV Report (Weekly Audit)**.
- Also supports manual runs via the *Run workflow* button.
- Badge is written to `docs/tv_status.svg` and committed to the repo.

## Add to README
Put this line near the top of your `README.md`:

![TV Audit Status](docs/tv_status.svg)

## Staleness
If the last audit is older than **2 days**, the badge shows **stale**.
Change this by editing `TV_STATUS_STALE_DAYS` env in the workflow.
