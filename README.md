# Token Vault (TV) — StegVerse Core

> **Bundle:** Option **C3** (Full Auto-Healing)

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

## Chain of Trust
- Signing: **Sigstore Keyless** if available; else **HMAC** fallback.
- Chainlog: stores SHA-256 of export + signature and workflow info.
- Verify: recomputes digests and appends verification records.

See `docs/README_TV_QUICKSTART.md` for details. 
