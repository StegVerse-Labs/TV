# TV Minimal Workflows (Option C — Chained)

Two workflows wired so **Apply** triggers **Verify** automatically.

- `.github/workflows/tv_apply_sigstore.yml` — Builds export and signs it (Sigstore keyless via OIDC; HMAC fallback inside `tv_sign_export_cosign.py`). Uploads `tv_signed_export_bundle`.
- `.github/workflows/tv_verify_integrity.yml` — Triggered by Apply (and can run manually). Downloads the artifact (or rebuilds), verifies, appends to `data/summary/chainlog.jsonl`, commits/pushes, uploads `tv_verified_bundle`.

## Install
1. Create these files at the paths above.
2. Ensure repo contains:
   - `scripts/tv_build_signed_export.py`
   - `scripts/tv_sign_export_cosign.py`
   - `scripts/tv_integrity_verify.py`
   - `roles_templates/` and `tv_manifest.yml`
3. Run **Actions → TV Apply (Signed Export via Sigstore/HMAC) → Run workflow**.
   - **TV Verify Integrity** will auto-run after Apply completes.

No secrets are required in this minimal set.
