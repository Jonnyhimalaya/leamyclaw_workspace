# Bookmarks Index — By Trigger Situation
> Use this when you're *in* one of these situations. Don't scan the catalogue — scan this.
> Updated: 2026-04-25 | Batches: Apr 2 (55 posts), Apr 14 (18 posts), Apr 25 (3 posts)

---

## 🏢 "Writing consultancy sales copy / pitch deck / landing page"

Pull these before writing a single word:

| Ref | Author | Hook to steal |
|-----|--------|--------------|
| C1 | @eng_khairallah1 | "60-70% of operational tasks automated, you focus on strategy" |
| C3 | UiPath | "Standard vs Advanced agents" framing; 4 signals test verbatim |
| C4 | Gregor (reply to C4) | **"The hard problem isn't storing knowledge. It's surfacing the right piece at the right moment."** — lift verbatim |
| C12 | @rohit4verse | **"Build the knowledge base in week one. Build the decay function in week two. Skip the second one and the first one becomes a liability."** — lift verbatim |
| C5 | @garrytan | **"Every failure becomes a permanent improvement. By month 6, your agent is irreplaceable."** — compounding-value pitch (Skillify) |
| C7 | @Sandeepg33k | **"Your agent isn't just deployed — it's continuously regression-tested in plain English. Breakage detected in 15 minutes, not when a customer complains."** |
| C8 | Karpathy/Tobi Lutke | **"Pick a KPI. The agent self-improves against it overnight. Tobi Lutke woke up to +19% on a smaller model."** |
| C9 | Google Cloud | **"Google Cloud's Agent Runtime gives you 7-day state persistence — at Google Cloud pricing. We give you the same statefulness on your server, your data, your control."** |
| C3+C9 pair | UiPath + Google | **"UiPath calls it Advanced Agents 2.0. Google Cloud calls them long-running agents. Two enterprise vendors agree on the architecture. We ship it without the cloud bill."** |
| C5+C8 pair | Skillify + Autoresearch | **"Skillify defends your wins. Autoresearch discovers new ones. Both run while you sleep."** |
| C6+C7 pair | Stitch + Passmark | **"Design rules validated automatically. Behaviour regression-tested automatically. Drift caught before customers see it."** |
| B13 | @hwchase17 | "If your agent's memory lives behind someone else's API, you don't have a product" |
| B17 | @garrytan | "Boil the ocean" — marginal cost of completeness is near zero |
| #61 | @polydao | "Architecture not chatbot" — token waste from bootstrap files |
| #43 | @TheMattBerman | Replaced $8K/mo content strategist for $30 — pricing proof point |
| #58 | @mgonto | Replaced executive assistant with OpenClaw — EA replacement proof point |
| #8 | @the_smart_ape | Saved $30K/year cutting photography budget 99.99% — hospitality hook |
| #90 | @berman66 | "Security nightmare of uncontrolled installs" — enterprise fear angle |

**Key pricing validation from prior research (action-items.md):**
- Gonto: $250-300/mo AI EA vs $1,500 human
- Matt Berman: $30/mo replaces $8K/mo strategist
- Our managed service anchor: €2-5K setup + €200-500/mo maintenance

---

## 🔍 "Qualifying / scoping a new consultancy client (discovery call)"

| Ref | Author | Use it for |
|-----|--------|-----------|
| C3 | UiPath | Run the **"4 signals test"** — hit 2+ = they need advanced agent, not chatbot |
| C1 | @eng_khairallah1 | Phase 1 "map workflows + label 🟢🟡🔴" → sell as paid Discovery (€500-1k) |
| #61 | @polydao | If client says "we just need a chatbot" — architecture reframe |
| B13 | @hwchase17 | If client is considering SaaS AI tools — memory moat argument |

**Discovery engagement pitch:** Khairallah's Week 1 exercise (map every workflow, label automate/assist/human) is a clean €500-1k first engagement. Low risk to client, sets up the build.

---

## 🏗️ "Designing a new client deployment"

