# TV Verify Integrity Workflow

Verifies the latest signed export and appends a verification entry into
`data/summary/chainlog.jsonl`. Can be run manually (mobile-safe) or automatically
after the Apply workflow finishes.

## Manual Run
1. Open: https://github.com/StegVerse/TV/actions/workflows/tv_verify_integrity.yml
2. Select **main** branch → **Run workflow**.

If the Apply artifact isn’t available, this workflow **rebuilds the export locally**
so verification + chainlog writing still proceed.
