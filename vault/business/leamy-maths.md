# Leamy Maths — Full Business Context

## Overview
- Website: https://leamymaths.ie
- Sells online courses (e.g. 6th Year Higher Level, Junior Cert Higher Level)
- Free trial course available (3 lessons)
- Courses priced around €49.99
- Platform: WordPress + WooCommerce
- Video hosting: Vimeo
- Todo file: `/home/jonny/.openclaw/workspace/leamymaths-todo.md`

## Google Analytics (property 286245028)
- GA4 service account credentials: `/home/jonny/.openclaw/workspace/credentials/ga4-service-account.json`
- Service account email: `claw-analytics@claw-489121.iam.gserviceaccount.com`
- ~100k+ total sessions, growing from ~500/month (2021) to 5,085 (Jan 2026)
- Peak months: Jan/Feb and Oct/Nov (Leaving Cert exam calendar)
- Top channel: Google organic (~56k sessions) — SEO is working well
- Social (Facebook + Instagram): only ~4k sessions — big untapped opportunity
- Top pages: homepage, /my-courses/, /my-account/, Junior Cert course, Leaving Cert course
- Devices: 57% desktop, 32% mobile, 11% tablet
- Geography: 83% Ireland
- Old/unused GA4 property: 405213626 (only 4 sessions ever — not properly set up)
- Key issue: `/nogo/` page getting 3,565 sessions — needs investigation
- Key issue: checkout conversion gap (9,800 course views → only 1,635 checkout visits)
- ChatGPT sending 281 sessions/year → new organic channel, worth monitoring

## Competitive Intelligence
- Biggest national threats: **Breakthrough Maths** (36k IG, 800 Trustpilot reviews, €149/month, national award winner) and **Grinds360** (23k students, Brian O'Driscoll backed)
- Limerick locals: Kilmartins (strong local brand), Premier Tuition Dooradoyle, Barnakyle Maths & Science (Patrickswell)
- Leamy gaps vs competitors: Instagram (330 vs 36k), zero Trustpilot/Google reviews, no subscription model
- Full report: `leamymaths-competitive-analysis.md`

## WooCommerce Admin
- Can log into WordPress admin via browser (leamyclaw@gmail.com)
- Can manage Forminator form submissions (form ID 11250, 720+ entries)
- Membership method: Add Member modal → JS inject user ID → set plan → Save → verify wcm-active
- Skill: `~/.openclaw/skills/woocommerce-memberships/SKILL.md`
- DO NOT waste time on: REST API, admin-ajax.php, post-new.php direct nav, Grant Access button

## Technical Notes
- Whisper (local STT) too slow on this CPU for long audio (>30 min)
- GTM containers GTM-KQRRRZRD + GTM-MZQ9J4J on site but NOT accessible under leamyclaw@gmail.com
- `/contact-us/` page is 404 — correct URL is `/contact/`
