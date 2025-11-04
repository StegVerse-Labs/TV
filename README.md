# Token Vault (TV) — StegVerse Core

This repository is the **policy + secret distribution hub** for StegVerse.
It ships with **Apply → Verify → Auto-Heal** workflows, OPA/Rego lint/validation,
and a signed export + append-only chainlog.

## One-Minute Quickstart
1. Commit this whole bundle (preserve folder paths).
2. Go to **Actions → “TV Apply + Verify (Chained)” → Run workflow**.
3. You should see green checks for:
   - Build export, Sign (Sigstore/HMAC), Append to chainlog, Verify bundle.
4. If a future run fails, **C3 Auto-Heal** kicks in, attempts a repair, and re-runs.

**No secrets required** for default path.  
Optional outbound push: set `TV_IMPORT_URL` + `TV_IMPORT_TOKEN` in repo **Settings → Secrets → Actions**.

## Folders
- `roles_templates/` — role policy templates for StegCore modules.
- `scripts/` — Python utilities used by workflows.
- `.github/workflows/` — CI (apply, verify, chain, lint, validate, auto-heal).
- `data/summary/chainlog.jsonl` — append-only log (created on first run).
- `tv_manifest.yml` — minimal seed manifest.

## 🔐 Token Vault Workflows (TV)

We ship four GitHub Actions under `.github/workflows/`:

- **TV Apply (Reusable)** – `tv_apply_reusable.yml`  
  Reusable job that builds the export (`tv_manifest.yml` + `roles_templates/`), signs it (Sigstore keyless if OIDC available; HMAC fallback), appends to `data/summary/chainlog.jsonl`, and uploads `tv_signed_export_bundle`.

- **TV Verify (Reusable)** – `tv_verify_reusable.yml`  
  Reusable job that verifies the latest export and appends a verification entry to the chainlog. Accepts optional inputs for export/sign paths.

- **TV Apply + Verify (Chained)** – `tv_apply_verify_chain.yml`  
  Orchestrator with **manual Run** and a daily cron. Calls the two reusables in sequence. Artifacts: `tv_signed_export_bundle`, `tv_verified_bundle`.

- **TV Apply (Standalone)** – `tv_apply_standalone.yml`  
  A direct, manual **Run** version of Apply (handy on mobile or if the chained workflow is hidden). Produces the same `tv_signed_export_bundle`.

### Where to find results
- **Artifacts**: Actions run → “Artifacts” → `tv_signed_export_bundle` / `tv_verified_bundle`
- **Chainlog**: `data/summary/chainlog.jsonl` (append-only ledger)

### Troubleshooting
- No **Run workflow** button? Use the **Standalone** or **Chained** workflows (they include `workflow_dispatch`). Reusable workflows (`workflow_call`) intentionally do not show a Run button.
- Ensure repo Settings → **Actions** → “Allow all actions and reusable workflows”, and **Workflow permissions = Read and write**.
- If Sigstore keyless can’t mint OIDC, the signer falls back (bundle still produced).

## Chain of Trust
- Signing: **Sigstore Keyless** if available; else **HMAC** fallback.
- Chainlog: stores SHA-256 of export + signature and workflow info.
- Verify: recomputes digests and appends verification records.

See `docs/README_TV_QUICKSTART.md` for details. 
