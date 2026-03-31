# Leamy Maths – Marketing & Website TODO

_Started: 2026-03-03_
_Based on initial site audit + checkout flow testing_

---

## ✅ Completed

- [x] **Negative keywords cleanup (2026-03-20)** — Created shared negative keyword list "Revision Campaigns - Negatives" with 45 phrase/broad match negatives (studyclix, mathletics, log tables, maths solver, exam papers, biology, chemistry, cork, dublin, textbook names, etc.). Applied to all 3 active campaigns: Local_B_Limerick, Revision_Parents_Limerick, Revision_Students_Limerick. Kept competitor "Julie Kilmartin" searches intentionally — Jonny wants to steal her traffic.
- [x] **Landing page change (2026-03-20)** — Revision_Parents_Limerick ad Final URL changed from `/revision-for-leaving-cert-2026/` → first to `/revision-courses-paid-traffic/` (wrong page), then corrected to `/revision-for-leaving-cert-2026-parents-b/` (the actual optimised page built Mar 19). Ad went into "Pending" review.
- [ ] **⚠️ URGENT: Meta/Instagram ads still pointing to OLD page** — As of Mar 24, Paid Social (140 sessions) all landing on `/revision-for-leaving-cert-2026/` instead of the optimised `-parents-b/` page. Need to update Meta ad URL immediately.
- [ ] **Verify Google Ads Revision_Parents review status** — Ad was "Pending" since Mar 20. Paid Search parents traffic going to `-parents-b/` (52 sessions) suggesting it may have cleared, but needs verification.

---

## 🌐 Website – Quick Fixes

- [ ] **Remove 2020 dates from revision course product names** — "Financial Maths May 17th 2020" etc. look like abandoned COVID content. Either remove the dates entirely or update to current year.
- [ ] **Update "Re-opening for September 2023"** — This reference on the classroom grinds page makes the site feel inactive/outdated.
- [ ] **Fix county display in billing address** — Post-purchase billing address shows "LK" instead of "Limerick". Cosmetic but unprofessional.

---

## 🛒 Checkout & Cart Bugs

- [ ] **Fix duplicate cart item bug** — Adding the free product to cart results in quantity × 2 at checkout. Needs investigation by developer (WooCommerce cart session issue likely).

---

## 🔁 Conversion & Funnel

- [ ] **Simplify homepage** — Create two clear paths for first-time visitors: "In-Person Grinds (Limerick)" and "Online Courses". Remove clutter.
- [ ] **Single clear CTA** — Currently "Book Now" and online course CTAs compete. Pick one primary action per page.
- [ ] **Add lead magnet** — Offer a free sample lesson or PDF cheat sheet to capture emails from visitors not ready to buy yet. Build an email nurture sequence from there.
- [ ] **Add urgency/scarcity for in-person grinds** — "Limited places available", enrolment deadline countdown etc.
- [ ] **Display classroom grind pricing on homepage** — Currently missing; parents shouldn't have to hunt for it.
- [ ] **Add FAQ section** — Address common parent concerns: class size, what to bring, refund policy, online vs in-person differences.
- [ ] **Make Packages & Bundles more visible** — Currently buried in a submenu; should be prominent.

---

## 📧 Post-Purchase Experience

- [ ] **Improve order confirmation message** — Replace generic "Thanks for purchasing a membership!" with a warm, personalised welcome: "Welcome to Leamy Maths! Here's what to do next…" with clear next steps.
- [ ] **Add upsell on order confirmation page** — Prime real estate. Add a "Want the full course? Upgrade for €49.99" prompt to convert free trial users immediately.
- [ ] **Verify bonus lesson email sequence is live** — Site says bonus lessons are delivered via email upon completion of each core lesson. Confirm this automation is actually firing correctly.

---

---

## 📊 Google Analytics — Findings & Actions

### Key Stats (All Time, property 286245028)
- ~100k+ total sessions across 55 months
- Growth from ~500/month (2021) → 5,085 (Jan 2026) — nearly 10x
- Peak months: Jan/Feb and Oct/Nov (LC exam calendar)
- Google organic: ~56k sessions (dominant channel)
- Direct: ~25k | Bing: 4.3k | Facebook+Instagram: ~4k combined
- Devices: 57% desktop, 32% mobile, 11% tablet
- Ireland: 83% of traffic

### Actions
- [ ] **FIX `/nogo/` page — FOUND IT!** — It's a paywall redirect page that says "Please purchase the above course to access this content." 275 sessions/month land here (17.5% bounce). This is where non-paying users get sent when they try to access paid lessons. **Problem:** The page is a dead end with no purchase link, no course name, no CTA button. It just says "buy the course" without linking TO the course. FIX: Add a clear CTA button linking to the relevant course page, or better yet, redirect to the specific course they were trying to access with a "Get access" prompt.
- [ ] **Fix checkout conversion gap** — Course pages get 9,800+ sessions but checkout only gets 1,635. Only ~17% of course viewers reach checkout. Add CTAs, urgency, and friction reduction.
- [ ] **Fix old GA4 property (405213626)** — Only 4 sessions ever recorded. Either remove tracking code or delete the property to avoid confusion.
- [ ] **Set up conversion goals in GA4** — Track: checkout started, purchase completed, free trial signup, lesson completed.
- [ ] **Monitor seasonal peaks** — Jan/Feb and Oct/Nov are high season. Plan campaigns and content around these windows.
- [ ] **Investigate China traffic (4,150 sessions)** — Likely bot/spam. Set up a filter to exclude it from reports.
- [ ] **Bing SEO** — 4.3k sessions from Bing with zero effort. Worth optimising for.

---

## 🎓 Course / Member Experience

