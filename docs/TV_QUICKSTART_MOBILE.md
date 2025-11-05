# TV Quickstart (Mobile) — StegVerse Token Vault
**Audience:** Internal & trusted contributors • **Mode:** iPhone-optimized

---

## 0) Read First (30 sec)
- TV is **security-critical**. Use **least privilege** + expect **audit**.  
- Ethics protect **people & truth** — not secrecy.  
- Read: [`docs/GUARDIAN_OATH.md`](./GUARDIAN_OATH.md)

---

## 1) One-Time Prep (2–3 taps each)
1. **Open Actions** → run **TV Self-Heal (Bootstrap)**.  
2. **Check** repo has: `tv_apply_*`, `tv_verify_*`, `tv_auto_heal.yml`.  
3. (Optional) Add secrets later: `TV_HMAC_SIGNING_KEY`, `TV_WEBHOOK_URL`.

---

## 2) Daily Use (Apply → Verify)
- **Run:** Actions → **TV Apply + Verify (Chained)** → *Run workflow*.  
- **Result:** signed export + signature; `data/summary/chainlog.jsonl` updated.  
- **If Verify fails:** Auto-Heal logs marker; webhook (if set) notifies.

---

## 3) Safety Rules (Tap-to-remember)
- No secrets in code/issues/docs.  
- PR review for TV policy/roles; emergency = post-audit <24h.  
- If origin/provenance is unclear → **Pause & escalate**.  
- Use 2-person (or human+AI) confirmation for high-risk changes.  
- Run **survivor safety check** before publishing correlated data.

---

## 4) For AI Agents
- Load **Oath** at start; treat as controlling policy.  
- Do **not** bypass via renaming (“cache” ≠ “store”).  
- Log rationales for sensitive actions.  
- Re-attest after model or prompt updates.

---

## 5) Fix It Fast
- Weird YAML? → Run **TV Self-Heal (Bootstrap)**.  
- No artifact? → Verify rebuilds automatically.  
- Cosign trouble? → Self-heal refreshes installer.  
- Manifest error? → Ensure one `version:` block in `tv_manifest.yml`.

---

## 6) Future (E5)
- Oath signing becomes **cryptographic attestation** in chainlog.  
- Re-sign on upgrades/role changes; revoke on breach.
