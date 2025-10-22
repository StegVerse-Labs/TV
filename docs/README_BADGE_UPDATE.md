# TV Status Badge (Auto-Update)

This pack keeps `docs/tv_status.svg` fresh using your latest audit summary (`reports/*_summary.json`).

## Files
- `.github/workflows/tv_status_badge_update.yml` — runs daily and after audits
- `scripts/tv_badge_update.py` — builds the SVG, writes `tv_status.meta.json`, and optional HMAC signature

## Optional secret
- `TV_BADGE_HMAC_KEY` — hex-encoded key (preferred) or raw string; creates `docs/tv_status.svg.sig` (HMAC-SHA256)

## Staleness window
- Env var `TV_STATUS_STALE_DAYS` (default 2) controls when the badge flips to **stale** if no recent audits.

## README usage
```md
![TV Audit Status](docs/tv_status.svg)
```
