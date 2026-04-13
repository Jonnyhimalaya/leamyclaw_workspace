# Gemma 4 as Local Model for OpenClaw Deployments
**Created:** 2026-04-09
**Status:** Evaluation / Research

## Overview
Google's Gemma 4, released April 2, 2026 under Apache 2.0, is the first open-weight model viable as a primary local backend for OpenClaw agent workflows.

## Key Specs
- **Architecture:** Mixture-of-Experts (MoE)
- **Sizes:** 4B, 12B, 26B (MoE)
- **Tool-use benchmark:** 85.5% on τ2-bench (26B MoE) — competitive with cloud APIs
- **Multimodal:** Text + images natively; audio on larger variants
- **License:** Apache 2.0 — full commercial use, no restrictions
- **Function calling:** Native structured tool use — critical for OpenClaw skills

## Hardware Requirements
| Model | VRAM (GPU) | RAM (CPU mode) | Recommended For |
|-------|-----------|----------------|-----------------|
| 4B | ~3GB | 8GB | Mobile, embedded, very basic tasks |
| 12B | ~8GB | 16GB | **Sweet spot for SME clients** — good tool-use + runs on decent desktop |
| 26B MoE | ~16GB | 32GB | Best quality, needs workstation-class hardware |

## OpenClaw Integration
- Provider: `ollama`
- Install: `ollama pull gemma4:12b` (or `gemma4:26b`)
- Config in openclaw.json: set default or per-agent model to `ollama/gemma4:12b`
- Works with existing skills, function calling, and tool routing
- Can be set as failover model so agents degrade gracefully when API credits deplete

## Consultancy Application
### Budget Tier Offering
- Client has a desktop/workstation with 16GB+ RAM
- Deploy OpenClaw + Ollama + Gemma 4 12B
- Zero ongoing API costs
- Good enough for: scheduling, email triage, basic content generation, data lookups
- Not good enough for: complex multi-step reasoning, long-form content, code generation

### Failover Strategy
- Primary: Cloud API (GPT-5.4, Sonnet, etc.)
- Failover: Local Gemma 4
- Benefit: Agents never go fully offline — they degrade instead of dying
- Config: OpenClaw model routing with priority list

## Limitations
- Our VPS (37-40% RAM usage) cannot run it — no spare capacity
- Inference speed on CPU is slow (~5-15 tokens/sec on 12B)
- Quality gap vs Opus/GPT-5.4 for complex reasoning tasks
- No fine-tuning ecosystem yet (too new)

## Sources
- HuggingFace blog: huggingface.co/blog/gemma4
- DeepMind model card: deepmind.google/models/gemma/gemma-4/
- Setup guide: lushbinary.com/blog/openclaw-gemma-4-local-ai-agent-ollama-setup-guide-2026/