- [ ] **Improve course introduction video** — Currently 2:51 long. Should be a proper welcome that hooks students emotionally and sets expectations. Think of it as a mini sales video for the full course.
- [ ] **Add upsell prompt inside free trial** — After Lesson 3 (last free lesson), add a clear "Enjoying this? Get the full course for €49.99" prompt. Don't let students reach the end of the trial without being nudged to upgrade.
- [ ] **Rename "Sept/Oct Term LCH" module** — Internal teacher language. Rename to something student-friendly like "6th Year Higher Level — Algebra Module."
- [ ] **Add Q&A / comments per lesson** — No way for students to ask questions inside the platform. Even a basic comments section would add value and differentiate from YouTube.
- [ ] **Move or duplicate "Complete Lesson" button to top** — Currently only at the bottom after two videos. Students may not scroll down, breaking the bonus lesson email drip sequence.

---

---

## 🎯 Google Ads — Findings & Actions

### Current State
- 25 campaigns total, all Search type
- **23/25 paused** — effectively zero ad spend right now
- Only active: `Local_B_Limerick` (€10/day, Maximize conversions) — but showing 0 impressions
- Total spend last 7 days: **€0.00**
- Campaigns cover all year groups (3rd, 5th, 6th Year, JC, LC, TY) in Higher (_E_) and Ordinary (_P_) levels — well structured
- Special campaigns: Brand_IE, Easter_B_Limerick, Location-Based_Campaign_P_IE (€20/day)

### Actions
- [ ] **Investigate why Local_B_Limerick is enabled but getting 0 impressions** — check keyword match types, Quality Scores, and bid levels
- [ ] **Decide which campaigns to reactivate** — at minimum: `Leaving_Cert_E_IE`, `Leaving_Cert_P_IE`, `Junior_Cert_E_IE`, `Brand_IE` for ongoing brand protection
- [ ] **Fix conversion tracking** — several campaigns use "Maximize conversions" bid strategy but if WooCommerce purchases aren't tracked as conversions, Google has no signal. Verify GA4 ↔ Google Ads conversion linking.
- [ ] **Increase budgets** — current budgets (€5–€20/day per campaign) are very low. Consolidate into fewer, better-funded campaigns.
- [ ] **Consider Performance Max campaigns** — all current campaigns are Search only. pMax can capture YouTube, Display, and Shopping inventory too.
- [ ] **Seasonal campaign calendar** — turn on specific campaigns before peak seasons: back-to-school (Aug/Sep), Christmas revision (Dec), Easter courses (Mar/Apr), pre-Leaving Cert (Apr/May)
- [ ] **Add negative keywords** — review search terms report once campaigns are live to filter irrelevant traffic

---

---

## 🚨 URGENT: Revision Course Launch Funnel (March 22nd start)

Full funnel spec: `/home/jonny/.openclaw/workspace/leamymaths-revision-funnel.md`

### Landing Pages
- `/revision-courses-paid-traffic/` — Parent lead capture (paid social)
- `/revision-for-leaving-cert-2026/` — Parent detailed (search)
- `/expert-revision-course/` — Student detailed (search + organic)

### Immediate Actions
- [ ] Remove "Message" field from paid traffic form — reduces friction
- [ ] Add CTA buttons above the fold on ALL 3 pages
- [ ] Add urgency ("Starts March 22nd — only X days away") to all pages
- [ ] Add phone number prominently on parent pages
- [ ] Film 30-sec video for Instagram organic + ads
- [ ] Post "5 DAYS TO GO" organic Instagram post
- [ ] Upgrade leamyclaw@gmail.com to Standard access on Google Ads (currently read-only, can't create campaigns)
- [ ] Create Google Ads campaigns per funnel spec
- [ ] Create Meta ad campaigns per funnel spec

---

## 📱 Social Media & Instagram

- [ ] Set up Instagram content strategy
- [ ] Plan content calendar (testimonials, exam tips, behind-the-scenes, student results)
- [ ] Link Instagram bio to a landing page (not homepage — a focused lead capture page)

---

## 📊 Analytics & Ads

- [ ] Get access to Google Analytics — review traffic sources, bounce rate, top pages
- [ ] Get access to Google Ads — review any existing campaigns
- [ ] Set up conversion tracking (free trial signups, paid course purchases)

---

## 🎓 Revision Course — Student Tracking (Easter 2026)

### €449 Bundle — Paid but NO sessions attended yet
- [ ] **Sean Fitzgerald** — paid €449, zero sessions attended. Follow up.
- [ ] **Niall O'Brien** — paid €449, zero sessions attended. Follow up.

### Notes
- Course started Sunday March 22nd
- These students have paid the full bundle but haven't shown up to any sessions
- Need to reach out to confirm they're aware of schedule / have access

---

## 🔮 Longer Term

- [ ] Add Google/social login to reduce checkout friction for younger users
- [ ] Add phone number field to checkout for SMS follow-up / remarketing
- [ ] Consider a dedicated landing page for in-person Limerick grinds (separate from online products)
- [ ] SEO audit — optimise for "maths grinds Limerick", "leaving cert maths grinds", etc.


## 🛠️ Infrastructure & Platform

- [ ] **Upgrade QMD to hybrid search** — Config already wired (vector + BM25 + temporal decay + MMR diversity). Just needs: top up OpenAI credits OR add free Gemini embedding API key, then change `searchMode: "search"` → `"query"` in openclaw.json. Priority increases as vault/memory files grow.
- [ ] **Top up OpenAI credits** — GPT-5.4 + GPT-4o failing, affects Pixel (content) agent + hybrid search embeddings
- [ ] **Top up xAI credits** — Scout agent + x_search both down
- [ ] **Install noVNC for Meta login** — `sudo apt install -y x11vnc novnc` (needs sudo access)
