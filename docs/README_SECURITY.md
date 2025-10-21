# TV Security Model

This repo uses a platform-agnostic trust design:

- **No secrets required** to run core workflows. An unsigned/digest-only mode records `export_sha256` to the append-only `data/summary/chainlog.jsonl`.
- **Optional HMAC** (`TV_HMAC_SIGNING_KEY`) enables signed exports without persistent keys in the repo.
- **Sigstore keyless** uses GitHub OIDC (no long-lived secrets) when available.
- **Importer push** is optional and gated by `TV_IMPORT_URL` + `TV_IMPORT_TOKEN`.

## Chainlog
Each run appends:
- `export_sha256` — content digest of `tv_export.json`
- `sig_type` — `none`, `hmac_or_sigstore`, or `unknown`
- `verified` — result from `tv_integrity_verify.py`
- `verifier_id` — provenance of the verification step
- `timestamp` — epoch seconds (UTC)

`data/summary/chainlog.jsonl` is **append-only** and committed by CI.

## Roles
Roles in `roles_templates/` define coarse-grained permissions and TTLs (guardian, auditor, operator, public). Modules can add their own role templates.
