# Deep Dive Research — Batch 2 (Remaining Posts)
> Researched 2026-04-02 · 40 remaining posts expanded

---

## 🤖 MULTI-AGENT & AUTONOMOUS SYSTEMS

### Paperclip — AI Company with Zero Employees
**Sources:** Bookmarks #3, #6, #22
- Full AI team: CEO, engineers, QA delegating autonomously
- Greg Isenberg met the anonymous creator — "one of the FASTEST growing open-source projects in AI"
- PaperClick adds org chart, roles, bosses, and approvals layer
- **Verdict:** Interesting concept but over-hyped. Our multi-agent team (5 agents, real roles, real output) is more practical. The org-chart/approval layer idea is worth stealing though.

### The Agency — 147 Agents, 12 Divisions
**Source:** Bookmark #17 · [GitHub](https://github.com/msitarzewski/agency-agents/)
- MIT-licensed, 50K stars in 2 weeks from a Reddit thread
- Each agent: unique personality, workflow, mission, success metrics, production code examples
- Works with Claude Code, Copilot, Gemini CLI, Cursor, OpenCode
- YAML frontmatter + Lua-style Markdown templates
- **Verdict:** Mostly prompt templates, not orchestration. But the *structure* (personality + workflow + success metrics per agent) is smart. We should adopt this pattern for documenting our agents more formally.

### ACP Agent Config (Hidden Feature)
**Source:** Bookmark #31 · @ziwenxu_
**Exact config:**
```json
"acpx": {
  "enabled": true,
  "dispatch": {"enabled": true},
  "backend": "acpx",
  "defaultAgent": "claude",
  "allowAgents": ["claude", "codex", "opencode"],
  "maxConcurrentSessions": 8,
  "config": {
    "permissionMode": "approve-all",
    "nonInteractivePermissions": "fail"
  }
}
```
- Lets OpenClaw tap into Claude Code, Codex, OpenCode natively
- Saves tokens by avoiding endless back-and-forth
- **Verdict:** We already use ACP — but should verify our config matches this. The `maxConcurrentSessions: 8` is worth checking against our setup.

---

## 📈 MARKETING, SEO & BUSINESS

### Alex Finn's Proactive Prompt (Overnight Building)
**Source:** Bookmark #7
**The full prompt:**
> "I am a 1 man business. I work from the moment I wake up to the moment I go to sleep. I need an employee taking as much off my plate and being as proactive as possible. Please take everything you know about me and just do work you think would make my life easier or improve my business and make me money. I want to wake up every morning and be like 'wow, you got a lot done while I was sleeping.' Don't be afraid to monitor my business and build things that would help improve our workflow. Just create PRs for me to review, don't push anything live. I'll test and commit. Every night when I go to bed, build something cool out I can test."

**Key safety rails:**
- DON'T commit code (if GitHub-connected)
- DON'T delete files
- Use Codex CLI for code writing to save Claude Max tokens
- **🎯 Takeaway:** This is essentially what we already do with HEARTBEAT.md + crons, but formalized as a proactive mandate. Worth adding a version of this to Kate's SOUL.md. The "create PRs, don't push live" pattern is excellent client safety.

### Brand Photography Replacement ($30K Saved)
**Source:** Bookmark #8 · @the_smart_ape
**The system:**
1. Give Claude Code: browser MCP + image gen API
2. Feed brand URL → agent crawls every page → builds "Brand DNA" doc (hex colors, fonts, photo style, catalog)
3. Drop reference images (Pinterest boards, editorials) → agent deconstructs (lighting, color grade, composition) → generates prompts
4. Combine Brand DNA + references → generate consistent product shots
5. Old: photographer $100-300/h + studio $500/day + editing $50/img
6. New: Claude $20/mo + image API ~$0.10/shot

**🎯 Takeaway:** This is a *killer* consultancy offering. Kilmurry Lodge spends on photography. Kate should know this is possible. Even if the output isn't 100% perfect, it covers 80% of routine product/property shots.

### Firecrawl — "AWS for Web Data"
**Source:** Bookmark #10 · 100K+ GitHub stars
- YC S22 startup, built by Mendable AI team
- URL → clean markdown, JSON, screenshots
- Agent endpoint: natural language queries → structured data
- Browser sandbox: AI automates clicks, forms, logins
- Works with OpenClaw, Claude, LangChain, n8n
- Self-hostable via Docker
- **🎯 Takeaway:** Better than our current web_fetch for structured extraction. The /interact endpoint (clicks, forms, logins with persistent sessions) could replace some browser automation. Evaluate for replacing Brave/SearXNG for certain tasks. Free credits available via n8n partnership.

