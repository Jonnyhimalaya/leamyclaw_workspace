# Client Deployment Status (as of 2026-04-05)

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

## Kilmurry Lodge / Kate Taylor — Deployed 2026-04-04
- **Server:** 172.239.98.61, `kateuser` OS user
- **Gateway:** Port 18792, systemd: openclaw-kate
- **Auth:** Shared Anthropic key, Sonnet primary, Gemini fallback
- **Security:** Exec allowlist, SOUL.md + AGENTS.md immutable (chattr +i), no sudo
- **Mission Control:** Port 3334 (kilmurry-kate-mc), 10 pages, Kilmurry brand theme
- **Data Pipelines:** Events scraper (34 events/6 sources), GA4 script (blocked on permissions), reviews (20 seeded), competitors (14-date rate comparison)
- **GitHub:** Jonnyhimalaya/kilmurry-kate
- **Score:** 93% — remaining 7% needs Kate (Wednesday meeting)
- **Open:** TUI test, Telegram bot (Wednesday), GA4 service account permissions, live review scraping

## Resource Impact
- Post-deployment RAM: 1.3GB used / 2.6GB available (tight but OK)
- Disk jumped to 56% (from 41% day prior) — Nexus npm/node caches account for ~9.3GB
