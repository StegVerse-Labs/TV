# TV QuickStart

### Workflows
- **TV Apply (Signed Export via Sigstore/HMAC)** — builds export from `tv_manifest.yml`
  + `roles_templates/`, signs it (Sigstore keyless if possible) and appends to
  `data/summary/chainlog.jsonl`.
- **TV Verify Integrity** — verifies last export (or rebuilds if artifact is absent) and
  appends a verification entry to chainlog.
- **TV Apply + Verify (Chained)** — convenience button that runs both in order.
- **Policy Lint / Validate** — OPA/Rego lint/validation (safe stubs; no policies needed).
- **TV Auto-Heal** — triggers automatically if Apply or Verify fails; repairs common issues
  (cosign fetch, missing dirs/manifest), commits fixes, then re-runs the chained job.

### Optional outbound push
If you want to POST the signed export to an API, add repo secrets:
`TV_IMPORT_URL`, `TV_IMPORT_TOKEN`, then re-run Apply.
