# Leamy Maths — Consolidated AI Visibility Score
> Date: April 3, 2026 | Two audits, one picture

## The Two Scores Explained

We ran **two different audits** that measure different things:

| Audit | Score | What It Measures |
|-------|-------|-----------------|
| **GEO Readiness** (geo-seo-claude) | **74/100 ✅** | Can AI bots find, crawl, and understand your site? |
| **Citability** (citability module) | **39/100 ❌** | Can AI models quote your content in their answers? |

**Think of it like a library:**
- 74/100 = The library has clear signage, a good catalogue, the doors are open → ✅ AI can find you
- 39/100 = But the best books are locked in a back room → ❌ AI can't recommend what it can't read

## GEO Readiness Breakdown (74/100)

| Check | Score | Status |
|-------|-------|--------|
| Robots.txt (AI bot access) | 15/18 | ✅ All 27 bots allowed |
| llms.txt (AI index file) | 15/18 | ✅ Exists, 1,367 links, but no descriptions |
| Schema markup | 10/16 | ⚠️ Has basics, missing FAQPage + Course |
| Meta tags & Open Graph | 14/14 | ✅ Perfect |
| Content accessibility | 11/12 | ✅ Works without JS |
| Freshness signals | 4/6 | ✅ Recent update date present |
| AI discovery endpoints | 0/6 | ❌ No ai.txt, ai-summary.json, ai-faq.json |
| Brand entity signals | 5/10 | ⚠️ Missing sameAs (Wikipedia, LinkedIn) |

## Citability Breakdown (39/100)

| Content Block | Score | Problem |
|---------------|-------|---------|
| "Privacy Overview" (cookie policy) | 58/100 | Best scoring block — the cookie text is more citable than course content |
| "Packed with Valuable Resources" (Stephen's bio) | 33/100 | Too short, not self-contained |
| Course listings | 27/100 | Product cards only — zero educational substance |

**Why it's low:** The homepage is a storefront, not a knowledge base. AI models can see *that you exist* (74/100) but when asked "What's the best way to prepare for Leaving Cert maths?" they have nothing quotable from your site (39/100).

## Combined Assessment

**Leamy Maths is technically well-set-up but content-empty for AI.**

Your infrastructure is solid — bots can crawl, schema exists, meta tags are perfect. But the public-facing pages are thin on the educational content that AI models actually cite. All the good stuff is behind the WooCommerce login.

### Priority Fixes (Impact Order)

| # | Fix | Effort | Impact on Citability | Impact on Readiness |
|---|-----|--------|---------------------|-------------------|
| 1 | **Add FAQ content + FAQPage schema** to homepage | Medium | +15-20 pts | +3 pts |
| 2 | **Create public educational content pages** ("Guide to LC HL Maths", study tips, exam prep advice) | High | +20-30 pts | +2 pts |
| 3 | **Build /llms-full.txt** with 2-3 sentence descriptions per page | Low | +5-10 pts | +3 pts |
| 4 | **Add /.well-known/ai.txt + /ai/summary.json + /ai/faq.json** | Low | +5 pts | +6 pts (→ perfect) |
| 5 | **Add Course schema** (@type: Course, syllabus, instructor) | Low | +3-5 pts | +4 pts |
| 6 | **Add sameAs links** (LinkedIn, education directories) | Low | +2 pts | +3 pts |
| 7 | **Publish student outcomes** (pass rates, testimonials, stats) | Medium | +10-15 pts | +1 pt |

### Projected Scores After Fixes
- **GEO Readiness:** 74 → ~90/100 (A)
- **Citability:** 39 → ~70-80/100 (B-A)

### Files Already Prepared (Ready to Deploy)
- `vault/research/geo-seo/leamymaths-fixes/faq-schema-snippet.html`
- `vault/research/geo-seo/leamymaths-fixes/ai-faq.json`
- `vault/research/geo-seo/leamymaths-fixes/ai-summary.json`
- `vault/research/geo-seo/leamymaths-fixes/well-known-ai.txt`
- `vault/research/geo-seo/leamymaths-fixes/DEPLOYMENT-GUIDE.md`

## Bottom Line

**74/100 and 39/100 are both real — they're just measuring different things.** The site's plumbing is great. The content AI models can actually cite is thin. Fix the content gap and both scores climb together.
