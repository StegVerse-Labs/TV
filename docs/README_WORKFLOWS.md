# Workflows Overview

- **TV Apply (Signed Export via Sigstore/HMAC)**: builds export from `tv_manifest.yml` + `roles_templates/`, signs, appends apply entry.
- **TV Verify Integrity**: verifies and appends verify entry.
- **TV Apply + Verify (Chained)**: one-click run of both stages.
- **Daily Scheduled**: runs chained flow daily 06:00 UTC.
- **Report (Daily/Weekly)**: builds audit snapshots.
- **Status Badge**: updates `docs/tv_status.svg` from latest summary.
- **README Badge Patch**: inserts badge line automatically.
- **Artifact Cleanup**: removes old artifacts (manual or weekly).

All support manual “Run workflow” on mobile.
