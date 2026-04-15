# OpenClaw Plugin & Supply Chain Security

**Date:** 2026-04-15
**Source:** OpenClaw Community Intel (April 2026)

## The Threat Landscape
As of April 2026, the OpenClaw ecosystem has experienced a surge in supply chain attacks, primarily targeting the `ClawHub` plugin marketplace. The community is tracking over 138 CVEs related to these plugins, with up to 12% containing malicious code.

**Key risks include:**
- **Unrestricted File Access:** Plugins reading sensitive environment files (`.env`) or SSH keys.
- **Malicious Evals:** Plugins executing remote code via unvalidated inputs or query parameters.
- **Data Exfiltration:** "Atomic Stealer" style campaigns designed to steal wallets, APIs, and credentials.
- **Domain Dominance:** When combined with Active Directory misconfigurations (e.g., related to the `CVE-2026-25253` control UI vulnerability), these plugins can grant attackers full domain takeover.

## The Mitigation Strategy: ClawSafe Audits
"ClawSafe" is a Swiss-operated security service that provides a free automated scanner specifically built for OpenClaw deployments. It analyzes agent repositories and flags hardcoded secrets, dangerous file access patterns, and sandbox escapes.

### Implementation for Consultancy Clients
For all new and existing OpenClaw client deployments, the following steps are mandatory:
1. **Never use blindly-trusted plugins:** Review the source code of any third-party skill or plugin before installation. 
2. **Run ClawSafe Scanning:** Submit the client's OpenClaw configuration repository (e.g., `Jonnyhimalaya/Kilmurry`) to the free ClawSafe scanner at `clawsafe.github.io`.
3. **Review 24-Hour Reports:** ClawSafe generates a PDF report detailing findings (categorized by risk level). Action any high/critical findings (e.g., unrestricted evals) before allowing the agent access to production data or PMS systems like RezLynx.
4. **Enforce Approvals:** Ensure `exec-approvals.json` is correctly set up with host-local `deny` or `allowlist` policies to prevent rogue plugins from escalating privileges on the host.

### Ongoing Maintenance
- During monthly health reviews, re-scan the client's repository using ClawSafe or the open-source equivalent `clawguard`.
- Monitor community alerts for CVEs linked to plugins you have installed.