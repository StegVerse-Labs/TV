# TV Quickstart — StegVerse Token Vault
**Audience:** Internal & trusted contributors  
**Tone:** Authoritative / Guardian  
**Self-Heal:** Enabled (workflows auto-repair canonical files)

---

## 0) Read This First
You are entering a **security-critical** system. Treat the Token Vault (TV) as a protected facility:
- Use **least privilege** and **short-lived** credentials.
- Expect **auditability** and **revocation** if standards are not met.
- Security exists to **protect people and truth**, not to hide it.

▶ Full Oath: **[`docs/GUARDIAN_OATH.md`](./GUARDIAN_OATH.md)**

---

## 1) Required Repo Layout (Essentials)

TV/
├─ .github/workflows/
│  ├─ tv_self_heal.yml
│  ├─ tv_apply_reusable.yml
│  ├─ tv_verify_reusable.yml
│  ├─ tv_apply_verify_chain.yml
│  └─ tv_auto_heal.yml                # optional notifier
├─ roles_templates/
│  ├─ stegcore.yml  stegtalk.yml  scw.yml  freedom.yml  guardian_ai.yml
├─ scripts/
│  ├─ tv_build_signed_export.py  tv_sign_export_cosign.py
│  ├─ tv_chainlog_builder.py     tv_integrity_verify.py
├─ data/summary/chainlog.jsonl
├─ tv_manifest.yml
└─ docs/GUARDIAN_OATH.md   docs/TV_WORKFLOWS.md   docs/TV_QUICKSTART.md

---

## 2) One-Time Setup
1. **Verify `tv_manifest.yml`** is a *single* YAML document with valid module paths.  
2. **Run Self-Heal**: Actions → **TV Self-Heal (Bootstrap)** → *Run workflow*.  
3. (Optional) Add secrets when ready:  
   - `TV_HMAC_SIGNING_KEY` (HMAC fallback signing)  
   - `TV_WEBHOOK_URL` (failure notifications)

---

## 3) Daily Operations (Apply → Verify)
- **Manual or Scheduled:** Actions → **TV Apply + Verify (Chained)**  
- **Outputs:** Signed export, signature, and updated `chainlog.jsonl`  
- **If Verify fails:** “TV Auto-Heal” writes a marker + optional webhook

---

## 4) Embodied Ethics (Excerpt)
> **Guardian Oath (Excerpt)**  
> I will protect the vulnerable, preserve truth with provenance, respect chain-of-custody, use least privilege, refuse misuse, accept auditability, defend against drift, and escalate ambiguity. I will act transparently and reversibly, and I will never suppress survivor testimony or ethical whistleblowing.  
>  
> Full text: [`docs/GUARDIAN_OATH.md`](./GUARDIAN_OATH.md)

---

## 5) Safety Rules You Must Follow
- **No secret sprawl:** Never store secrets in code, issues, or docs.  
- **PR review required** for TV policy/role changes; emergency changes must be post-audited <24h.  
- **Provenance or pause:** If integrity/origin is unclear, halt & escalate.  
- **Dual control:** Use two-person (or human+AI) confirmation for high-risk moves.  
- **Survivor safety check** before publishing correlated data.

---

## 6) For AI Entities (Stage 1)
- Load the **Oath** at start; treat it as controlling policy.  
- No semantic relabeling to bypass rules.  
- Log rationales for sensitive actions.  
- Re-attest after model or prompt changes (Appendix B roadmap).

---

## 7) Troubleshooting
- **YAML errors:** Run **TV Self-Heal (Bootstrap)** — it rewrites canonical workflows.  
- **Artifact missing:** Verify will rebuild export automatically.  
- **Cosign issues:** Our installer uses a direct binary; self-heal refreshes it.  
- **Manifest parse:** Ensure no duplicate `version:` documents in `tv_manifest.yml`.

---

## 8) Roadmap to E5 (Signing Oath)
When StegCore governance is ready:
- Cryptographically **sign Oath** at activation; append attestation to chainlog.  
- Re-sign on model upgrade, role change, or policy revision.  
- Enable **key revocation** + quarantine on breach.

See **Appendix B** in [`docs/GUARDIAN_OATH.md`](./GUARDIAN_OATH.md).

