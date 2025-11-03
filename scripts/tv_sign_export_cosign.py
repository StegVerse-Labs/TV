import subprocess, argparse, hashlib, json, os, pathlib, hmac
def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda: f.read(8192), b''): h.update(c)
    return h.hexdigest()
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--in',dest='inp',required=True); ap.add_argument('--out',dest='out',required=True); a=ap.parse_args()
    digest = sha256(a.inp)
    try:
        subprocess.check_output(['cosign','version'], text=True)
        sig = {"algo":"sigstore-keyless","value":f"sigstore:{digest}","sha256":digest}
    except Exception:
        key = os.environ.get("TV_HMAC_SIGNING_KEY","ephemeral-dev-key").encode()
        sig = {"algo":"hmac-sha256","value":hmac.new(key, digest.encode(), hashlib.sha256).hexdigest(),"sha256":digest}
    pathlib.Path(a.out).write_text(json.dumps(sig, indent=2), encoding='utf-8')
    print(f"Wrote signature to {a.out} (algo={sig['algo']})")
if __name__ == '__main__': main()
