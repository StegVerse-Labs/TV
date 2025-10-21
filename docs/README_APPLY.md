# TV Apply (Signed Export via Sigstore/HMAC)

This workflow builds a Token Vault export from `tv_manifest.yml` + `roles_templates/`, signs it
with Sigstore (keyless OIDC) or falls back to HMAC if `TV_HMAC_SIGNING_KEY` is provided, then
appends an entry to the append-only `data/summary/chainlog.jsonl` and publishes an artifact.

## Mobile-friendly Manual Run
1. Open: https://github.com/StegVerse/TV/actions/workflows/tv_apply_sigstore.yml
2. Ensure branch **main** is selected.
3. Tap **Run workflow** and accept default reason.

## Optional Secrets
- `TV_HMAC_SIGNING_KEY` — used if Sigstore cannot produce a keyless signature.
- `TV_IMPORT_URL` + `TV_IMPORT_TOKEN` — if present, the job POSTs the signed export to your importer.

Artifacts:
- `tv_signed_export_bundle`: contains the export JSON, detached signature, and updated chainlog.
