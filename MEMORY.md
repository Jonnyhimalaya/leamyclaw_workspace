# MEMORY.md — Long-Term Memory

## About Jonny
- Name: Stephen (goes by Jonny; Himalaya on Telegram, @jonnyhimalaya)
- Professional name on Leamy Maths: **Stephen** (correct spelling, NOT Stephan)
- Based in Limerick, Ireland
- Runs an online maths education business: **Leamy Maths** (leamymaths.ie)
- Teaches Leaving Cert and Junior Cert maths online
- Has a YouTube-style teaching approach: face-to-camera, digital whiteboard, home/studio setup

## Leamy Maths — Business Context
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

## Marketing — Active
- **Google Ads**: Full access via leamyclaw@gmail.com (AW-10776906058)
  - 3 active campaigns: Local_B_Limerick (€2.50/day), Revision_Parents (€20/day), Revision_Students (€10/day)
  - Conversion tracking working via thank-you page redirect
- **Meta Business Suite**: Partial access via leamyclaw@gmail.com (business_id: 253648777546692)
  - Facebook: Leamy Maths (113 followers) | Instagram: @leamy_maths (554 followers)
  - Meta Pixel: 6151104201627053
  - ⚠️ Cannot create posts yet — permissions issue, needs Full access or individual Content toggle
- **Instagram Campaign**: Easter revision courses, €50/day for 4 days, files in workspace/instagram-campaign/
- Marketing masterplan still to cover: SEO, email marketing

## Sub-Agent Capabilities
- Can spawn sub-agents for content strategy (gpt-5.3-codex), image generation (Sonnet + Nano Banana Pro)
- Nano Banana Pro (Gemini image gen) installed and configured with paid API key
- Image gen lesson: NO text in AI images, composite real photos + add text overlays separately
- Jonny's headshots in workspace/instagram-campaign/images/stephan-photos/

## Revision Courses (Easter 2026)
- Start date: Sunday March 22, 2026
- Target: Leaving Cert students (17-18yo) + parents, within 30km of Limerick
- Landing pages:
  - Parents (ORIGINAL, less optimised): /revision-for-leaving-cert-2026/
  - Parents (NEW, optimised Mar 19): /revision-for-leaving-cert-2026-parents-b/
  - Parents (older generic paid traffic): /revision-courses-paid-traffic/
  - Students: /expert-revision-course/
- Google Ads Revision_Parents_Limerick → changed to -parents-b/ on Mar 20 (was pending review)
- Meta/Instagram ads → ⚠️ STILL pointing to old /revision-for-leaving-cert-2026/ as of Mar 24 — NEEDS FIX
- Phone: 085 846 6670 (NOT clickable tel: link yet — todo)
- Form: Forminator ID 11250 → redirects to /thank-you-for-contacting-us/ → fires Google Ads conversion

## WooCommerce Admin Access
- Can log into WordPress admin via browser (leamyclaw@gmail.com)
- Added Logs and Exponential Functions (#5686) membership to 22 users on Mar 22-24
- Can manage Forminator form submissions (form ID 11250, 720+ entries)

## Preferences & Style
- Jonny prefers observations always added to leamymaths-todo.md
- Direct, no-fluff communication style
- Wants me to act as his marketing guru
