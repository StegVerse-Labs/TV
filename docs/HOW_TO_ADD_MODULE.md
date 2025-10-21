# How to Add a Module to StegVerse/TV (Green Baseline)

This process produces a role template that passes both:
- JSON Schema (`schema/policy.schema.json`)
- OPA/Rego policy (`policy/opa/policy.rego`)

## 1) Choose a role name and keys
- Role naming: `<module>/ci/<purpose>` (e.g., `analytics/ci/build`)
- Keys: minimal **read-only** keys required by CI (no writes)

## 2) Copy a baseline and edit
Use one of the files in `roles_templates/` (e.g., `stegtalk.yml`) and change:
- `roles.<your-role>.description`
- `ttl_minutes` (≤ 30 preferred; ≤ 60 required by policy)
- `permissions.kv:read` (list only what you need)
Do **not** add `kv:write` or `actions` unless creating a **guardian** role.

## 3) Validate locally (optional)
```bash
pip install pyyaml jsonschema
python scripts/validate_policies.py

# If you installed conftest and have policy/opa/policy.rego:
conftest test roles_templates --policy policy/opa --all-namespaces
