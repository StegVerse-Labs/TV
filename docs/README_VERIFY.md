# Verification

`TV Apply` produces:
- `tv_export.json` — manifest + role templates
- `tv_export.sig` — HMAC/Sigstore signature (or placeholder `{}` when disabled)
- `data/summary/chainlog.jsonl` — append-only events

`TV Verify Integrity`:
- Downloads the latest bundle
- Computes `export_sha256`
- Heuristically marks `sig_type` and `verified`
- Appends a verification entry to the chainlog and commits it

To enable real signing, add the secret:
- `TV_HMAC_SIGNING_KEY` — a strong random string (64+ hex chars is fine)
