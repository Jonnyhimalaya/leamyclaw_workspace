# 🧠 Morning Action Brief — 2026-04-15

## 🔴 Fix Now (risks, security, breaking issues)
### 1. Supply Chain Risk & 138+ CVEs (ClawSafe Audit Required)
- **Intel:** The community is tracking 138+ CVEs (including RCE and sandbox escapes) linked to malicious third-party plugins on ClawHub. A new Swiss security service, "ClawSafe", provides a free scanner for OpenClaw GitHub repos.
- **Our exposure:** Our memory already flags a 12%+ malicious plugin rate on ClawHub. Kilmurry Lodge relies on two repos (`Jonnyhimalaya/Kilmurry` and `Jonnyhimalaya/kilmurry-kate`) that need immediate scanning. (Note: We are protected from the CVE-2026-25253 domain takeover since we upgraded to v2026.4.12 yesterday, which patched the `gatewayUrl` vulnerability).
- **Recommended action:** Submit both Kilmurry repos to the free ClawSafe scanner (clawsafe.github.io). Review the 24-hour PDF reports for hardcoded secrets, unrestricted file access, and malicious evals.
- **Effort:** Low

### 2. Update to v2026.4.14 (Fixes Telegram & Chrome/CDP Bugs)
- **Intel:** OpenClaw released v2026.4.14 which patches Telegram integration issues, unstucks subagents, and fixes Chrome/CDP flakiness.
- **Our exposure:** Kate's Telegram RAM alerts are currently failing. We also heavily rely on Chrome browser automation for Meta/IG logins via noVNC.
- **Recommended action:** Update Main VPS, Jack (port 18789), and Kate (port 18792) to v2026.4.14. **Crucial:** Run `openclaw doctor --fix` *before* updating to back up configs, as users report auto-updates wiping configurations. Follow the Universal Playbook Post-Update Verification Checklist.
- **Effort:** Medium

## 🟡 Improve (better patterns, optimisations, upgrades)
### 3. Incorporate LM Studio for Local Model Failovers
- **Intel:** Official LM Studio integration was released, allowing local models on Mac/Windows/Linux via `openclaw onboard --auth-choice lmstudio`.
- **Our exposure:** We currently pitch Gemma 4 via Ollama for compliance-heavy clients. LM Studio provides a much friendlier GUI for Windows/Mac deployments, especially for our SME consultancy clients. With Anthropic API billing remaining expensive, a strong local fallback is critical.
- **Recommended action:** Test the LM Studio integration locally and update our `consultancy/overview.md` to offer it as an alternative to Ollama for Windows/Mac client deployments.
- **Effort:** Low

## 🟢 Opportunities (new tools, client pitch material, competitive advantage)
### 4. Competitive Scenario Planning via DojoZero
- **Intel:** "DojoZero" is gaining massive traction as a platform for real-time multi-agent task competitions (e.g., sports predictions).
- **Our exposure:** We recently deployed the `MiroFish` swarm prediction engine on the main VPS for consultancy and Kilmurry scenario planning.
- **Recommended action:** Analyze DojoZero's architecture to see if we can adapt their competitive scoring mechanisms for our MiroFish engine. This could vastly improve Kilmurry's scenario planning accuracy.
- **Effort:** High

## 📋 Summary
- 4 items flagged (2 critical, 1 improvement, 1 opportunity)
- Estimated total implementation effort: ~2-3 hours
- Priority recommendation: Run the free ClawSafe scanner immediately to ensure our Kilmurry repos aren't compromised by supply chain attacks, then update to v2026.4.14 to fix the failing Telegram alerts.