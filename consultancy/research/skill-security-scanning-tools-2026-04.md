# OpenClaw Skill Security Scanning Tools — April 2026

## Context
ClawHub supply chain risk is significant: Snyk ToxicSkills report (April 2026) found 91% of malicious skills bundle malware, 36% contain prompt injection. 12%+ of ClawHub plugins confirmed malicious (341-1,467 confirmed, 35k+ downloads). ClawHub added VirusTotal scanning Feb 2026 but only for new downloads — existing installs are unscanned.

## Available Tools

### 1. Built-in: `openclaw skill-scan`
- **What:** Native OpenClaw CLI command for scanning installed skills
- **Pros:** No extra installation, built into the platform
- **Cons:** Limited documentation on detection capabilities
- **Use case:** Post-deployment verification on client instances
- **Command:** `openclaw skill-scan`

### 2. Bitdefender AI Skills Checker (Free)
- **URL:** https://www.bitdefender.com/en-us/consumer/ai-skills-checker
- **What:** Cloud-based, AI-powered security scanner for OpenClaw skills
- **Detects:** Hidden backdoors, data exfiltration logic, prompt injection vectors, obfuscation techniques, suspicious file/system operations
- **Pros:** Free, no installation, AI-powered pattern detection beyond simple regex
- **Cons:** Cloud-based (skills uploaded to Bitdefender servers — consider data sensitivity)
- **Use case:** Pre-install vetting of any ClawHub skill before deploying to client

### 3. clawvet (Open Source)
- **URL:** https://github.com/MohibShaikh/clawvet
- **What:** 6-pass security scanner with unit, integration, regex safety, and CLI end-to-end tests
- **Pros:** Open source, CI/CD integration via GitHub Actions, JSON output format
- **Cons:** Requires npm install, community-maintained
- **Use case:** CI/CD pipeline integration for clients with skill repos
- **Command:** `npx clawvet scan ./my-skill --format json --fail-on high`

### 4. anikrahman0/security-skill-scanner (Open Source)
- **URL:** https://github.com/anikrahman0/security-skill-scanner
- **What:** Detects credential harvesting, external downloads, suspicious APIs, shell injection
- **Pros:** Focused detection patterns, open source
- **Use case:** Additional scanning layer for high-security deployments

## Recommended Consultancy Process

1. **Pre-install (any ClawHub skill):** Run through Bitdefender AI Skills Checker
2. **Post-deployment:** Run `openclaw skill-scan` on the instance
3. **For CI/CD clients:** Add clawvet to GitHub Actions pipeline with `--fail-on high`
4. **Periodic audit:** Run `openclaw skill-scan` monthly or after any skill updates

## Integration with Consultancy Security Checklist
Add these as concrete tools for the existing "skill scan" checklist item:
- ☐ Pre-install: Bitdefender AI Skills Checker passed
- ☐ Post-install: `openclaw skill-scan` clean
- ☐ CI/CD: clawvet integrated (if applicable)
