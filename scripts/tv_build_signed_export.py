#!/usr/bin/env python3
import sys, json, yaml, os, hashlib
from pathlib import Path
from datetime import datetime, timezone

def sha256_bytes(b: bytes) -> str:
    import hashlib
    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--roles_dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    manifest_path = Path(args.manifest)
    roles_dir = Path(args.roles_dir)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    manifest = {}
    if manifest_path.exists():
        with open(manifest_path, "r", encoding="utf-8") as f:
            manifest = yaml.safe_load(f) or {}
    else:
        manifest = {"version": 1, "org": "unknown", "vault_name": "TV", "audience": "default"}

    roles = []
    if roles_dir.exists():
        for p in sorted(roles_dir.glob("*.yml")):
            roles.append({"name": p.stem, "path": str(p)})
    export = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "manifest": manifest,
        "roles": roles,
    }
    raw = json.dumps(export, indent=2).encode("utf-8")
    out_path.write_bytes(raw)
    print(f"Wrote export to {out_path} (sha256={sha256_bytes(raw)})")

if __name__ == "__main__":
    main()
