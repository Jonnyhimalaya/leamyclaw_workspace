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

## 📊 Consultancy Positioning Updates

### Add to Sales Materials:
- "Lenny Rachitsky's 500K-subscriber newsletter validates our exact approach"
- "We implement the patterns that Kaostyl's viral thread (3.6K bookmarks) describes"
- "Our clients get the $8K/mo content strategist result for $30/mo in API costs"
- Reference Polydao's "architecture not chatbot" framing

### Pricing Validation Points:
- Gonto: $250-300/mo for AI EA (vs $1,500 human)
- Matt Berman: $30/mo replaces $8K/mo strategist
- Florian: $4.8K MRR from 300 founders at ~$16/mo
- Our managed service: $2-5K setup + $200-500/mo maintenance (justified by above)
