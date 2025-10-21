# TV Weekly Audit Report

Generates a weekly snapshot of Token Vault integrity:

- Reads `data/summary/chainlog.jsonl`
- Produces `reports/tv_audit_YYYY-WW.csv` and (if possible) `reports/tv_audit_YYYY-WW.pdf`
- Commits reports back to the repo and uploads them as workflow artifacts

Files:
- Workflow: `.github/workflows/tv_report_weekly.yml`
- Script: `scripts/tv_generate_audit_report.py`
