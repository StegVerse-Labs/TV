#!/usr/bin/env python3
import argparse, json, os, sys, base64, hmac, hashlib, subprocess

def sign_hmac(data_bytes, key):
    mac = hmac.new(key.encode('utf-8'), data_bytes, hashlib.sha256).digest()
    return {"type":"hmac-sha256","sig":base64.b64encode(mac).decode()}

def sign_sigstore(path):
    try:
        out = subprocess.check_output(
            ["cosign","sign-blob","--yes","--output-signature","-", path],
            stderr=subprocess.STDOUT
        )
        return {"type":"sigstore-cosign","sig":out.decode().strip()}
    except Exception:
        return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    with open(args.inp,'rb') as f:
        data = f.read()

    sig = sign_sigstore(args.inp)
    if sig is None:
        key = os.getenv("TV_HMAC_SIGNING_KEY")
        if not key:
            print("No cosign available and TV_HMAC_SIGNING_KEY missing; cannot sign.", file=sys.stderr)
            sys.exit(2)
        sig = sign_hmac(data, key)

    with open(args.out,'w',encoding='utf-8') as f:
        json.dump(sig, f, indent=2, sort_keys=True)
    print(f"Wrote signature to {args.out} ({sig['type']})")

if __name__ == "__main__":
    main()
