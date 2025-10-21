# TV Guardian + Sigstore Pack

Adds:
- **Signed exports** (Sigstore keyless if available, HMAC fallback)
- **Weekly audit report** (`data/summary/tv_audit_report.json`)
- **Integrity check** across repos from `tv_manifest.yml`
- **Append-only chain log** at `data/summary/chainlog.jsonl`

## Secrets (optional but recommended)
- `TV_IMPORT_URL`, `TV_IMPORT_TOKEN` — push export to your importer
- `TV_HMAC_SIGNING_KEY` — HMAC fallback signing secret
- `TV_GH_TOKEN` — query private repos in integrity checks

## Workflows
- `.github/workflows/tv_apply_sigstore.yml`
- `.github/workflows/tv_report.yml`
- `.github/workflows/tv_integrity_check.yml`

## Scripts
- `scripts/tv_build_signed_export.py` — assemble export JSON
- `scripts/tv_sign_export_cosign.py` — sign via Sigstore or HMAC
- `scripts/tv_generate_audit_report.py` — weekly summary
- `scripts/tv_integrity_verify.py` — repo snapshot
- `scripts/tv_chainlog_builder.py` — append-only chain log

> No secrets are printed to logs. Artifacts are uploaded for review.
