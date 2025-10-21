#!/usr/bin/env python3
import argparse, json, os, time, hashlib

def sha256_text(path):
    h = hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--export", required=True)
    ap.add_argument("--signature", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    entry = {
        "kind": "tv.apply",
        "timestamp": int(time.time()),
        "export_sha256": sha256_text(args.export),
        # we don't store full sig here for safety; verification step will classify
    }

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, 'a', encoding='utf-8') as f:
        f.write(json.dumps(entry, sort_keys=True) + "\n")
    print(f"Appended chain entry to {args.out}")

if __name__ == "__main__":
    main()
