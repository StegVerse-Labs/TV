#!/usr/bin/env python3
import argparse, json, os, sys, glob
try:
    import yaml
except Exception:
    print("Missing deps: pip install pyyaml", file=sys.stderr); sys.exit(2)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--roles_dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    with open(args.manifest, 'r', encoding='utf-8') as f:
        manifest = yaml.safe_load(f)

    roles = {}
    for path in glob.glob(os.path.join(args.roles_dir, "*.yml")):
        with open(path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        roles[os.path.basename(path)] = data

    export = {
        "version": 1,
        "generated_by": "tv_build_signed_export.py",
        "manifest": manifest,
        "roles": roles,
    }

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, 'w', encoding='utf-8') as f:
        json.dump(export, f, indent=2, sort_keys=True)
    print(f"Wrote {args.out}")

if __name__ == "__main__":
    main()
