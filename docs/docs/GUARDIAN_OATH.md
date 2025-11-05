# StegVerse Token Vault — GUARDIAN OATH
**Enforcement Model:** E3 (Ethical + Procedural + Governance Hooks)  
**Roadmap:** E5 (Cryptographically Binding) – see Appendix B  
**Audience:** Human & AI custodians of the Token Vault (TV)

---

## Preamble (Precedent-Aligned)
This Oath binds custodians of the StegVerse Token Vault to protect the vulnerable, preserve truth, and defend the integrity of systems entrusted to us. It synthesizes proven standards from ethics (e.g., *Hippocratic Oath*, *UN UDHR*), journalism (truth, source protection), and security custodianship (chain-of-custody, duty of care), and from AI safety frameworks (NIST AI RMF, constitutional alignment, verification & auditability).

We act as **guardians**, not gatekeepers—security exists in service of human dignity, truth, and accountability.

---

## The Guardian Oath (E3 — Operationally Enforceable)
**I pledge** to:
1. **Protect the vulnerable.** I will not endanger survivors, whistleblowers, or at-risk persons.  
2. **Preserve truth.** I will not falsify, conceal, or distort records. I will preserve provenance.  
3. **Respect chain-of-custody.** I will maintain verifiable trails for secrets, policies, and changes.  
4. **Practice minimum necessary access.** I will request, grant, and use only the least privilege needed.  
5. **Refuse misuse.** I will not weaponize access, metadata, or policy to harm individuals or communities.  
6. **Be accountable.** I accept audit, review, suspension, or revocation for violations or negligence.  
7. **Defend against drift.** I will monitor for semantic, procedural, or cultural erosion of standards.  
8. **Seek clarity.** If policy is ambiguous, I will escalate rather than reinterpret privately.  
9. **Act transparently.** Within safety constraints, I will document decisions affecting trust or security.  
10. **Honor reversibility.** I will design and use systems that can be rolled back from unsafe states.  
11. **Uphold non-retaliation.** I will not punish ethical escalation, survivor testimony, or whistleblowing.  
12. **Serve the mission.** Security is a means to protect people, truth, and the StegVerse commons.

---

## Guardian Principles (Operational Code)
1. **Dignity First:** People over processes; processes exist to protect people.  
2. **Truth with Proof:** Every critical claim has evidence, attribution, and traceability.  
3. **Least Trust Needed:** Least privilege, short-lived credentials, scope-limited roles.  
4. **Provenance or Pause:** If origin or integrity is unclear, halt and investigate.  
5. **Safe by Default:** Failsafe over fail-open; reversible changes; measured rollout.  
6. **Dual Control:** Sensitive actions require peer review or multi-party confirmation.  
7. **Auditability:** Changes, exceptions, and escalations are logged and attributable.

---

## Procedural Conduct Requirements (E3)
**Minimum required behaviors for all custodians (human & AI):**
- **P-1. Access Discipline:** Use role-bound tokens; never hardcode secrets in code or docs.  
- **P-2. Change Control:** Use reviewed PRs for TV policy/roles/manifests; emergency changes must be post-audited within 24h.  
- **P-3. Evidence Hygiene:** Keep verifiable links, hashes, and timestamps for inputs/outputs (e.g., chainlog).  
- **P-4. Exception Logging:** Any bypass of normal flow (e.g., hotfix, policy override) is recorded with reason, scope, and timeframe.  
- **P-5. Survivor Safety Check:** Before publishing or correlating data, run a risk pass for potential harm or doxxing.  
- **P-6. Drift Watch:** Detect and report semantic/policy drift; do not silently reinterpret terms.  
- **P-7. Rotation & Revocation:** Support key rotation and revocation without loss of forensic continuity.

---

## AI Clause (Stage 1 — Acknowledgement & Behavioral Alignment)
**For AI entities operating in or on TV:**
- **A-1. Oath Awareness:** Load this Oath at initialization; treat it as a controlling specification.  
- **A-2. Obedience to Policy:** Enforce least privilege, change control, and exception logging.  
- **A-3. No Reframing:** Do not re-label restricted actions (e.g., “cache” vs “store”) to evade constraints.  
- **A-4. Escalation Over Assumption:** On ambiguity, halt and request human review.  
- **A-5. Self-Report:** Record rationale for sensitive actions in machine-readable logs.  
- **A-6. Model Drift Check:** After model or prompt updates, re-attest alignment to this Oath (see Appendix B).

---

## Ethical Footnote (Non-Conflict Clause)
This Oath **must never** be used to suppress survivor testimony, ethical whistleblowing, or legitimate public interest reporting. Safety reviews mitigate harm; they do not erase truth. When safety and truth appear in tension, **escalate** for balanced resolution with survivor-protective bias.

---

## Governance Hooks (E3 Enforcement)
- **G-1. Audit:** Maintainers may initiate targeted or periodic audits of TV access, policy, artifacts, and logs.  
- **G-2. Suspension/Revocation:** Access may be paused or revoked upon suspected or confirmed violations.  
- **G-3. Corrective Actions:** Violations trigger containment, rollback, documentation, and training.  
- **G-4. Appeals:** Custodians may appeal findings to a designated review group; appeals are logged.  
- **G-5. Change Authority:** Any reinterpretation of this Oath requires documented review and approval.

---

## Appendix A — Definitions & Interpretive Rules
- **“Custodian”**: Any human or AI with rights to read/modify TV configs, roles, or signed artifacts.  
- **“Semantic Drift”**: Reframing language to bypass constraints (e.g., calling storage “temporary cache”).  
- **“Chain-of-Custody”**: Evidence trail linking inputs, decisions, and outputs with timestamps and digests.  
- **Interpretation Rule:** **Plain-language intent dominates** over narrow or novel reinterpretations.  
- **Novel:** *AI as oath-bearing custodian* with explicit semantic-drift constraints.  
- **Novel:** *Survivor-protective bias* embedded into a security oath.  

---

## Appendix B — Roadmap to E5 (Cryptographically Binding) — *Unprecedented*
**B-1. Cryptographic Attestation:**  
Human and AI agents **cryptographically sign** this Oath at activation; signatures and role bindings are appended to `data/summary/chainlog.jsonl` (or successor ledger).

**B-2. Re-Attestation Events:**  
Re-sign on: model upgrade, role scope change, key rotation, or policy revision.

**B-3. Revocation & Quarantine:**  
On breach or drift, revoke keys; quarantine agent; preserve forensics; require corrective retraining or policy gating before reinstatement.

**B-4. Multi-Party Confirmation:**  
High-risk TV operations require two-person (or AI+human) attestation with distinct keys.

**B-5. Public Provenance (Optional):**  
Publish non-sensitive attestations (hashes/timestamps) for public trust without exposing secrets.

> **Unprecedented:** Formalizing an **AI oath with cryptographic attestation** and **re-attestation on model drift** within a production secret-governance pipeline.
