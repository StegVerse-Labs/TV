# TV Audit Reports + Webhooks

Two reporting workflows:
- **Weekly** (`TV Report (Weekly Audit)`): CSV + PDF + optional webhook.
- **Daily** (`TV Report (Daily Mini-Audit)`): CSV only + optional webhook.

## Webhook (Slack/Discord)

Add a repo secret named **`TV_WEBHOOK_URL`**. The workflow will POST the latest
`*_summary.json` (one-line JSON with counts) to that URL. For Slack, use an
Incoming Webhook; for Discord, use a Channel Webhook.

Example payload (sent by the workflow):
```json
{
  "csv": "tv_audit_2025-41.csv",
  "pdf": "tv_audit_2025-41.pdf",
  "total_entries": 42,
  "apply": 21,
  "verify": 21,
  "status_ok": 40,
  "status_fail": 2,
  "sig_sigstore": 25,
  "sig_hmac": 17,
  "first_ts": "2025-10-16T07:01:00+00:00",
  "last_ts": "2025-10-21T06:59:00+00:00"
}
```
You can transform this at your webhook endpoint or post raw JSON to Slack/Discord.
