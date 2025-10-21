# Verification

`TV Apply` produces:
- `tv_export.json` — manifest + role templates
- `tv_export.sig` — HMAC/Sigstore signature or `{}` placeholder
- `data/summary/chainlog.jsonl` — append-only entries

`TV Verify Integrity`:
- Downloads export + signature
- Computes `export_sha256`
- Marks `sig_type` and `verified`
- Appends verification entry to chainlog and commits
