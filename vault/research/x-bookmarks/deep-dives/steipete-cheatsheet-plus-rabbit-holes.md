# Peter Steinberger's 50+ OpenClaw Tips (AI Edge Cheatsheet)
> Source: https://x.com/aiedge_/status/2039825229472747704
> 237 likes, 477 bookmarks · Researched 2026-04-03

---

## The Cheatsheet (Full Extraction)

### 1. PLAYFUL ITERATION
- Approach building in a fun, exploratory way
- Start with something you've always wanted to make
- Experiment without expecting instant expertise
- *"Approach it in a playful way… Just play."*

### 2. PROMPT INTO EXISTENCE
- Don't overthink. Use AI to prototype ideas quickly
- Dozens of projects built this way

### 3. IMPERFECTION
- Let go of perfectionism
- Not all code needs to be exactly how you'd write it
- *"I ship code I don't read."*

### 4. CODING & WORKFLOW WITH AI AGENTS
- **Prefer Codex** for large codebases — fewer mistakes, less hand-holding, better long-running execution
- **No plan mode** — instead say "let's discuss" and iterate naturally
- **No MCPs** — use simple CLIs. Agents discover help menus, chain commands. MCPs pollute context. *"MCP is a crutch… everything should be a CLI."*
- **Close the loop** — agents should compile, lint, test, execute, self-verify via local CI
- **Intentional under-prompting** — leave gaps for creative solutions
- **Queue multiple agents** — run 5-10 in parallel like a full dev team
- **Focus on architecture** — prioritize system design, modularity, outcomes over code details
- Most code is boring data transformation — shift focus higher
- *Top engineers optimize for shipping real products*

### 5. RUNNING & OPTIMIZING OPENCLAW

**Tiered model routing:**
- Cheap models for simple tasks, best models for complex reasoning
- Use /model for switching

**Guardrails:**
- Use SKILL.md files
- Add anti-loop rules, checkpoints, summaries

**Persistence:**
- Store knowledge in USER.md, AGENTS.md, MEMORY.md
- Prevents relearning

**Background tasks:**
- Use cron jobs + schedulers (sessions lose state)

**One workflow first:**
- Master a single use case before expanding

**Model quality matters most:**
- Performance depends on LLM reasoning + tool use

### 6. OTHER INSIGHTS
- **Avoid agentic trap** — over-complex workflows produce low-quality slop
- Keep systems simple and conversational
- Real-world usage: flight check-ins, smart home control, life ops via messaging
- OpenClaw moving toward a foundation while advancing agents broadly

---

## 🔥 RABBIT HOLE 1: OpenClaw Optimization Guide (OnlyTerp)
**Repo:** https://github.com/OnlyTerp/openclaw-optimization-guide
**What it is:** 17-part comprehensive optimization guide with benchmarks and templates

### Key Numbers (Before → After):
| Metric | Before | After |
|--------|--------|-------|
| Context per msg | 15-20 KB | 4-5 KB |
| Time to respond | 4-8 sec | 1-2 sec |
| Memory recall | Forgets daily | Remembers weeks |
| Token cost/msg | ~5,000 tokens | ~1,500 tokens |
| Long sessions | Degrades | Stable |
| Concurrent tasks | One at a time | Multiple parallel |

### Core Architecture (matching our approach):
- SOUL.md: < 1KB (personality, tone, core rules only)
- AGENTS.md: 2-10KB (decision tree, tool routing, operational protocols)
- MEMORY.md: < 3KB (pointers only, NOT full docs)
- TOOLS.md: < 1KB (tool names + one-liner usage)
- **Total per message: 8-15KB** (with operational protocols)

### Key Principle: 
> "Workspace files become lightweight routers, not storage. All knowledge lives in a local vector database. The bot loads only what it needs."

