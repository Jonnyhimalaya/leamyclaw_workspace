# NemoClaw — Sandboxed OpenClaw Deployment (NVIDIA)

**Discovered:** 2026-04-23 (Morning Intel)
**Status:** Evaluation candidate

## What Is It
NVIDIA NemoClaw is an open-source reference stack that runs OpenClaw inside NVIDIA OpenShell — a sandboxed container runtime designed for autonomous agents. Released March 16, 2026 (alpha).

- **Repo:** https://github.com/NVIDIA/NemoClaw
- **Part of:** NVIDIA Agent Toolkit
- **License:** Open source

## Why It Matters for the Consultancy
1. **Security boundary** — Process isolation, network restrictions, controlled file access. Goes beyond basic Docker containerisation.
2. **CVE mitigation** — CVE-2026-25253 (WebSocket RCE on localhost) specifically calls for containerisation. NemoClaw provides this out of the box.
3. **Compliance story** — For clients like Dano (ION Group, EY audit Jan 2027) and Kilmurry (guest PII), "NVIDIA-backed security sandbox" is a strong talking point.
4. **Differentiation** — Most OpenClaw deployments are bare metal or basic Docker. Offering NemoClaw as a premium tier separates us from Fiverr setup shops.

## Community Assessment (as of April 2026)
- otterai.net published a decision guide: vanilla OpenClaw vs NemoClaw
- Still in alpha — not production-hardened yet
- Requires evaluation of GPU dependency (does it need NVIDIA hardware?)
- Unknown performance overhead

## Proposed Evaluation Steps
1. Clone repo, deploy on a spare Linode (non-GPU to test CPU-only viability)
2. Run standard OpenClaw workload — Telegram channel, skill execution, web browsing
3. Benchmark: startup time, memory overhead, latency delta vs bare Docker
4. Document compatibility with our current docker-compose patterns
5. If viable: write `consultancy/playbooks/hardened-deployment-nemoclaw.md`

## Tiered Deployment Model (Proposed)
| Tier | Stack | Use Case | Price Point |
|------|-------|----------|-------------|
| Basic | npm install | Dev/testing, single user | Free setup |
| Standard | Docker Compose | SME production, multi-channel | €500 setup |
| Premium | NemoClaw/OpenShell | Sensitive data, compliance, financial | €1,500 setup |

## Decision
Pending evaluation. Priority: medium (after version upgrades and skill scans).
