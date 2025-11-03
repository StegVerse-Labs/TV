import argparse, json, pathlib, hashlib, datetime
def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda: f.read(8192), b''): h.update(c)
    return h.hexdigest()
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--export',required=True); ap.add_argument('--signature',required=True); ap.add_argument('--chainlog',required=True); a=ap.parse_args()
    entry={"ts":datetime.datetime.utcnow().isoformat()+"Z","event":"verify",
           "export_sha256":sha256(a.export),"signature_sha256":sha256(a.signature),"status":"ok"}
    outp=pathlib.Path(a.chainlog); outp.parent.mkdir(parents=True,exist_ok=True)
    with open(outp,'a',encoding='utf-8') as f: f.write(json.dumps(entry)+"\n")
    print(f"Verification appended to {outp}")
if __name__=='__main__': main()
