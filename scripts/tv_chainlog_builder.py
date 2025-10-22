#!/usr/bin/env python3
import os, sys, json, hashlib
from pathlib import Path
from datetime import datetime, timezone

def sha256_path(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", required=True)
    ap.add_argument("--signature", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    export_path = Path(args.export)
    sig_path = Path(args.signature)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "stage": "apply",
        "event": "apply",
        "export_sha256": sha256_path(export_path) if export_path.exists() else None,
        "signature_kind": "present" if sig_path.exists() and sig_path.stat().st_size > 2 else "none",
        "status": "ok",
        "notes": "apply/append by tv_chainlog_builder.py"
    }
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
    print(f"Appended apply entry to {out_path}")

if __name__ == "__main__":
    main()
