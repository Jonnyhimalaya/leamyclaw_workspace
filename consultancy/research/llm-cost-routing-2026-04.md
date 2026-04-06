# LLM Cost Routing for OpenClaw — Research Notes
**Date:** 2026-04-06
**Trigger:** Anthropic billing change + rising multi-agent costs

## The Problem
Running multiple agents (Opus, Sonnet, Grok, GPT-5.4) on API billing with no routing intelligence. Every request goes to the assigned model regardless of complexity. A simple file read costs the same as a complex strategic analysis.

## Tools Evaluated

### 1. claw-llm-router (Donn Felker)
- **How it works:** Local classification of request complexity before routing to appropriate model
- **Claims:** 40-80% cost savings
- **Key advantage:** All classification runs locally — no data sent to third parties
- **Published:** Feb 2026, LinkedIn article + GitHub
- **Status:** Proven in community, stable

### 2. ClawRouter (BlockRunAI)
- **How it works:** Analyses each request across 15 dimensions, routes to optimal model
- **Claims:** Up to 92% cost reduction
- **Key advantage:** Most sophisticated routing, open-source
- **Published:** April 4, 2026 (2 days ago)
- **Status:** Very new, needs evaluation. Open source on GitHub.

### 3. Clawzempic (Community)
- **How it works:** Simpler cost-reduction approach (details TBC from ClawHub)
- **Claims:** General cost reduction
- **Key advantage:** Community favourite, simple to deploy
- **Status:** Popular but less documented than alternatives
- **⚠️ Caution:** Sourced from ClawHub — needs security vetting given supply chain risks

### 4. SaladCloud (External)
- **How it works:** Run models on distributed GPU infrastructure instead of API calls
- **Claims:** Significant cost reduction for heavy workloads
- **Published:** Blog guide available
- **Status:** More suitable for high-volume production use cases

## Recommended Approach
1. **Start with claw-llm-router** — proven, local, privacy-preserving
2. **Test on marketing agent first** — highest volume, most variable complexity
3. **Measure for 1 week** — compare costs before/after
4. **Evaluate ClawRouter** after it matures (give it 2-4 weeks)
5. **Skip Clawzempic** until ClawHub supply chain audit is complete

## Architecture Notes
- Our current model assignments: Opus (strategy), Sonnet (site mgmt + marketing), Grok (scouting), GPT-5.4 (content)
- The routing layer would sit between the agent and the provider
- Simple heuristic: if request is <500 tokens and involves file ops/status checks → route to Gemini Flash or similar cheap model
- Complex reasoning, strategic analysis, code generation → keep on assigned premium model

## For Consultancy
This is a packaged offering: "AI Cost Optimization" service for clients running multi-agent setups. We configure routing, measure savings, charge a setup fee. Especially relevant now that Anthropic's billing change is hitting everyone.
