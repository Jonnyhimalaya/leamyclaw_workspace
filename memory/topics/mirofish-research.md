# MiroFish — Research Brief
_Researched: 2026-04-13_

## What It Is
MiroFish is an open-source **swarm intelligence prediction engine**. Instead of asking one LLM to predict an outcome, it builds a miniature digital society of thousands of autonomous AI agents — each with unique personalities, long-term memories, and social relationships — and lets them interact. The collective emergent behaviour produces a structured prediction report.

Built in 10 days by Guo Hangjiang ("Baifu"), a 20-year-old student at Beijing University of Posts and Telecommunications. Predecessor was BettaFish (public opinion analysis). Backed by Shanda Group (Chen Tianqiao, formerly China's richest man) who committed ~$4.1M (30M yuan) within 24 hours of seeing the demo video.

**GitHub:** https://github.com/666ghj/MiroFish  
**Stars:** 33,000+ as of Apr 2026 — topped GitHub global trending  
**Status:** v0.1.2, early stage, APIs may change  
**Licence:** Open source (MIT-ish)

---

## How It Works — The 5-Stage Pipeline

1. **Graph Building** — Upload seed material (news article, financial report, policy draft, novel, anything). GraphRAG extracts entities and relationships → knowledge graph. Individual + collective memories injected.

2. **World Building** — Environment Configuration Agent reads the graph, generates simulation parameters: agent personas, social environment, starting conditions. Agents reflect demographics, power structures, cultural context of the seed material.

3. **Simulation** — Runs on dual-platform parallel architecture. Agents post, react, debate, form coalitions, change minds. Each agent's memory updates per round via Zep Cloud. You can inject new variables mid-run from a "God View" (drop in a breaking news event, watch how the world responds).

4. **Report Generation** — Report Agent produces a structured prediction report: emergent patterns, majority/minority opinion paths, likely event sequences, confidence levels.

5. **Deep Interaction** — The world stays live after simulation. Chat directly with any individual agent ("What's your view as a simulated hotel GM?"). Interrogate the Report Agent for further analysis. Run counterfactuals.

**Powered by:** OASIS (Open Agent Social Interaction Simulations) from CAMEL-AI. MiroFish adds the full product layer on top.

---

## Tech Stack
- **Frontend:** Vue.js, Node.js 18+
- **Backend:** Python 3.11-3.12, FastAPI
- **Knowledge graph:** GraphRAG
- **Agent memory:** Zep Cloud (free tier sufficient for basic use)
- **LLM backend:** Any OpenAI-compatible API — default config uses Alibaba Qwen-plus via Bailian Platform
- **Deployment:** Source code or Docker

**Offline fork exists:** `nikmcfly/MiroFish-Offline` — replaces cloud dependencies with Ollama (local LLM) + Neo4j Community Edition. Fully air-gapped. Important for data-sensitive clients.

---

## Costs
Costs depend on agent count, simulation rounds, and model choice:

| Run size | Cost (standard model) | Cost (budget model e.g. Gemini Flash) |
|---|---|---|
| 50 agents × 20 rounds | $0.50 – $2 | < $0.50 |
| 500 agents × 40 rounds | $8 – $25 | $2 – $5 |
| 1,000 agents × 100 rounds | $40 – $120 | $5 – $20 |
| 1,000 agents × 1,000 rounds (full scale) | ~$1,000 | $100–200 |

**Key lever:** Model choice. Qwen-plus default is reasonable. Gemini Flash or DeepSeek bring large runs into affordable territory.

Zep Cloud: free tier is sufficient for standard usage.

---

## Use Cases

### Public Opinion / Crisis Simulation
- How will customers react to a price increase?
- How will guests respond to a hotel renovation announcement?
- How will staff respond to a restructure?
- PR scenario planning before going public

### Financial / Market Modelling
- How will investor sentiment spread after an earnings surprise?
- Narrative spread modelling (how a story travels through different agent types)

### Business Decision Support
- Product launch reaction before committing marketing budget
- Competitive scenario planning (how will competitor agents respond to our move?)
- Organisational change simulation (new leadership, acquisition)

### Creative / Narrative
- Already demonstrated: fed first 80 chapters of Dream of the Red Chamber → simulated probable ending through emergent agent behaviour
- Screenwriting, game narrative, interactive fiction

### Hospitality (Kilmurry angle)
- Simulate guest community reaction to a new pricing strategy, room type launch, or venue opening (CASK, The Residence)
- "What if we raise rack rates by 15% in Q3?" → simulate how different guest segments (corporate, leisure, wedding) respond
- Simulate how a negative TripAdvisor review spread affects booking intent across different traveller profiles

---

## Strengths
- **Genuinely novel approach** — not a single-LLM prediction, actual emergent collective behaviour
- **Open source + self-hostable** — full data sovereignty option via offline fork
- **Interactive world** — stays live after simulation, can probe individual agents
- **Fast to prototype** — Docker deploy, cheap small runs
- **Model-agnostic** — works with any OpenAI-compatible API

## Weaknesses / Risks
- **Accuracy unproven at scale** — no rigorous benchmarks published. "We don't know if predictions are better than random for any specific use case" (Medium, Mar 2026)
- **Early stage (v0.1.2)** — APIs changing, not production-hardened
- **Cost at scale** — 1,000 agent runs get expensive fast with premium models
- **Chinese project/backing** — Shanda Group = Chinese internet company. Data sovereignty question for enterprise clients. Offline fork mitigates this.
- **OASIS dependency** — simulation engine is CAMEL-AI's OASIS. Bugs there affect MiroFish.
- **Zep Cloud dependency** (unless using offline fork)

---

## Relevance to Us

### For Kilmurry / Hospitality Clients
High potential for scenario planning. Jack asking "how will guests respond to X?" is exactly the use case. Small runs ($2-10) could produce genuinely useful intelligence on pricing, venue launches, or reputation events.

### For Consultancy
Could be positioned as a premium add-on: "AI scenario planning" service. Run simulations for clients pre-launch. Results packaged as a deliverable.

### For Leamy Maths
Less obvious fit — could simulate student/parent community response to pricing changes or new course formats, but probably overkill.

### Integration Angle
Could sit alongside OpenClaw rather than replace anything. OpenClaw orchestrates the bot workflow; MiroFish gets called for specific "what if?" prediction tasks. Could be triggered from Mission Control as an intelligence tool.

---

## Next Steps to Evaluate
- [ ] Spin up a test instance (Docker, cheapest model)
- [ ] Run a small Kilmurry scenario (e.g. "Kilmurry raises weekend rack rate by 20% — how does guest sentiment spread?")
- [ ] Evaluate output quality vs cost
- [ ] Assess offline fork viability for data-sensitive use

## Sources
- GitHub: https://github.com/666ghj/MiroFish
- Beitroot deep breakdown: https://www.beitroot.co/blog/mirofish-open-source-swarm-intelligence-engine
- Blocmates origin story: https://www.blocmates.com/articles/what-is-mirofish-the-agent-engine-that-can-predict-anything-and-everything
- Emelia.io: https://emelia.io/hub/mirofish-ai-swarm-prediction
- Offline fork: https://github.com/nikmcfly/MiroFish-Offline
