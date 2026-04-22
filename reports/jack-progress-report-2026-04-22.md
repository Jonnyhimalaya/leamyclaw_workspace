# Kilmurry — Progress Report for Jack

**Date:** 22 April 2026
**From:** Stephen (via OpenClaw)
**Covering:** Today's work across Kate's MC, Faye's new agent + MC, your weekly rate cron, and GitHub versioning

---

## Headline

Three large things shipped today at Kilmurry:

1. **Kate's Mission Control — fully rebuilt from scratch** to match her 6-module spec. Replaces the old cluttered MC. Live now.
2. **Faye has her own OpenClaw agent + Mission Control** — standalone sandboxed instance, mirrors Kate's setup. Her MC landing page is literally her weekly revenue report brought to life.
3. **Every agent at Kilmurry (you, Kate, Faye) now has its own private GitHub repo** for both workspace and MC. Proper versioning end-to-end.

All three are live, tested, accessible, and documented.

---

## 1. Kate's Mission Control — Rebuilt

**URL:** http://172.239.98.61:3337
**Login:** `kate` / `ExcitedKate2026!`
**Repo:** github.com/Jonnyhimalaya/kilmurry-kate-mission-control

### What changed
Kate sent through a 6-module spec (Command centre, Content engine, Reputation & reviews, SEO & visibility, Revenue intelligence, AI task log). I built it fresh rather than patching the old dashboard — the new one is cleaner, faster, and actually matches how she thinks about her week.

### What's wired to live data
- **GA4 analytics** → real sessions, users, page views, conversion funnel for kilmurrylodge.com
- **Marketing snapshot + operations snapshot** pulling from the existing gateway endpoints

