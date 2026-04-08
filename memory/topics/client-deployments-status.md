# Client Deployment Status (as of 2026-04-07)

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
- **Tailscale IP:** 100.111.174.13 (Jack's tailnet — Kate needs to join via Jack invite)
- **Gateway:** Port 18792, systemd: openclaw-kate
- **Auth:** Shared Anthropic key, Sonnet primary, Gemini fallback
- **Security:** Exec allowlist, SOUL.md + AGENTS.md immutable (chattr +i), no sudo
  - ⚠️ exec-approvals.json was also chattr+i'd (bug) — removed 2026-04-07. Only SOUL.md + AGENTS.md should be immutable.
- **Mission Control:** Port 3334 (kilmurry-kate-mc), 10 pages, Kilmurry brand theme
- **Telegram:** @Katetaylor123_bot | Kate's TG ID: 8778805348 | pairing code: QBCY5BVQ (used/approved)
- **Whisper:** Installed, exec-approvals.json updated (whisper + ffmpeg allowlisted)
- **Data Pipelines:** Events scraper (34 events/6 sources), GA4 script (blocked on permissions), reviews (20 seeded), competitors (14-date rate comparison)
- **GitHub:** Jonnyhimalaya/kilmurry-kate — ⚠️ push unresolved, neither kateuser nor clawuser has GitHub auth on server
- **Score:** 93% — remaining 7% needs Kate (Wednesday meeting)
- **Open:** GitHub auth (HTTPS fine-grained token), GA4 service account permissions, Meta token, email platform, live review scraping
- **Wednesday meeting needs from Kate:** GA4 property access, Meta/Facebook API token, email platform + API key, Google Ads account ID

## Resource Impact
- Post-deployment RAM: 1.3GB used / 2.6GB available (tight but OK)
- Disk jumped to 56% (from 41% day prior) — Nexus npm/node caches account for ~9.3GB
