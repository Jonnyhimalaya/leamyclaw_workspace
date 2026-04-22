# Faye MC — Deployment Checklist

Follows Kate MC rebuild pattern (2026-04-22).

## Phase 0 — Spec signoff
- [ ] Jonny approves product spec v1
- [ ] Open questions for Faye captured into first-session agenda

## Phase 1 — Infra
- [ ] Create private repo `Jonnyhimalaya/kilmurry-faye-mission-control`
- [ ] Scaffold Next.js 14 + Tailwind + TS app locally
- [ ] All 9 module components stubbed (label mode: `MANUAL` or `DEMO`)
- [ ] Anchor nav from top module cards to sections (Kate pattern)
- [ ] Commit + push via Jonny PAT (Faye server token can't read new repo yet — same wrinkle as Kate's build)
- [ ] Deploy to Kilmurry via tarball
- [ ] systemd `faye-mc` on port 3338
- [ ] nginx basic-auth proxy on port 3339
- [ ] Login `faye` / generated password → stored in main workspace MEMORY.md + Telegram to Jonny
- [ ] Copy GA4 service-account credential if needed for analytics tie-in
- [ ] URL http://172.239.98.61:3339 smoke-tested

## Phase 2 — Shared data plumbing
- [ ] `/api/hot-dates` route reads `/home/clawuser/shared/hot-dates-2026.json`
- [ ] `/api/content-calendar` proxy to Kate MC (requires Kate MC endpoint built first)
- [ ] `/api/status` gateway health
- [ ] Migrate gateway.ts + useApi.ts from Kate MC (proven pattern)

## Phase 3 — Right Revenue scraper (big one, Claude Code via ACP)
- [ ] Browser automation module: login + session management
- [ ] Data extractors: rates, occupancy, pickup, comp set
- [ ] Cached JSON output refreshed every 30 min
- [ ] Toggle label `MANUAL` → `LIVE` once stable

## Phase 4 — Avvio reports
- [ ] Confirm mechanism with Faye (API / email / PDF)
- [ ] Build ingestion
- [ ] Daily + weekly report views

## Phase 5 — Alerts
- [ ] Telegram bot paired for Faye
- [ ] Cancellation / large booking triggers
- [ ] MC banner for active alerts

## Phase 6 — Gap analysis & handover
- [ ] All panels labelled correctly (LIVE/MANUAL/DEMO audit)
- [ ] README with ops notes
- [ ] 30-min session with Faye to walk through
- [ ] Capture her feedback as Phase 2 backlog in her agent's workspace
