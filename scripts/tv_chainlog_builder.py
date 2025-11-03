import argparse, json, pathlib, datetime, hashlib
def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda: f.read(8192), b''): h.update(c)
    return h.hexdigest()
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--export',required=True); ap.add_argument('--signature',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    entry={"ts":datetime.datetime.utcnow().isoformat()+"Z","event":"apply",
           "export_sha256":sha256(a.export),"signature_sha256":sha256(a.signature)}
    outp=pathlib.Path(a.out); outp.parent.mkdir(parents=True,exist_ok=True)
    with open(outp,'a',encoding='utf-8') as f: f.write(json.dumps(entry)+"\n")
    print(f"Appended apply entry to {outp}")
if __name__=='__main__': main()
