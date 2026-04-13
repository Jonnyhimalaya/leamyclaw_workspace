# Research: Coolmanns OpenClaw Memory Architecture
**Date:** 2026-04-10
**Source:** github.com/coolmanns/openclaw-memory-architecture (v6), @CoolmannSa on X

## What It Is
A multi-layer memory plugin for OpenClaw that replaces flat MEMORY.md files with structured fact graphs and tiered storage.

## Key Features
- **Hot/Warm/Cool decay tiers** — facts auto-demote based on recency and relevance via daily cron
- **GPU semantic search** — migrated from ONNX CPU to llama.cpp GPU embeddings (~7ms search latency)
- **Graph-memory plugin** — injects relevant facts into prompts dynamically
- **Multilingual support** — useful for international client deployments
- **Activation system** — facts gain/lose activation based on usage patterns

## How It Compares to Our Current Setup
| Feature | Current (QMD + MEMORY.md) | Coolmanns |
|---------|--------------------------|-----------|
| Storage | Flat markdown pointer files | Structured fact graph |
| Search | QMD semantic (vector + BM25) | llama.cpp GPU embeddings |
| Decay | Manual cleanup | Automatic Hot→Warm→Cool cron |
| Scale | Works but bloats over time | Designed for 3K+ facts |
| Integration | Native OpenClaw | Plugin install |

## Compatibility Notes
- Runs as OpenClaw plugin/skill
- Daily cron fits our existing cron pipeline (Scout 5:50, Main 6:00, Strategist 6:15, dreaming 3am)
- Per-agent deployment compatible with Jonny's isolation policy (no cross-agent shared memory)
- Requires GPU for optimal search speed; CPU fallback available but slower

## Consultancy Angle
Could be offered as "Advanced Memory Tier" for enterprise clients who need:
- Long-running agent sessions with context retention
- Multi-topic fact management
- Automatic knowledge decay (compliance: data doesn't persist indefinitely)

## Also From Coolmanns
- **openclaw-guardian** — plugin to block risky tool calls (rm -rf, etc). Worth evaluating for client deployments where safety rails matter.

## Next Steps
1. Clone and review architecture
2. Test on non-production agent
3. Evaluate as consultancy offering if successful
