#!/usr/bin/env python3
import argparse, json, os, sys, glob, hashlib, time
try:
    import yaml
except Exception:
    print("Missing deps: pip install pyyaml", file=sys.stderr); sys.exit(2)

def sha256_of(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--roles_dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    with open(args.manifest,'r',encoding='utf-8') as f:
        manifest=yaml.safe_load(f)

    items=[]
    for path in sorted(glob.glob(os.path.join(args.roles_dir,"*.yml"))):
        items.append({"file": os.path.basename(path), "sha256": sha256_of(path)})

    report={
        "version": 1,
        "generated_at": int(time.time()),
        "manifest_summary": {
            "org": manifest.get("org"),
            "vault_name": manifest.get("vault_name"),
            "audience": manifest.get("audience"),
            "issuer_count": len(manifest.get("issuers",[])),
            "module_count": len(manifest.get("modules",[])),
        },
        "roles_digest": items,
    }

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out,'w',encoding='utf-8') as f:
        json.dump(report,f,indent=2,sort_keys=True)
    print(f"Wrote {args.out}")

if __name__=="__main__":
    main()