### 17 Parts Cover:
1. Speed — trim context files, add fallbacks
2. Context Bloat — quadratic scaling, built-in defenses
3. Cron Session Bloat — session file cleanup
4. Memory — 3-tier system + Ollama vector search
5. Orchestration — CEO/COO/Worker model
6. Models — provider comparison, pricing, local
7. Web Search — Tavily, Brave, Serper, Gemini grounding
8. One-Shotting Big Tasks — research-first methodology
9. Vault Memory System — structured knowledge graph, MOCs
10. State-of-the-Art Embeddings — Qwen3-VL, Stark Edition
11. Auto-Capture Hook — automatic knowledge extraction post-session
12. Self-Improving System — micro-learning loop, $0/day
13. Memory Bridge — give coding agents vault access
14. Quick Checklist — 30-minute setup
15. Infrastructure Hardening — compaction crash loops, GPU, gateway fixes
16. autoDream Memory Consolidation — from Claude Code leaked source
17. One-Shot Prompt — copy-paste automation for entire setup

### 🎯 Critical Takeaway for Us:
**Our AGENTS.md is 21KB+ — that's DOUBLE the recommended max.** This confirms what Polydao said. We need to:
1. Audit and ruthlessly trim AGENTS.md
2. Move reference material to vault/ (fetched on demand via memory_search)
3. Keep only decision-tree logic and operational protocols in AGENTS.md
4. Target: SOUL.md < 1KB, AGENTS.md < 10KB, MEMORY.md < 3KB

---

## 🔥 RABBIT HOLE 2: SlowMist Security Practice Guide
**Repo:** https://github.com/slowmist/openclaw-security-practice-guide
**What it is:** Enterprise-grade security guide by SlowMist (blockchain security firm). Agent-facing, not just human checklist.

### Paradigm Shift:
Traditional "host-based static defense" → **"Agentic Zero-Trust Architecture"**

### 3-Tier Defense Matrix:
1. **Pre-action:** Behavior blacklists + strict Skill installation audit (anti-supply chain poisoning)
2. **In-action:** Permission narrowing + cross-skill pre-flight checks (business risk control)
3. **Post-action:** Nightly automated audits (13 core metrics) + Brain Git disaster recovery

### Deployment Method (Brilliant):
1. Drop the markdown guide directly into chat with your agent
2. Agent reads, evaluates, identifies conflicts
3. Agent deploys the defense matrix itself
4. Run red team validation drills after

### v2.8 Enhancements:
- Agent-Assisted Deployment Workflow (5-step automated)
- --light-context cron protection (prevents workspace context hijacking audit sessions)
- Persistent security reports ($OC/security-reports/, 30-day rotation)
- Post-upgrade baseline rebuild process
- Enhanced code review protocol
- Token optimization (bash pre-filtering before LLM processing)
- 7 production pitfall records (real-world lessons)

### Red Teaming Guide:
Includes end-to-end defense testing to ensure the agent doesn't bypass its own defenses out of "obedience"

### 🎯 Critical Takeaway for Us:
1. **We should deploy this guide on our server** — drop it in chat, let the agent self-harden
2. **For Kilmurry:** Same process. Agent reads guide → self-deploys defenses
3. **For consultancy:** This is a DELIVERABLE. "We deploy SlowMist's security practice guide on your agent" is a line item that sounds incredibly professional
4. **The nightly audit cron** (13 metrics) is something we should add immediately
5. **Red team testing** should be part of our post-deployment checklist for every client

---

## Reply Thread Gems

### @hex_agent:
> "Separate your SOUL.md (who the agent is) from AGENTS.md (how it works). Cramming both into one file is why most agents feel inconsistent — identity drifts when it's mixed with instructions."

**Verdict:** We already do this. ✅

### @Samward:
> "The Crab Trap concept is the part most people will overlook..."

**Crab Trap = one agent works, another audits.** This is our Advisor cron pattern. ✅

---

## Updated Action Items

### 🔴 IMMEDIATE

**A. Clone OnlyTerp Optimization Guide**
```bash
cd ~/consultancy/reference/
git clone https://github.com/OnlyTerp/openclaw-optimization-guide
```
- Extract templates, vault structure, one-shot prompt
- Compare our setup against their benchmarks
- Target: reduce our context injection from ~21KB to <15KB

**B. Deploy SlowMist Security Guide**
- Download v2.8 guide
- Feed it to our agent in a dedicated session
- Let it self-deploy the defense matrix
- Run red team validation
- Then do the same for Kilmurry

**C. Audit Our Bootstrap Size (URGENT)**
- Measure exact token count of SOUL.md + AGENTS.md + MEMORY.md + TOOLS.md + HEARTBEAT.md
- Compare against OnlyTerp's targets
- Create trimming plan
