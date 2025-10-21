# TV Security Model (Expansion Pack)

This pack adds:
- Hardened **Apply** workflow (signed exports with Sigstore/HMAC and append-only chainlog)
- **Verify Integrity** workflow (auto-runs on Apply completion)
- Updated scripts and schema for append-only verification trails
- Tiered role templates (guardian, auditor, operator, public)

## No secrets required
All workflows run in digest-only mode if no secrets are configured. Add optional secrets later to upgrade security.

## Chainlog
`data/summary/chainlog.jsonl` appends one JSON per line with:
- `kind`: `tv.apply` or `tv.verify`
- `timestamp`: epoch seconds (UTC)
- `export_sha256`: content digest of `tv_export.json`
- `sig_type` (verify step): `none`, `hmac_or_sigstore`, or `unknown`
- `verified` (verify step): heuristic based on signature presence

## Workflows
- `.github/workflows/tv_apply_sigstore.yml`
- `.github/workflows/tv_verify_integrity.yml`
