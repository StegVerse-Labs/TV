#!/usr/bin/env python3
import argparse, json, os, sys
try:
    import yaml, requests
except Exception:
    print("Missing deps: pip install pyyaml requests", file=sys.stderr); sys.exit(2)

API = "https://api.github.com"

def gh_get(url, token=None):
    h = {"Accept":"application/vnd.github+json"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    r = requests.get(url, headers=h)
    r.raise_for_status()
    return r.json()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    token = os.getenv("TV_GH_TOKEN")  # okay if missing for public repos

    with open(args.manifest,'r',encoding='utf-8') as f:
        m = yaml.safe_load(f)

    repos = []
    for iss in m.get("issuers", []):
        for allow in iss.get("allow", []):
            org = allow.get("org"); repo = allow.get("repo")
            if org and repo: repos.append((org, repo))
    repos = sorted(set(repos))

    results = []
    for org, repo in repos:
        info = {"org":org, "repo":repo, "status":"unknown"}
        try:
            repodata = gh_get(f"{API}/repos/{org}/{repo}", token)
            info["default_branch"] = repodata.get("default_branch","unknown")
            info["visibility"] = repodata.get("visibility","unknown")
            info["status"] = "ok"
        except Exception as e:
            info["status"] = f"error: {e}"
        results.append(info)

    out = {"version":1, "repos":results}
    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out,'w',encoding='utf-8') as f:
        json.dump(out,f,indent=2,sort_keys=True)
    print(f"Wrote {args.out}")

if __name__ == "__main__":
    main()