| Ref | Author | Use it for |
|-----|--------|-----------|
| C3 | UiPath | Check deployment against the **4 pillars**: planning, sub-agents, skills+prompts, filesystem-memory |
| C9 | Google Cloud | Check deployment against **5 patterns**: Checkpoint-and-Resume, Delegated Approval, Memory-Layered Context, Ambient Processing, Fleet Orchestration |
| C10 | @eng_khairallah1 | Bake **"Khairallah Top-10 Defaults"** subset into Phase 2 deployment template (Plan Mode, /init, Reference File, Test-First, Pattern Enforcer, Undo Checkpoint, etc.) — first-90-days onboarding kit |
| C11 | Higgsfield | Optional Phase 2 add-on for consumer-facing clients: UGC ad pipeline. Vendor-agnostic (Higgsfield, VEO, Nano Banana, Kling). DESIGN.md is the brand-safety rail. |
| C12 | @rohit4verse | **Phase 5 "Maintain"** — every client deployment ships with a decay function, dedup pass, contradiction handling. Build in week 2 of any new engagement. "Skip it and the knowledge base becomes a liability." |
| C5 | @garrytan | Bake **Skillify** into the deployment SOP — client gets failure→skill pipeline as Phase 3 of engagement (compounding-value story) |
| C6 | @stitchbygoogle | Bake **`DESIGN.md`** into Phase 2 deployment for any client with public-facing visual output (website/social/reports). Brand-consistent agent output, WCAG accessibility built-in |
| C7 | @Sandeepg33k | **Passmark** regression suite — standard Phase 2 deliverable for any client with a public web surface (Leamy, Kilmurry, Dano MCs). Catches breakage before customers do. |
| C8 | @aiwithmayank / Karpathy | **Autoresearch** loop — Phase 4 deliverable. Identify 1 client KPI, let agent self-improve against it overnight. Examples: Leamy checkout rate, Faye pickup MAE, Kate engagement rate, Dano audit completeness. |
| C2 | @steipete | If budget is tight → README-as-dashboard tier instead of full web MC |
| C4 | @RoundtableSpace | Membase = SaaS competitor frame — our pitch is locally-hosted, client-owned, governed (vs cloud lock-in). OpenKB option for long-PDF clients (Dano IFRS 15, Faye competitor pricing) |
| B1 | @kevinnguyendn | ByteRover — if deployment is multi-agent, consider git-like memory versioning |
| B7 | @jlehman_ | lossless-claw — if client needs total recall / context persistence |
| #80 | @kaostyl | Battle-tested 24/7 patterns — apply to client's AGENTS.md |
| #40 | @jordymaui | Skills guide + language drift fix — apply to client system prompts |
| B16 | @BenjaminBadejo | Include session transcripts in QMD paths, not just memory folder |

**3-tier deployment model (from C2):**
- **Starter:** README-as-dashboard. Agent updates one live markdown doc. No hosting overhead.
- **Pro:** Web MC like Kate/Faye/Dano. Nginx + systemd + auth.
- **Enterprise:** Multi-agent + SSO + audit trail.

---

## 📣 "Planning X / social content"

| Ref | Author | Use it for |
|-----|--------|-----------|
| C2 | @steipete | Quote-tweet / build-on-top-of clawsweeper — 565k views, audience is primed |
| C6 | @stitchbygoogle | Riff: "Google open-sourced the design layer for AI agents. We've been doing the same thing for cognition for 6 months." 6.6M views — most-engaged source in our set |
| C1 | @eng_khairallah1 | Riff on his "3 starter workflows" angle with real Kilmurry/Leamy examples |
| C3 | UiPath | "UiPath says this. We deliver it." — enterprise validation post |
| #27 | @minchoi | "7 people's X strategies automated while sleeping" — post format that performs |
| #43 | @TheMattBerman | "$30/mo vs $8K/mo" — proven viral format, apply to our clients |
| B17 | @garrytan | "Boil the ocean" as a content angle — completeness is the differentiator |

**Draft post ideas already identified:**
1. "How a maths school + country hotel + fintech firm all run the same 3 workflows"
2. "UiPath says Advanced Agents need 4 things. We deliver all 4 — without UiPath."
3. Clawsweeper riff: "We're doing this for businesses, not just code repos"
4. **"AGENTS.md gives agents a brain. DESIGN.md gives them a face. We've been doing both for clients."**

---

## 💰 "Pricing / tier discussion"

| Ref | Author | Data point |
|-----|--------|-----------|
| C2 | @steipete | README tier is a real, viable product (proof: clawsweeper built in 2 days) |
| #43 | @TheMattBerman | $30/mo replaces $8K/mo strategist — floor anchor |
| #58 | @mgonto | $250-300/mo vs $1,500 human EA — mid anchor |
| C3 | UiPath | Enterprise six-figure contracts — ceiling anchor / wedge argument |
| C1 | @eng_khairallah1 | Discovery engagement = Phase 1 map exercise, €500-1k |

**Proposed tier anchors (synthesised):**
- Starter: ~€200-500/mo (README-as-dashboard, 1 agent, basic workflows)
- Pro: ~€500-1,500/mo (web MC, multi-module, dedicated support)
- Enterprise: €2,000+/mo or €2-5K setup + maintenance

---

## 🔐 "Pitching to finance / audit / regulated industries"

| Ref | Author | Use it for |
|-----|--------|-----------|
| C3 | UiPath | "Inspectable evidence trail" = pillar 2 of Advanced agents — maps to Dano |
| B13 | @hwchase17 | Memory ownership argument — regulated industries can't use SaaS AI |
| #90 | @berman66 | "Security nightmare of uncontrolled installs" — fear hook for compliance buyers |
| #73 | @johann_sath | SSH brute force / disk monitoring — shows operational security depth |

**Dano's Ledger = flagship case study here.** IFRS 15 compliance, EY audit Jan 2027 — that's exactly UiPath's "inspectable evidence trail needed" signal.

---

## 🧠 "Improving our own agent setup / architecture"

