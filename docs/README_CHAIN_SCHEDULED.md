# TV Apply + Verify (Daily Scheduled)

This workflow runs the same steps as the one-click **TV Apply + Verify (Chained)**, but on an **automatic schedule**.

- Default schedule: **06:00 UTC daily**
- Also supports **manual runs** (has its own Run button)

## Files
- Workflow: `.github/workflows/tv_apply_verify_daily.yml`

## Optional Secrets (only if you need remote importer push)
- `TV_IMPORT_URL`
- `TV_IMPORT_TOKEN`
- `TV_HMAC_SIGNING_KEY` (fallback signing)

> You can change the time by editing the cron string in the workflow:
> `0 6 * * *` → minute hour day-of-month month day-of-week
