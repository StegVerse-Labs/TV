import json, argparse, pathlib, yaml
def load_yaml(p): return yaml.safe_load(open(p, 'r', encoding='utf-8'))
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--manifest', required=True)
    ap.add_argument('--roles_dir', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    m = load_yaml(a.manifest)
    roles = []
    for mod in m.get('modules', []):
        rp = pathlib.Path(a.roles_dir) / pathlib.Path(mod['policy']).name
        roles.append(load_yaml(rp) if rp.exists() else {"name": mod['name'], "missing_policy": str(rp)})
    export = {"version": m.get("version",1), "org": m.get("org"), "vault_name": m.get("vault_name"),
              "audience": m.get("audience"), "roles": roles}
    outp = pathlib.Path(a.out); outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(export, indent=2), encoding='utf-8')
    print(f"Wrote export to {outp}")
if __name__ == '__main__': main()
