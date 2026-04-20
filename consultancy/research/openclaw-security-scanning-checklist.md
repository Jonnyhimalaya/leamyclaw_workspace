# OpenClaw Security Scanning Checklist
**Created:** 2026-04-18
**Source:** Semgrep cheat sheet, Snyk ToxicSkills report, community healthcheck tools

## Pre-Deployment / Maintenance Checklist

### 1. Version Verification
- [ ] Running latest stable release
- [ ] Check: `openclaw version` — compare against GitHub releases
- [ ] Known critical CVEs patched: CVE-2026-25253 (≥2026.1.29), CVE-2026-35625 (≥2026.3.25)

### 2. Skill Safety Scan
- [ ] Run built-in skill safety scanner (available since v2026.4.1)
- [ ] Install community `openclaw-healthcheck-skill` v2.1.0
- [ ] Cross-reference installed skills against Snyk/Clawdex malicious skills database
- [ ] Review any ClawHub-sourced skills manually — check GitHub repo, look for exec/message access requests

### 3. Gateway Security
- [ ] Gateway bound to localhost (`gateway.bind: localhost`) OR behind authenticated reverse proxy
- [ ] Auth mode set to `token` or `oidc` (not open)
- [ ] Verify with: `lsof -i :<port> -nP` — should show 127.0.0.1, not 0.0.0.0
- [ ] Tailscale or VPN for remote access (not direct port exposure)

### 4. Execution Security
- [ ] Exec security mode = `allowlist` (not `full`) for client-facing instances
- [ ] No `noSandbox=true` in browser config
- [ ] No root/admin access granted to agent
- [ ] Exec approvals configured for sensitive operations

## Reference Materials
- Semgrep cheat sheet: https://semgrep.dev/blog/2026/openclaw-security-engineers-cheat-sheet/
- Snyk ToxicSkills: https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/
- Hardening guide (3-tier): https://aimaker.substack.com/p/openclaw-security-hardening-guide
- Community security monitor: https://github.com/adibirzu/openclaw-security-monitor

## Key Principles (from Semgrep)
1. **Separation of concerns is lost** — LLMs consume data AND produce code. Input sanitization doesn't apply in the traditional sense.
2. **Trust cannot be inherited** — Every tool call needs validation regardless of origin.
3. **Determinism is gone** — Can't exhaustively test agent behaviour. Enforce security at execution boundary.
4. **Blast radius scales with capability** — Most useful agents are most dangerous. Security requires constraining capability to minimum needed.

## Threat Landscape (as of April 2026)
- 12%+ of ClawHub skills confirmed malicious (1,184–1,467 depending on source)
- 36% contain prompt injection, 91% bundle malware
- Nation-state actors (APT37, Kimsuky, APT28) actively exploiting
- 27% of global instances still unpatched for ClawJacked (CVE-2026-25253)
- ClawHub added VirusTotal scanning Feb 2026 — only for new downloads, not retroactive
