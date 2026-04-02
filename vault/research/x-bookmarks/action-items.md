# Action Items from Bookmark Research
> Generated 2026-04-02 from Batch 1 deep dives

## 🔴 IMMEDIATE (This Week)

### 1. Evaluate social-cli for Meta Ads
- **Why:** Our Meta integration is broken (session expired). Matt Berman runs his entire Meta Ads system on it for $0/mo. Handles token refresh, pagination, rate limits.
- **Action:** `npm install social-cli` or check GitHub for @vishalojha_me's repo. Test with our Meta Business account.
- **Impact:** Fixes our #1 recurring maintenance issue with Meta

### 2. Run GEO-SEO Claude on leamymaths.ie + kilmurrylodge.ie
- **Why:** Free AI search visibility audit. Kate's AEO module should wrap this tool.
- **Action:** `pip install geo-optimizer-skill`, run audit, save results to artifacts/
- **Impact:** Immediate client deliverable + informs Kate's dashboard build

### 3. Clone Gonto's EA Skills Repo
- **Why:** Reference implementation for client agent setups. Declarative skills + isolated crons.
- **Action:** `git clone https://github.com/mgonto/executive-assistant-skills` into consultancy/reference/
- **Impact:** Accelerates Kate's setup + future client templates

### 4. Add active-tasks.md Crash Recovery Pattern
- **Why:** Kaostyl's pattern — tracks task starts/spawns/completions, auto-resumes on restart.
- **Action:** Add `memory/active-tasks.md` to AGENTS.md startup protocol
- **Impact:** Prevents lost work on session crashes (we've lost context before)

## 🟡 THIS SPRINT (Next 2 Weeks)

### 5. Evaluate OpenViking Memory Manager
- **Why:** ByteDance's context database with tiered loading (L0/L1/L2). 50%+ token savings. 10K+ GitHub stars.
- **Action:** Install, test with our workspace, compare token usage before/after
- **Impact:** Could revolutionize our memory architecture for all agents

### 6. Audit Bootstrap Size
- **Why:** Polydao's analysis — bootstrap files inject 3-5K tokens per message. Our AGENTS.md alone is 21K chars.
- **Action:** Measure exact token cost of our bootstrap. Trim AGENTS.md ruthlessly. Move reference material to memory/ where it's fetched on demand.
- **Impact:** 20-40% token savings per session

### 7. Script-Back Critical Agent Rules
- **Why:** Jordymaui confirmed 40% instruction drift. Language suggests, code enforces.
- **Action:** Identify top 5 "driftable" rules in AGENTS.md, create validation scripts
- **Impact:** Reliability improvement for critical workflows

### 8. Install Context Hub (chub) for Coding Agents
- **Why:** Andrew Ng's tool — gives coding agents up-to-date API docs. Reduces hallucination.
- **Action:** `npm install -g @aisuite/chub`, add to coding-agent skill
- **Impact:** Better code quality from sub-agents

## 🟢 BACKLOG

### 9. Evaluate Lightpanda for Internal Scraping
- Replace Chromium for non-authenticated scraping. 11x faster, 9x less RAM.
- Caveat: Beta, no stealth. Good for friendly sites only.

### 10. Evaluate Scrapling for Review Scraping
- Adaptive scraper that survives site redesigns. Good for Kilmurry review monitoring.
- `pip install scrapling`

### 11. Evaluate AlphaClaw for Non-Technical Clients
- GUI wrapper for Kate? Let her see agent status without SSH.
- Check if it adds value vs just giving her Telegram access.

### 12. Build AutoReason Debate Skill
- For high-stakes content: agent debate loop → blind judge → iterate until convergence.
- Use for marketing copy, strategy docs, client deliverables.

### 13. Study VirloMain + ScrapeCreators for Content Module
- Matt Berman's content strategist system. Could power Kate's competitive intel.

## 🟡 FROM BATCH 2 (New This Sprint Items)

### 14. Jonny: Get Claude Certified Architect (FREE)
- **Why:** Anthropic's free certification. "Highest paid AI job." Instant credibility for consultancy.
- **Action:** Find the course at anthropic.com/education or similar, complete it
- **Impact:** "Claude Certified Architect" on business cards/website

### 15. Run Rimsha's 3-Question Framework on Kilmurry
- **Why:** YC founder's method for compressing months of market research into 3 hours
- **Questions:** (1) What does every successful boutique hotel understand that guests never say? (2) What 3 assumptions is the Limerick hotel market built on? (3) 5 investor-level challenges to Kilmurry's strategy.
- **Impact:** Produces insights for Jack that feel like expensive consulting

### 16. Build Critic Agent Skill for Content Pipeline
- **Why:** Ole Lehmann's self-correcting writing system. Voice DNA + critic protocol = no manual editing.
- **Action:** Create critic.md skill with banned AI-isms list, voice matching, 3-round review loop
- **Impact:** All content output passes quality gate before delivery

### 17. Implement Bloggersarvesh Local SEO Playbook for Kilmurry
- **Why:** 5-step system that generated 78 leads in 30 days. Directly applicable to hotels.
- **Steps:** Keywords → service area pages → GBP optimization → proof content → review system
- **Impact:** Kate's SEO/AEO module gets a proven framework

### 18. Evaluate Firecrawl for Web Extraction
- **Why:** 100K GitHub stars, YC-backed. Better than web_fetch for structured extraction.
- **Action:** Self-host via Docker, test against current web_fetch quality
- **Impact:** Improved data quality for research + competitor monitoring

### 19. Add Proactive Mandate to Kate's SOUL.md
- **Why:** Alex Finn's overnight building prompt works. Adapted version for Kate's marketing agent.
- **Action:** Include in Kate's setup: "Every night, prepare tomorrow's social posts, check reviews, update competitor intel."
- **Impact:** Kate wakes up to work done, not work to do

## 📊 Consultancy Positioning Updates

### Add to Sales Materials:
- "Lenny Rachitsky's 500K-subscriber newsletter validates our exact approach"
- "We implement the patterns that Kaostyl's viral thread (3.6K bookmarks) describes"
- "Our clients get the $8K/mo content strategist result for $30/mo in API costs"
- Reference Polydao's "architecture not chatbot" framing
- "Your unmanaged AI agents are 91% vulnerable to prompt injection" (Runlayer stat)
- Chrys Bader's $4,200 car negotiation story as viral demo
- Brand photography replacement ($30K savings) as killer hook for hospitality

### Pricing Validation Points:
- Gonto: $250-300/mo for AI EA (vs $1,500 human)
- Matt Berman: $30/mo replaces $8K/mo strategist
- Florian: $4.8K MRR from 300 founders at ~$16/mo
- Smart Ape: $30K/year photography savings
- Boring Marketer → Hermes migration = what happens without proper setup
- Our managed service: $2-5K setup + $200-500/mo maintenance (justified by above)

### New Service Lines Identified:
1. **Brand Photography Replacement** — $30K savings pitch for hotels/restaurants
2. **Local SEO Automation** — 5-step playbook for any local business
3. **Research-as-a-Service** — 3-hour deep dive replacing months of discovery
4. **Content Critic Pipeline** — self-correcting AI writing system
5. **Enterprise Security Audit** — "your agents are 91% vulnerable" hook
