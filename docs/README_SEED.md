# TV Seed Pack

This seed gives you the absolute minimum files so the **TV Apply** and **TV Verify** workflows can run on a fresh repo.

## Files
- `tv_manifest.yml` — minimal manifest (org, vault, audience)
- `roles_templates/sample_operator.yml` — one valid role so exports aren't empty

## Usage
1. Upload these files to the repo root (keep paths).
2. Run **Actions → TV Apply (Signed Export via Sigstore/HMAC)**.
3. The **TV Verify Integrity** workflow will follow automatically (if installed).

Generated: 2025-10-21 12:00:51 UTC