### Bloggersarvesh — Local SEO Playbook
**Sources:** Bookmarks #53, #92, #94
**The 5-step system (under $100/mo):**
1. **Keywords:** Claude generates "service + location", "near me", emergency, comparison terms
2. **Service Area Pages:** Claude drafts per-area pages (offer, prices, process, photos, reviews, FAQs, CTA)
3. **GBP Optimization:** AI-generated description, services, 20 FAQs, weekly posts
4. **Proof Content:** 1 job → 10 assets (case study, GBP post, Reel script, FAQ update)
5. **Reviews:** Claude writes request texts & reply templates

**Claims:** 78 extra leads in 30 days on GBP. Outrank local business in 60 days.
**Stack:** Claude $20-30/mo + GBP (free) + WordPress + Canva/CapCut + GSC/Analytics (free)

**🎯 Takeaway:** This is DIRECTLY applicable to Kilmurry Lodge. Kate's modules 2 (SEO/AEO) and 5 (Reviews) should implement this playbook. The "1 job → 10 assets" pattern is brilliant for hotel content (1 event → blog + GBP post + social + email + review request).

### Min Choi — 7 X Strategy Use Cases
**Source:** Bookmark #27
1. Content creators → auto-draft from trending AI news
2. Founders → monitor competitors + alerts
3. Newsletter writers → curate daily research queue
4. Day traders → scan market-moving announcements
5. Developers → automate workflows via cron
6. Solopreneurs → full content team of 1
7. "Me → all of the above"

**Notable:** Also flagged "RIP OpenClaw" as Claude adds native scheduling/agents features. Interesting competitive dynamic to watch.

### Rimsha — Month of Research in 3 Hours
**Source:** Bookmark #46
**The YC founder's method (3 killer questions):**
1. "What does every successful player in this market understand that their customers never say out loud?" (not "summarize" or "analyze")
2. "Show me the 3 assumptions this entire market is built on, and what would have to be true for each one to be wrong." (attack surface of entire industry)
3. "Write 5 questions a world-class investor would ask to destroy this business idea, then answer each one using only the evidence in these documents."

**Then 2 hours stress-testing:** "What's the strongest version of this argument and where does it still break?"

**🎯 Takeaway:** These 3 questions are gold for our consultancy discovery process. Before we onboard any client, we should run this framework on their industry. For Kilmurry: "What does every successful boutique hotel understand that guests never say out loud?" Would produce incredible insights.

### Ole Lehmann — Self-Correcting AI Writing
**Source:** Bookmark #67
**The system:**
1. **Voice DNA file** — banned AI-isms (delve, game-changer, etc.) + your writing samples
2. **Critic Agent Protocol** (save as critic.md) — spawns sub-agent to review against voice rules
3. Rates output: Needs Work / Good / Excellent
4. Rewrites up to 3 rounds until "send-ready"
5. **Feedback logs** that adapt over sessions

**🎯 Takeaway:** We should build a critic skill for our content agent (Pixel). Every piece of content should pass through a critic before delivery. The Voice DNA concept is excellent for Kate — her agent should learn her writing voice and enforce it.

---

## 🏢 BUSINESS & ENTERPRISE

### Chrys Bader (AlphaClaw) — Real Founder Use Cases
**Source:** Bookmark #75
**Most impressive claims from his Rosebud ($2.5M ARR) usage:**
- Negotiated $4,200 off a car via email overnight
- Filed legal rebuttal that reopened an insurance claim
- Cleared 10K emails + 122 slides in one session
- Ad creative pipeline: ideation → Meta ads publishing in Slack
- BigQuery analytics: natural language → charts (no SQL)
- Recruited 30 candidates from LinkedIn, ranked by fit

**🎯 Takeaway:** The car negotiation and insurance claim stories are PERFECT consultancy sales stories. "Your AI agent negotiated $4,200 off a car purchase while you slept." That's the kind of headline that sells.

### OpenClaw for Enterprise (Runlayer)
**Source:** Bookmark #90 · @berman66
- Employees installing OpenClaw shadow-style = security nightmare
- Full shell access, no sandboxing, zero visibility
- 91% vulnerable to prompt injection attacks out of box
- Runlayer provides guardrails: discovers agents, blocks injections in <100ms
- Improves injection resistance from 8.7% to 95%
- Powers Gusto, Instacart

