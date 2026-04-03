# Leamy Maths GEO Fixes — Deployment Guide
> Goal: Push GEO score from 74/100 → 85+/100
> All files ready in this folder. Just need to upload to WordPress.

---

## Fix 1: FAQPage Schema (+5-8 points)
**File:** `faq-schema-snippet.html`
**Where:** WordPress → Appearance → Theme Header/Footer plugin, or paste into homepage template before `</body>`
**What it does:** Tells AI engines "here are structured Q&As" — they love citing FAQ content directly in responses.

## Fix 2: AI Discovery Endpoints (+5-8 points)
Upload these 3 files to the WordPress root:

| File | Upload to | Purpose |
|------|-----------|---------|
| `well-known-ai.txt` | `/.well-known/ai.txt` | Declares AI crawler permissions |
| `ai-summary.json` | `/ai/summary.json` | Site identity for AI engines |
| `ai-faq.json` | `/ai/faq.json` | Structured FAQ for AI search |

**WordPress method:** Use a file manager plugin or FTP. The `.well-known` directory may need to be created.

## Fix 3: External Authority Links (+3-5 points)
Add outbound links to authoritative sources on the homepage. Suggestions:
- Link to SEC.ie (State Examinations Commission) from exam-related content
- Link to curriculumonline.ie from curriculum mentions
- Link to education.ie from any policy/system references
- Link to NCCA.ie from syllabus mentions

**Why:** AI engines use outbound links to gauge whether you're a credible source or a closed ecosystem.

## Fix 4: RSS Feed (+2-3 points)
If WordPress blog is active, ensure RSS is enabled and add to `<head>`:
```html
<link rel="alternate" type="application/rss+xml" title="Leamy Maths Blog" href="https://leamymaths.ie/feed/" />
```

## Fix 5: Organization Schema sameAs (+2-3 points)
Add social/knowledge graph links to existing Organization schema:
```json
"sameAs": [
  "https://www.facebook.com/leamymaths",
  "https://www.instagram.com/leamymaths",
  "https://www.linkedin.com/company/leamy-maths"
]
```

## Fix 6: Hidden Text Cleanup (+1-2 points)
The audit flagged hidden text (display:none with content) and aria-hidden injection. Check homepage for:
- Cookie banners with hidden content that contains keyword-stuffed text
- Any elements with `display:none` that have substantial text inside

**Why:** AI crawlers can read hidden text and may penalize it as cloaking.

## Expected Result
| Fix | Points | Effort |
|-----|--------|--------|
| FAQPage schema | +5-8 | 5 min |
| AI discovery endpoints | +5-8 | 10 min |
| External links | +3-5 | 10 min |
| RSS feed | +2-3 | 5 min |
| sameAs links | +2-3 | 5 min |
| Hidden text cleanup | +1-2 | 15 min |
| **Total** | **+18-29** | **~50 min** |

**Projected score: 74 + 18-29 = 92-100+ (EXCELLENT)**

---

*Generated from GEO-SEO audit 2026-04-03. Re-run audit after deployment to verify.*
