# TV README Badge Patch

This workflow automatically adds the audit badge line to your **root README.md**.

## Files
- `.github/workflows/tv_readme_badge_patch.yml`
- `scripts/tv_insert_badge_line.py`

## How it works
1. Run the workflow **manually once** from the Actions tab.
2. It checks if `![TV Audit Status](docs/tv_status.svg)` exists.
3. If not found, it inserts it just below the first H1 title in your README.
4. Commits and pushes the change to `main`.

If the badge already exists, the workflow exits cleanly with no changes.
