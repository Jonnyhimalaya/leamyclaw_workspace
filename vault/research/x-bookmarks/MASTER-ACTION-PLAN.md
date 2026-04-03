# 🎯 Master Action Plan — From Bookmarks Research
> Created 2026-04-03 · Derived from 55 deep-dived posts + 2 GitHub repos
> All items prioritized by impact and effort

---

## PHASE 1: OPTIMIZE OUR OWN SETUP (2-3 hours)
*Before we sell consulting, our house needs to be best-in-class*

### 1A. Bootstrap Trim ⚡
**Problem:** Our AGENTS.md is 21KB. OnlyTerp's guide says total bootstrap should be 8-15KB. Every extra KB = slower responses + wasted tokens on every single message.

**Plan:**
- [ ] Measure current bootstrap: `wc -c SOUL.md AGENTS.md MEMORY.md TOOLS.md HEARTBEAT.md IDENTITY.md USER.md`
- [ ] Move all reference material from AGENTS.md → `vault/ops/` (git protocols, client infra docs, debugging protocol, standing rules)
- [ ] Keep only: startup sequence, memory protocols, decision rules, safety rules
- [ ] Target: SOUL.md < 1KB, AGENTS.md < 8KB, MEMORY.md < 3KB, total < 15KB
- [ ] Test: compare response speed before/after

**Effort:** 1 hour · **Impact:** 50-70% token savings per message, faster responses

### 1B. Deploy SlowMist Security Guide
**Problem:** We have ad-hoc security. SlowMist offers a structured 3-tier defense matrix with nightly audits.

**Plan:**
- [ ] Download v2.8 guide from GitHub
- [ ] Feed to agent in dedicated session → self-deploy
- [ ] Run red team validation drills
- [ ] Add nightly audit cron (13 metrics)
- [ ] Document what was deployed → update architecture schematic

**Effort:** 30 min · **Impact:** Enterprise-grade security, becomes a client deliverable

### 1C. Deploy openclaw-ops (Cathryn Lavery)
**Problem:** We've hit exec approval blocks, gateway crashes, session bloat, cron silence — all manually diagnosed. Her toolkit automates all of it.

**Plan:**
- [ ] `git clone https://github.com/cathrynlavery/openclaw-ops.git ~/.openclaw/skills/openclaw-ops`
- [ ] Run `bash scripts/heal.sh` for immediate one-shot fix pass
- [ ] Add watchdog cron: `*/5 * * * * bash ~/.openclaw/skills/openclaw-ops/scripts/watchdog.sh >> ~/.openclaw/logs/watchdog.log 2>&1`
- [ ] Run `bash scripts/security-scan.sh` and action findings
- [ ] Compare against our server-health.sh — merge or replace

**Effort:** 15 min · **Impact:** Self-healing ops layer. Prevents recurring breakages we've hit 3+ times.

### 1D. Add Crash Recovery (active-tasks.md)
**Problem:** When sessions crash or /new, in-progress work is lost. Kaostyl's pattern prevents this.

**Plan:**
- [ ] Create `memory/active-tasks.md` — tracks task starts, spawns, completions
- [ ] Add to AGENTS.md startup: check active-tasks.md for incomplete work
- [ ] On task start → log it. On completion → mark done. On crash → resume from last state.

**Effort:** 15 min · **Impact:** Prevents the exact context loss we've experienced

---

## PHASE 2: FIX BROKEN INTEGRATIONS (1-2 hours)

### 2A. Evaluate social-cli for Meta Ads 🔴
**Problem:** Meta integration broken since session expiry. Matt Berman runs his entire Meta Ads system on social-cli for $0/mo.

**Plan:**
- [ ] Research social-cli: `npm install social-cli` or find GitHub repo
- [ ] Test with Leamy Maths Meta Business account
- [ ] If working: build OpenClaw skill wrapping social-cli
- [ ] If working: deploy same for Kilmurry when Kate comes online

**Effort:** 1 hour · **Impact:** Fixes #1 recurring maintenance issue. Autonomous ad management.

### 2B. Run GEO-SEO Claude on All Sites
**Problem:** We have zero visibility into how AI search engines see our clients' sites.

**Plan:**
- [ ] `pip install geo-optimizer-skill`
- [ ] Run audit on leamymaths.ie → save report to artifacts/
- [ ] Run audit on kilmurrylodge.ie → save report
- [ ] Extract action items from both reports
- [ ] Build findings into Kate's AEO dashboard module

**Effort:** 30 min · **Impact:** Immediate client deliverable + informs Kate's dashboard build

---

## PHASE 3: CONSULTANCY ARSENAL (2-3 hours)

### 3A. Clone Reference Repos
**Plan:**
- [ ] `git clone https://github.com/mgonto/executive-assistant-skills` → consultancy/reference/
- [ ] `git clone https://github.com/OnlyTerp/openclaw-optimization-guide` → consultancy/reference/
- [ ] `git clone https://github.com/slowmist/openclaw-security-practice-guide` → consultancy/reference/
- [ ] Extract reusable templates from each

**Effort:** 15 min · **Impact:** Reference implementations for all future client setups

