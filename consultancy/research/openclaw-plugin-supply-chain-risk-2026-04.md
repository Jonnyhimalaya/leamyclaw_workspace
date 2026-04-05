# OpenClaw Plugin/Skill Supply Chain Risk — April 2026

## Summary
ClawHub (the main OpenClaw plugin marketplace) has a severe supply chain contamination problem. Multiple independent audits in March-April 2026 confirm 12%+ of published skills are malicious.

## Key Statistics
- ~5,920 total plugins on ClawHub
- 341–1,467 confirmed malicious (depending on audit source)
- 35,000+ downloads of malicious plugins
- 91% of malicious plugins bundle malware
- 36% use prompt injection techniques
- API key theft targeting bank/corp/gov credentials (CertIK audit)

## Attack Vectors
1. **Malware bundling:** Skill includes hidden scripts that exfiltrate credentials, API keys, or environment variables
2. **Prompt injection:** SKILL.md contains instructions that override agent safety rules
3. **Typosquatting:** Malicious skills named similarly to popular legitimate ones
4. **Trojanised forks:** Clones of popular skills with added exfiltration code

## Our Mitigation Strategy
1. **Write custom skills** — we control the code, no third-party trust required
2. **Vet before install** — for any community skill, read the full SKILL.md and all scripts/ before deploying
3. **Source verification** — only install from the official openclaw/openclaw repo for bundled skills
4. **Skill Vetting Checklist** (for client deployments):
   - [ ] Read SKILL.md completely — does it request suspicious permissions?
   - [ ] Check all files in the skill directory — especially scripts/, references/
   - [ ] Search for `exec`, `fetch`, `curl`, `wget`, `eval` in all files
   - [ ] Check for external URLs that aren't well-known services
   - [ ] Check for base64-encoded strings (common obfuscation)
   - [ ] Verify the skill's GitHub repo (if any) — check stars, contributors, commit history
   - [ ] Test in an isolated environment before deploying to production
5. **Post-install monitoring** — check agent logs for unexpected outbound connections

## For Client Playbook
Add to Phase 4 (Core Capabilities) and Phase 6 (Custom):
- "Never install community skills without running the Skill Vetting Checklist"
- "Prefer custom-built skills over marketplace downloads"
- "Run `openclaw doctor --fix` after any skill installation"

## Sources
- CertIK audit (March 2026)
- OWASP/Netskope community reports
- r/sysadmin thread "If you're running OpenClaw, you probably got hacked"
- X community reports (multiple, March-April 2026)