| Ref | Author | What to do |
|-----|--------|-----------|
| C12 | @rohit4verse | **Decay function audit** — our MEMORY.md has stacked dreaming-promotion sections from Apr 13 onwards, many with recalls=0. Stale candidates outvote fresh entries. Audit for stale/duplicate/contradicting entries. Add Memory Protocol F: decay & contradiction discipline. |
| C3 | UiPath | Audit all four pillars across our setup |
| C9 | Google Cloud | Audit all 5 patterns across our 4 active deployments — Checkpoint-and-Resume, Delegated Approval, Memory-Layered Context, Ambient Processing, Fleet Orchestration. **Delegated Approval (paused-resumable) is the known gap.** Rename existing patterns using Google's vocabulary in client-facing docs. |
| C10 | @eng_khairallah1 | **35 Claude Code techniques** checklist — audit our workspace AGENTS.md against the list. Known immediate-fix: Technique 16 (Undo Checkpoint, git commit before any major change) is missing as a hard rule. Technique 21 (Pattern Enforcer with file references) is inconsistent. |
| C5 | @garrytan | **Skillify** — the 10-step pipeline to turn any failure into a permanent, tested skill. Operational maturity model. Apply to next failure we hit. |
| C7 | @Sandeepg33k | **Passmark** — natural-language regression testing on Playwright. Tool of choice for Skillify steps 3, 4, 9 when surface is web-based. |
| B2 | @garrytan | "Durable agent" — already implemented in AGENTS.md (Garry Tan rule). C5 = the full pipeline behind it. |
| B6 | @garrytan | GBrain — pgvector/Postgres semantic search over markdown; eval vs QMD |
| B7 | @jlehman_ | lossless-claw — total recall across /new and /reset |
| B11 | @MatthewBerman | Skill Drift Detector — run periodically on AGENTS.md/SOUL.md/skills |
| B15 | @RoundtableSpace | Permanent memory for Claude Code — 95% less token consumption |
| #1A | @OnlyTerp | Bootstrap trim — total bootstrap should be 8-15KB; we're over |
| #80 | @kaostyl | Battle-tested 24/7 patterns — memory architecture > prompts |
| #35 | @PrajwalTomar_ | "Copy-paste into agent and tell it to implement everything" — self-deploy pattern |

---

## 🔒 "Security audit / hardening"

| Ref | Author | What to do |
|-----|--------|-----------|
| #73 | @johann_sath | SSH brute force detection, disk monitoring, 3am attack prevention |
| #72 | @johann_sath | Kybernesis plugin — persistent memory, stop re-reading files |
| #1B | SlowMist | 3-tier defense matrix with nightly audits (from MASTER-ACTION-PLAN Phase 1) |
| #90 | @berman66 | "Security nightmare of uncontrolled installs" — prompt injection risk |

---

## 🛠️ "Building / improving Kate or Faye's Mission Control"

| Ref | Author | What to do |
|-----|--------|-----------|
| C3 | UiPath | Sub-agent delegation — if missing, that's Phase 2 upsell |
| C6 | @stitchbygoogle | Drop `DESIGN.md` into Kate's workspace — content engine output becomes brand-consistent automatically. Same for Faye's revenue dashboards. |
| C11 | Higgsfield | UGC ad pipeline for Kate (hotel UGC) and Leamy (parent-testimonial style ads). DESIGN.md from C6 = mandatory brand-safety rail. |
| #55 | @RoundtableSpace | Sub-agents analyse 50 competitor ads + generate brief in 5 min — replicate for Kate |
| #43 | @TheMattBerman | Content strategist system — apply to Kate's content engine |
| #59 | @TheMattBerman | Meta Ads with social-cli — fix for Kate's broken Meta integration |
| #13 | @maxxmalist | Adjacent ad workflow — Claude + Nano Banana + VEO/Kling. Treat as alternative to Higgsfield. |
| B18 | @Voxyz_ai | Horizontal memory (cross-agent) — shared Gmail/Calendar layer for Kate + Faye |

---

## 📚 "Still unresearched — high priority queue"

These are in the catalogue (⬜) but haven't been deep-dived yet. Top picks by likely ROI:

| Ref | Author | Why it's a priority |
|-----|--------|-------------------|
| #80 | @kaostyl | 3 weeks running 24/7 — most battle-tested patterns in the whole set |
| #61 | @polydao | Architecture framing — directly usable in sales copy |
| #59 | @TheMattBerman | Meta Ads for $0/mo — fixes a live broken integration |
| #55 | @RoundtableSpace | 50-competitor-ad analysis — directly deployable for Kate |
| #1C | @cathrynlavery | openclaw-ops — self-healing layer (from MASTER-ACTION-PLAN) |
| #36 | @sukh_saroy | GEO-SEO Claude — AI search optimisation, unrun on any of our sites |
| #92 | @bloggersarvesh | Google Business Profile + Claude = 78 extra leads in 30 days — Kilmurry |
| B6 | @garrytan | GBrain — semantic search over markdown, eval vs what we have |
| B11 | @MatthewBerman | Skill Drift Detector — should run this on our setup periodically |
