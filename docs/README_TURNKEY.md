# StegVerse TV — Turnkey Bundle

Drop-in pack that bootstraps Token Vault (TV) CI:
- Apply + Verify workflows (manual, chained, and scheduled)
- Weekly & Daily audit reports
- Status badge (auto-updating) + README patch helper
- Artifact cleanup job

## Install
1. Upload this bundle to your repo (preserve paths).
2. Commit to `main`.
3. Optional: set repo secrets for extra features
   - `TV_HMAC_SIGNING_KEY` (HMAC fallback for signing)
   - `TV_WEBHOOK_URL` (if you added webhook posting in your audits)
   - `TV_BADGE_HMAC_KEY` (sign badge SVG)
4. Create a minimal `tv_manifest.yml` (example below).

## Minimal files to add (recommended)
- `tv_manifest.yml`:
```yaml
version: 1
org: StegVerse
vault_name: TV
audience: stegverse-tv
```
- Add at least one role file in `roles_templates/` (e.g., `sample_operator.yml`).

## Run
- Actions → **TV Apply + Verify (Chained)** → Run workflow
- Actions → **TV Report (Daily/Weekly)** → Run workflow
- Actions → **TV Status Badge (Auto-Update)** → Run workflow

The `data/summary/chainlog.jsonl` will accumulate append-only entries.

## README Badge
Insert this in your README:
```md
![TV Audit Status](docs/tv_status.svg)
```
