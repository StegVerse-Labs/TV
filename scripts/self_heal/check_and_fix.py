#!/usr/bin/env python3
import sys, json, re, subprocess, pathlib
from typing import Dict, Any, List
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]  # repo root
REPORT: Dict[str, Any] = {"problems": [], "fixes": []}

def add_problem(msg: str, path: pathlib.Path = None):
    REPORT["problems"].append({"msg": msg, "path": str(path) if path else None})

def add_fix(msg: str, path: pathlib.Path = None):
    REPORT["fixes"].append({"msg": msg, "path": str(path) if path else None})

def read_text(p: pathlib.Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except FileNotFoundError:
        add_problem(f"Missing file: {p}", p); return ""

def write_text(p: pathlib.Path, s: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")
    add_fix(f"Wrote {p.name}", p)

def load_yaml_single(doc_path: pathlib.Path):
    raw = read_text(doc_path)
    if not raw:
        return None, raw
    # if multiple YAML docs (---), keep only the first
    parts = [part for part in raw.split("\n---") if part.strip() != ""]
    first = parts[0] if parts else raw
    try:
        data = yaml.safe_load(first) if first.strip() else {}
        return data, raw
    except Exception as e:
        add_problem(f"YAML parse error: {doc_path}: {e}", doc_path)
        return None, raw

def dump_yaml(obj) -> str:
    return yaml.safe_dump(obj, sort_keys=False).rstrip() + "\n"

def ensure_chainlog():
    p = ROOT / "data/summary/chainlog.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        write_text(p, "")
    return p

def heal_tv_manifest():
    mpath = ROOT / "tv_manifest.yml"
    data, raw = load_yaml_single(mpath)
    if data is None:
        return
    # required keys
    required = ["version","org","vault_name","audience"]
    missing = [k for k in required if k not in data]
    for k in missing:
        add_problem(f"tv_manifest.yml missing key: {k}", mpath)

    # normalize modules to list of {name,policy}
    mods = data.get("modules", [])
    if mods is None: mods = []
    fixed = []
    seen = set()
    for item in mods:
        if isinstance(item, dict) and "name" in item and "policy" in item:
            key = (item["name"], item["policy"])
            if key in seen:
                add_problem(f"Duplicate module entry: {key}", mpath)
                continue
            seen.add(key)
            fixed.append(item)
        else:
            add_problem(f"Bad module entry (expect {{name,policy}}): {item}", mpath)
    data["modules"] = fixed

    # verify referenced role files exist
    for it in fixed:
        rpath = ROOT / it["policy"]
        if not rpath.exists():
            add_problem(f"Referenced role policy missing: {it['policy']}", rpath)

    # if original had multiple YAML docs, rewrite single normalized doc
    new = dump_yaml(data)
    if new != raw:
        write_text(mpath, new)

def find_yaml_files() -> List[pathlib.Path]:
    bad_dirs = {".git"}
    out = []
    for p in ROOT.rglob("*.yml"):
        if any(seg in bad_dirs for seg in p.parts): continue
        out.append(p)
    for p in ROOT.rglob("*.yaml"):
        if any(seg in bad_dirs for seg in p.parts): continue
        out.append(p)
    return out

def lint_all_yaml():
    for p in find_yaml_files():
        try:
            yaml.safe_load(read_text(p))
        except Exception as e:
            add_problem(f"YAML parse error: {e}", p)

def heal_workflow_uses_paths():
    """
    Fix common local-uses mistakes in the chained workflow:
    - ensure local reusable references use './.github/workflows/...'
    """
    w = ROOT / ".github/workflows/tv_apply_verify_chain.yml"
    if not w.exists(): return
    s = read_text(w)
    orig = s
    # normalize './.github/workflows/...' if someone wrote '.github/workflows/...'
    s = re.sub(r'uses:\s*\.github/workflows/', 'uses: ./.github/workflows/', s)
    if s != orig:
        write_text(w, s)

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["check","fix"], default="fix")
    ap.add_argument("--report", default="data/summary/heal_report.json")
    args = ap.parse_args()

    ensure_chainlog()
    heal_tv_manifest()
    lint_all_yaml()
    heal_workflow_uses_paths()

    # write report
    rpath = ROOT / args.report
    rpath.parent.mkdir(parents=True, exist_ok=True)
    rpath.write_text(json.dumps(REPORT, indent=2), encoding="utf-8")

    # If running in "check", exit nonzero on problems
    if args.mode == "check" and REPORT["problems"]:
        sys.exit(1)

if __name__ == "__main__":
    main()