### What's still DEMO/MANUAL
- Meta / Facebook insights (token issue — different FB account owns the page)
- Review platform ingestion (TripAdvisor, Google Reviews, Booking reviews)
- Email platform analytics (Kate's email tool TBC)

### Nothing lost from the old MC
All useful plumbing (gateway.ts, useApi.ts, GA4 route, marketing APIs) was ported across. Old MC at port 3334 is still running in parallel as a safety net until Kate is confident with the new one — we can turn it off whenever you want.

---

## 2. Faye's New Agent — The Big One Today

### Why
Faye currently spends **4–8 hours a day on rate inquiry emails**. The agent + MC exists to shrink that to under 2, codify her 47+ unwritten rate exception rules, and give her one screen for every decision she makes.

### What we built

**A standalone sandboxed OpenClaw agent for Faye**, independent of yours and Kate's:

| | |
|---|---|
| **User** | `fayeuser` on the Kilmurry server (no sudo, in `clawuser` group for shared-folder access) |
| **Gateway** | systemd `openclaw-faye` on port 18795 |
| **Model** | Claude Opus 4.7 (fallback to Sonnet / Gemini) |
| **OpenClaw version** | 2026.4.21 (latest) |
| **Claude Code** | Installed v2.1.117 — same cost-saving ACP pattern you use. When Faye asks for builds, her agent will route them through Claude Code on the Max subscription, not burn Opus API tokens. |
| **Shared folder** | `/home/clawuser/shared` — Faye can read your Hot Dates JSON and your weekly rate-intel output; you can read hers. |
| **Telegram bot** | Deferred — we'll pair it when Faye is ready for it. She'll get her own bot, won't interfere with yours. |

She's not on your Telegram, not in your sessions, can't see your revenue data or your agent's transcripts. Same boundary we set up for Kate.

### Faye's Mission Control
**URL:** http://172.239.98.61:3339
**Login:** `faye` / `0KiehZuBAbXgJd8U`
**Repo:** github.com/Jonnyhimalaya/kilmurry-faye-mission-control

Faye sent a detailed HTML mockup of the revenue intelligence report she produces manually now. So I built her MC around it: **the landing page IS her report**, with every section clickable through to a deeper live page.

11 sections on the landing (matching her exact layout — DM Serif Display + DM Sans, paper/white aesthetic):

1. **Executive Summary** (Occ / ADR / RevPAR / Pickup)
2. **Forward Booking Position** (4/8/12 week with pace vs forecast)
3. **Booking Velocity & Pickup** (last 7 days bookings, by arrival month)
4. **Segment Performance** (Bigger Stage, Direct, OTA, LNR, TAMS, Corporate, Comp)
5. **Distribution Channel & Source** (all 9 sources with ADR comparison)
6. **Booking.com YoY detail**
7. **Avvio Booking Engine 4-day conversion**
8. **Cancellations & Revenue Leakage** (by reason code)
9. **No-Show Report**
10. **Expedia Snapshot**
11. **Strategic Recommendations** (High / Medium / Watch priority list)

Plus a persistent sidebar with forward-looking tools she doesn't have in her current workflow:
- 📈 **Competitor Pricing graph** (live — see below)
- 🗓️ **Unified Calendar** (Hot Dates + Kate's content + availability gaps)
- 📅 **Month at a Glance** rate grid with event overlay
- 🔔 **Real-time Alerts** for cancellations and big bookings
- 💡 **Upsell Prompts**

**Export PDF** button top-right so she can still produce her Friday physical report if she wants — but it'll auto-generate from live data, no more 4 hours of copy-paste.

### What's LIVE right now on Faye's MC
- **Hot Dates Calendar** — 185 real events from the shared JSON
- **Competitor Pricing graph** — real rates from your weekly rate-intel cron (see below)

### What's still DEMO on Faye's MC
Everything that needs data from Right Revenue, RezLynx, Avvio, or a confirmed package list. We labelled every panel `LIVE / MANUAL / DEMO` so Faye will always know what's real.

### What Faye needs to give us Wednesday to unlock Phase 2
1. Confirm comp set list (we're using Castletroy / Strand / South Court / Radisson / Savoy as placeholder)
2. Avvio delivery mechanism — API, email, or PDF download?
3. RezLynx access route — direct to Faye or through you?
4. Current live package names (replace demo)
5. Alert preferences — Telegram / email / both?

---

## 3. Your Weekly Rate Intelligence Cron — Fixed + Plugged Into Faye

Your `weekly-rate-intelligence` cron had been failing since the Anthropic billing issue. I confirmed the fix from April 20 (moved to `openai-codex/gpt-5.4`), then manually triggered it:

- **Ran clean** for ~5 minutes
- Fresh JSON saved for April 23 – May 6 scraping Kilmurry, Castletroy Park, Strand, South Court
- **Kilmurry sold out 5 of 14 nights**; Castletroy sold out on most of those same nights
- Strand priced at €325 Saturday — highest in comp set

**And I patched the cron so every future run auto-copies the output to `/home/clawuser/shared/`** — which means Faye's competitor pricing chart stays up-to-date every Monday without anyone lifting a finger.

Next scheduled run: Monday 27 April 08:00.

---

## 4. GitHub Versioning — Every Kilmurry Agent Now Properly Tracked

Today we went from "most agents don't have git" to "every agent has two repos: workspace + MC."

| Agent | Workspace repo | MC repo |
|---|---|---|
| Jack (you) | `Kilmurry` | `kilmurry-mission-control` |
| Kate | `kilmurry-kate` | `kilmurry-kate-mission-control` *(new today)* |
| **Faye** | **`kilmurry-faye-workspace`** *(new today)* | **`kilmurry-faye-mission-control`** *(new today)* |

All private. Jonny and I are the owners.

**Token issue resolved:** the Kilmurry server's GitHub token was scoped to only 5 repos, which is why Kate couldn't push for 3+ weeks. Jonny widened the token this afternoon to include Kate's and Faye's new repos. **Kate and Faye can now both push their own commits directly** — their agents are fully autonomous on versioning.

---

## What's running on your Kilmurry server right now

```
Port  Service                   Owner
────  ────────────────────────  ─────────
3333  Jack MC                   you
3334  Old Kilmurry MC           (legacy, keep for now)
3336  Kate MC (new)             Kate
3337  Kate MC nginx             Kate (public URL)
3338  Faye MC (new)             Faye
3339  Faye MC nginx             Faye (public URL)
18789 Jack gateway              you
18792 Kate gateway              Kate
18795 Faye gateway              Faye
```

Disk: 37 GB free (53% used). RAM: 4.9 GB available (2.9 GB used). Swap: 21 MB used (healthy).
The server is carrying three agents + three MCs comfortably — we'll keep watching as Faye comes online.

---

## Open items for you

1. **Faye discovery meeting** (whenever suits Faye) — 30 min to walk her through the MC and capture the 5 answers above.
2. **Right Revenue credentials** — when Faye's ready, we'll need login so her agent can automate the rate inquiry drafts (her biggest time sink).
3. **Claude Code one-time auth for Faye** — same as you did, so her agent's builds route through the Max subscription not API billing. Can be done in 2 minutes any time.
4. **Old MC at port 3334** — decision point. Keep running, or decommission now that Kate has her new one?

---

## One thing worth noting

Faye's mockup was better than most client specs I've seen. She knows exactly what decisions she makes every day and what data she needs to make them. That meant I could build her MC in ~30 minutes from a spec she clearly had in her head for months. When you speak to her, she'll probably have one or two tweaks — but the bones are right.

The bigger insight: her current 4-hour Friday report was a manual version of what this MC renders automatically. When Right Revenue and RezLynx are wired in, that 4 hours a week disappears. That's 200 hours a year back to her for actual revenue decisions.

---

*Prepared for Jack Hoare · Revenue & GM · Kilmurry Lodge Hotel*
*Document available at `reports/jack-progress-report-2026-04-22.md`*