**🎯 Takeaway:** This is our security hardening playbook VALIDATED by an enterprise vendor. Our security playbook already covers most of what Runlayer sells. Positioning: "Enterprise-grade security without the enterprise price tag." The 91% injection vulnerability stat is powerful for sales conversations.

### Boring Marketer — Evolution of Opinion
**Source:** Bookmark #74
**Feb 21:** Enthusiastic — "Sonnet 4.6 daily driver, spawn subagents, SSH into VPS"
**Mar 6:** Shifted to GPT 5.4 as default ("big intelligence upgrade from Sonnet")
**Mar 27:** "Anyone feel themselves using OpenClaw less? Memory not great, tool use not close to Claude Code"
**Mar 30:** Moved to Hermes — "the blocker was OpenClaw wasn't capable enough for ownership of stuff"

**🎯 Takeaway:** This evolution is the EXACT trajectory a frustrated user follows. Memory problems + tool use limitations drive churn. Our memory architecture (daily logs + MEMORY.md + heartbeats + checkpoints) solves exactly what he's complaining about. This is our differentiation story.

---

## 🔧 TOOLS & PLUGINS

### Pexo — Video Generation via Chat
**Source:** Bookmark #16
- ClawHub skill for video generation inside Telegram/Discord/WhatsApp
- Auto-picks best model per scene (Sora, Kling, Seedance)
- Handles storyboarding, scene gen, editing, music, pacing
- Up to ~2 min videos, multiple formats (16:9, 9:16, 1:1)
- **⚠️ ClawHub risk:** ~12% malicious skills reported. Vet before install.
- **Verdict:** Interesting for Kate's content pipeline. Could generate short property tour clips. Test before deploying to client.

### Prompt Library — 152K Stars
**Source:** Bookmark #33
- GitHub: https://github.com/f/prompts.chat
- Browse by category, AI search, "Act as..." prompts
- Works with any model
- **Verdict:** Reference resource. Not actionable on its own but useful for client onboarding — helps them understand what's possible.

### Claude Certified Architect
**Source:** Bookmark #28 · @TimHaldorsson
- Anthropic offering free certification course
- "Highest paid AI job"
- **🎯 Takeaway:** Jonny should get certified. It's free and adds massive credibility to the consultancy. "Claude Certified Architect" on the business card is instant authority.

---

## 📊 UPDATED STRATEGIC ANALYSIS

### New Tools to Add to Action Items:

| Tool | Priority | Why |
|------|----------|-----|
| social-cli | 🔴 | Fix Meta Ads integration |
| GEO-SEO Claude | 🔴 | Run on all client sites |
| Gonto's EA skills | 🔴 | Reference architecture |
| Firecrawl | 🟡 | Better web extraction than web_fetch |
| Scrapling | 🟡 | Stealth scraping for reviews |
| Pexo | 🟢 | Video generation for content |
| Context Hub | 🟢 | Better coding agent docs |
| Lightpanda | 🟢 | RAM savings for scraping |
| OpenViking | 🟡 | Token savings via tiered memory |

### Consultancy Service Expansions Identified:

1. **Brand Photography Replacement** — $30K savings pitch for hotels/restaurants
2. **Local SEO Automation** — 5-step playbook for any local business
3. **Research-as-a-Service** — 3-hour deep dive replacing months of discovery
4. **Content Critic Pipeline** — self-correcting AI writing system
5. **Enterprise Security Audit** — "your agents are 91% vulnerable" sales hook
6. **Car/Insurance Negotiation Agent** — viral demo for sales

### Key People to Follow/Engage:

| Account | Why | Content Type |
|---------|-----|-------------|
| @johann_sath | Most practical OpenClaw tips | Technical how-tos |
| @chrysb | AlphaClaw + founder use cases | Tools + real results |
| @jordymaui | WeeklyClaw newsletter | Weekly roundup |
| @TheMattBerman | Marketing agent systems | Video tutorials + kits |
| @kaostyl | Battle-tested patterns | Long operational threads |
| @bloggersarvesh | Local SEO with AI | Prompt playbooks |
| @boringmarketer | Honest evolution of opinion | Shifting sentiment signal |
| @floriandarroman | OpenClaw Lab community ($4.8K MRR) | Community building model |
| @mgonto | Open-source EA skills | Reference implementations |
