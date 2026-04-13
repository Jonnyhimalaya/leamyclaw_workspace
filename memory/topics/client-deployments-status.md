# Client Deployment Status (as of 2026-04-11)

## Nexus (BTC Company) — Deployed 2026-04-04
- **Server:** Same VPS (172.239.114.188), `nexus` OS user
- **Gateway:** Port 18790, systemd managed, auto-restart
- **Telegram:** @OnNexus_bot connected + paired
- **Auth:** Failover configured (profile rotation + cooldowns)
- **Memory:** QMD (Gemini embeddings)
- **Mission Control:** Port 3334, PM2 managed (8-page Next.js app)
- **Security:** 100/100 compliance
- **Score:** 95% (advisor cron deferred)
- **Open:** Git remote needs private repo. RAM impact ~740MB.

## Kilmurry Lodge — Current State

### Jack Hoare / Main Kilmurry Instance
- **Server:** 172.239.98.61, `clawuser` OS user
- **Tailscale IP:** 100.111.174.13
- **Gateway:** Port 18789
- **Primary app:** Mission Control at port 3333
- **Repo/app path:** `/home/clawuser/mission-control`
- **Workspace path:** `/home/clawuser/.openclaw/workspace`
- **Model in active use for Jack's bot:** Claude Opus 4.6 during blueprint phase, with stated intention to route cheaper work later
- **Current architectural reality:** Mission Control is now a hybrid system
  - Next.js shell/app remains the core
  - multiple department and intelligence modules are now shipped as static HTML/JS files alongside it
- **Mission Control scope has expanded** from a standard dashboard into a broader hotel operating and intelligence layer

#### Live / Implemented for Jack
- **Marketing Department prototype** live at `/marketing-dept/index.html`
  - built from `public/marketing-dept/index.html` + `public/marketing-dept/marketing.js`
  - sidebar updated so Marketing Hub points to the static module
  - this is a vision prototype with demo data, not yet a production workflow engine
- **Department dashboards added** as self-contained HTML modules:
  - Revenue
  - Sales
  - Facilities
  - Guest Relations
  - F&B
- **Intelligence tools added:**
  - Morning Brief
  - Forecasting dashboard / Alkimii bridge
  - Hot Dates review queue
  - Prediction Challenge
  - World Scenarios
- **Shared operational data introduced:** hot dates JSON with 185 real events feeding department modules
- **Real business analysis work completed:** CASK intelligence, Alkimii forecasting analysis, Bigger Stage/Troy Studios analysis, Dolans/Limerick music scene research, macro/fuel risk work

#### Important interpretation
- **This is the newest source of truth** for Jack's setup and supersedes older simpler descriptions of Mission Control
- Much of the new estate is still **prototype/intelligence-layer architecture**, not fully live API-driven operations
- The biggest near-term risk is sprawl: lots of powerful static modules, not yet enough productionised workflow behind them

#### Operational open items for Jack
- Mission Control repo discipline needs attention, especially around remote/branching workflow
- Need to decide what gets productionised first rather than continuing to add prototype surfaces
- Best candidates for first real operationalisation:
  - Morning Brief pipeline
  - Hot Dates ingestion + scoring
  - Forecasting / Alkimii bridge
  - Marketing review queue
- Kilmurry is now both:
  - a live client deployment
  - a high-value R&D pattern source for consultancy reuse

### Kate Taylor / Marketing Instance
- **Server:** same Kilmurry server, `kateuser` OS user
- **Gateway:** Port 18792, systemd: openclaw-kate
- **Mission Control:** Port 3334 (kilmurry-kate-mc)
- **Telegram:** @Katetaylor123_bot | Kate's TG ID: 8778805348
- **Auth:** Shared Anthropic key, Sonnet primary, Gemini fallback
- **Security:** exec allowlist, no sudo; immutable-lock lesson already applied so only truly static files should be locked
- **Whisper:** Installed, exec approvals updated for whisper + ffmpeg
- **Data pipelines:** events scraper, review seeding, competitor comparisons; GA4 and some marketing integrations still partially blocked by access
- **Current strategic wrinkle:** Kate's separate MC and Jack's newer Marketing Department prototype now overlap conceptually, so a boundary or merger path is needed
- **Open:** GA4 access, Meta token, email platform/API, Google Ads ID, and clearer architecture decision about Kate MC vs Jack marketing module

## Reusable Consultancy Learnings Emerging from Kilmurry
- Department-module architecture can work well as a fast prototyping pattern
- Intelligence layer over existing business systems is often better than trying to replace source systems immediately
- Human-in-the-loop review queues are commercially useful and easier to trust
- "Flag as Wrong" correction-to-memory/training loop is a strong reusable pattern
- Morning brief as a daily intelligence product is high-value and likely reusable for future clients
- Kilmurry should be treated as a pattern lab, but reusable ideas should be merged into existing consultancy docs/playbooks rather than spawning redundant new docs

## Resource Impact
- Kilmurry runs multiple instances and dashboard surfaces on the same server, so RAM and architectural sprawl need ongoing monitoring
- Nexus npm/node caches previously accounted for significant disk growth on shared infrastructure; versioning and cache hygiene remain important