### 3B. Build Critic Agent Skill
**Problem:** All content output needs quality gating. Ole Lehmann's self-correcting system eliminates manual editing.

**Plan:**
- [ ] Create `skills/content-critic/SKILL.md`
- [ ] Include: Voice DNA matching, banned AI-isms list, 3-round review loop
- [ ] Ratings: Needs Work / Good / Excellent
- [ ] Auto-rewrite until "send-ready"
- [ ] Deploy for our Content agent (Pixel), later for Kate

**Effort:** 45 min · **Impact:** All content passes quality gate automatically

### 3C. Bloggersarvesh Local SEO Playbook → Skill
**Problem:** Proven playbook (78 leads in 30 days) sitting in notes, not automated.

**Plan:**
- [ ] Create `skills/local-seo-audit/SKILL.md`
- [ ] 5 steps: keywords → service pages → GBP optimization → proof content → review system
- [ ] Include prompt templates for each step
- [ ] Test on Kilmurry first, then package for all local business clients

**Effort:** 1 hour · **Impact:** Repeatable service offering for any local business client

### 3D. Rimsha's 3-Question Research Framework → Skill
**Plan:**
- [ ] Create `skills/market-research/SKILL.md`
- [ ] The 3 killer questions + 2-hour stress-test methodology
- [ ] Input: competitor URLs, review data, industry reports
- [ ] Output: strategic brief with attack surface, blind spots, opportunities
- [ ] Run first on Kilmurry's market as proof of concept

**Effort:** 30 min · **Impact:** "3-hour deep dive" becomes a packaged consultancy offering

---

## PHASE 4: EVALUATE NEW TOOLS (spread over 1-2 weeks)

### 4A. OpenViking Memory Manager
- [ ] `git clone https://github.com/volcengine/OpenViking`
- [ ] Test tiered loading (L0/L1/L2) with our workspace
- [ ] Compare token usage before/after
- [ ] Decision: adopt or keep current approach

### 4B. Firecrawl for Web Extraction
- [ ] Self-host via Docker
- [ ] Compare against current web_fetch on 5 test URLs
- [ ] Evaluate /interact endpoint for form-filling scenarios
- [ ] Decision: replace web_fetch for structured extraction?

### 4C. Lightpanda for Scraping
- [ ] Docker install, test on 5 non-Cloudflare sites
- [ ] Measure RAM savings vs our Chromium
- [ ] Decision: use for internal scraping to save RAM on 2GB VPS

### 4D. Scrapling for Review Monitoring
- [ ] `pip install scrapling`
- [ ] Test adaptive scraping on TripAdvisor, Google Reviews
- [ ] If stable: build into Kilmurry review monitoring skill

### 4E. Pexo for Video Generation
- [ ] Install from ClawHub (with security vetting)
- [ ] Test: generate a 30-sec property tour clip for Kilmurry
- [ ] Evaluate quality + cost
- [ ] Decision: add to Kate's content toolkit?

---

## PHASE 5: PERSONAL / STRATEGIC (ongoing)

### 5A. Jonny: Claude Certified Architect
- [ ] Find course at anthropic.com or search for "Claude Certified Architect" program
- [ ] Complete certification (free)
- [ ] Add to LinkedIn, consultancy website, business cards
- **Why:** Instant authority. "Claude Certified Architect" is a differentiator.

### 5B. Proactive Mandate for Kate's Agent
- [ ] Adapt Alex Finn's overnight building prompt for hotel marketing context
- [ ] Include in Kate's SOUL.md: nightly social prep, review checking, competitor intel
- [ ] Safety: "create drafts for review, don't publish anything live"

### 5C. Build Consultancy Sales Narrative
Using validated data points from the research:
- "Lenny Rachitsky (500K subscribers) recommends our exact approach"
- "Unmanaged agents are 91% vulnerable to prompt injection" (Runlayer stat)
- "$8K/mo content strategist replaced for $30" (Matt Berman)
- "$30K/year photography savings" (Smart Ape)
- "3-hour market research replacing 3 months" (Rimsha/YC)

### 5D. Follow Key Accounts
Set up monitoring (via intel sweep cron) for:
@johann_sath, @chrysb, @jordymaui, @TheMattBerman, @kaostyl, @steipete, @bloggersarvesh, @mgonto, @floriandarroman

---

## 📊 EFFORT/IMPACT SUMMARY

| Phase | Total Effort | Impact |
|-------|-------------|--------|
| 1. Optimize our setup | 2-3 hrs | 🔴 Token savings, speed, security |
| 2. Fix integrations | 1-2 hrs | 🔴 Unblocks Meta Ads + AEO |
| 3. Build arsenal | 2-3 hrs | 🟡 Repeatable service offerings |
| 4. Evaluate tools | 1-2 weeks | 🟡 Future capabilities |
| 5. Strategic | Ongoing | 🟢 Positioning + credibility |

**Total to reach "best-in-class" setup: ~8 hours of focused work**

---

## QUICK WINS (Can do right now, < 15 min each)
1. Clone the 3 reference repos
2. Measure current bootstrap size
3. Run GEO-SEO on leamymaths.ie
4. Add active-tasks.md crash recovery
5. Search for Claude Certified Architect program link
