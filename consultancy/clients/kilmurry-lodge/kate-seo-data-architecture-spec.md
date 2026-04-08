# Kate Marketing Control Panel — SEO & Data Architecture Build Spec

**Client:** Kilmurry Lodge Hotel  
**Owner:** Kate Taylor  
**Prepared by:** OpenClaw  
**Date:** 2026-04-08

## 1. Objective

Build the SEO, analytics, local visibility, and content-planning parts of Kate's Marketing Control Panel so they work with free data sources first, then accept Semrush later without rebuilding the dashboard structure.

The core principle is:

**Build around business objects and decisions, not around vendor tools.**

The UI should show things like:
- keyword performance
- page performance
- competitor gaps
- local visibility
- technical health
- recommended actions

It should NOT be hard-coded as:
- Search Console tab
- GA4 tab
- Semrush tab

## 2. Architecture Principle

Use a 3-layer architecture.

### Layer 1 — Ingestion
Each source writes raw or lightly-normalized JSON into the data layer.

### Layer 2 — Domain Model
Combine source data into shared business objects used by the UI.

### Layer 3 — Insight Layer
Claude/OpenClaw reads the normalized objects and generates:
- plain-English summaries
- trend explanations
- priority actions
- content opportunities
- competitor positioning notes

This means Semrush can be added later as another input to the same domain model, instead of forcing a dashboard rebuild.

## 3. Phase 1 Data Sources (Build These First)

### 3.1 Google Search Console API
**Role:** Primary source of SEO performance for Kilmurry's own site.

**Key outputs:**
- queries
- clicks
- impressions
- CTR
- average position
- page/query combinations
- indexing signals (where available via related tooling)

**Feeds:**
- Module A: SEO / AEO Performance
- Module B: Content Planning
- Module C: Executive / Analytics Summary

### 3.2 Google Analytics 4 Data API
**Role:** On-site user behaviour and conversion context.

**Key outputs:**
- sessions
- users
- landing pages
- bounce / engagement signals
- session duration
- conversions / key events
- source / medium / channel group

**Feeds:**
- Module C: Executive / Analytics Summary
- Module B: Content Planning
- Module D: Conversion / Landing Page Performance

### 3.3 Google Business Profile API
**Role:** Local visibility and local action tracking.

**Key outputs:**
- listing views
- website clicks
- calls
- direction requests
- review signals
- photo engagement

**Feeds:**
- Module E: Reputation & Local Visibility
- Module C: Executive / Analytics Summary

### 3.4 PageSpeed Insights API
**Role:** Technical SEO / Core Web Vitals / page performance diagnostics.

**Key outputs:**
- performance score
- accessibility / best practices / SEO score where useful
- LCP
- INP / interaction metrics
- CLS
- page-level opportunities and diagnostics

**Feeds:**
- Module A: SEO / AEO Performance
- Module F: Technical Health

## 4. Phase 2 Data Source

### 4.1 Semrush API
**Role:** Competitive and advanced SEO enrichment.

**Add later for:**
- competitor rankings
- keyword gaps
- keyword difficulty
- backlink gaps
- site audit issue scoring
- historical rank tracking
- competitor domain visibility

**Feeds:**
- Module G: Competitive Intelligence
- Module A: SEO / AEO Performance
- Module B: Content Planning
- Module H: Paid Media / Search Opportunity Layer

## 5. Domain Model (Tool-Agnostic)

These are the normalized objects the front end should consume.

### 5.1 KeywordPerformance
Fields:
- keyword
- clicks
- impressions
- ctr
- avgPosition
- trendDirection
- source
- targetPage
- searchIntent
- cluster
- notes

### 5.2 PagePerformance
Fields:
- pageUrl
- pageTitle
- organicClicks
- organicImpressions
- avgPosition
- ctr
- sessions
- engagementRate
- avgSessionDuration
- conversions
- pageSpeedScore
- coreWebVitals
- issues[]

### 5.3 LocalVisibility
Fields:
- listingViews
- websiteClicks
- calls
- directionRequests
- photoViews
- reviewVelocity
- avgRating
- reviewThemes[]

### 5.4 CompetitorGap
Fields:
- competitorName
- keywordGap[]
- backlinkGap[]
- rankingAdvantage[]
- weakness[]
- opportunity[]

### 5.5 TechnicalIssue
Fields:
- pageUrl
- issueType
- severity
- metric
- currentValue
- recommendedFix
- owner

### 5.6 ContentOpportunity
Fields:
- topic
- targetKeyword
- supportingKeywords[]
- intent
- difficulty
- currentGap
- recommendedAssetType
- source

### 5.7 ExecutiveInsight
Fields:
- title
- summary
- whyItMatters
- recommendedAction
- priority
- confidence
- sourceModules[]

## 6. Dashboard Module Map

### Module A — SEO / AEO Performance
**Primary inputs:** Search Console + PageSpeed  
**Later enrich with:** Semrush

Show:
- top keyword movers
- CTR winners / underperformers
- page-level SEO performance
- AEO opportunities (FAQ, schema, intent gaps)
- Core Web Vitals summary
- top technical blockers

### Module B — Content Planning
**Primary inputs:** Search Console + GA4  
**Later enrich with:** Semrush

Show:
- content gaps from queries with impressions but weak CTR/rank
- emerging query themes
- content ideas by intent cluster
- underperforming pages that need refreshes
- recommended next content actions

### Module C — Executive / Analytics Summary
**Primary inputs:** GA4 + Search Console + GBP

Show:
- key KPIs
- acquisition trends
- local action trends
- organic performance trends
- short plain-English summary
- priority actions this week

### Module D — Conversion / Landing Page Performance
**Primary inputs:** GA4 + Search Console + PageSpeed

Show:
- landing pages by traffic
- landing pages by conversion performance
- bounce / engagement issues
- pages with strong impressions but weak conversion behaviour

### Module E — Reputation & Local Visibility
**Primary inputs:** GBP + review inputs

Show:
- local actions trend
- review velocity
- rating trend
- dominant positive / negative themes
- location-specific visibility notes

### Module F — Technical Health
**Primary inputs:** PageSpeed + internal audits

Show:
- page-level performance scores
- CWV failures
- issue severity table
- quick-win fixes
- top pages needing technical attention

### Module G — Competitive Intelligence (Phase 2)
**Primary inputs:** Semrush

Show:
- competitor keyword overlaps
- missing rankings
- backlink gaps
- defensive vs offensive keyword opportunities

### Module H — Paid + Search Opportunity Layer (Phase 2)
**Primary inputs:** Semrush + Google Ads + Meta

Show:
- terms worth defending organically vs buying via paid
- overlap between organic weakness and ad opportunity
- competitor paid pressure signals

## 7. Insight Layer

The agent should not just display numbers. It should generate useful interpretation.

Examples:
- "Your ranking for 'Ryder Cup 2027 accommodation Limerick' improved from 12 to 7 this week. CTR is still low for that position. Add FAQ schema and stronger transport copy."
- "This page gets impressions but weak sessions and low engagement. Search intent and page promise likely misaligned."
- "Competitor X is winning local-intent queries you are absent from. Build a dedicated venue/accommodation landing page."

### Insight output requirements
Each insight should include:
- what changed
- why it matters
- confidence level
- recommended next action
- linked source data

## 8. Storage Pattern

Recommended structure under Kate dashboard data layer:

```text
data/
  seo/
    search-console.json
    pagespeed.json
    normalized-keywords.json
    normalized-pages.json
    insights.json
  analytics/
    ga4.json
    normalized-analytics.json
  local/
    gbp.json
    reputation.json
  competitors/
    semrush.json
    competitor-gaps.json
```

The UI should read normalized files where possible, not raw vendor responses.

## 9. Build Sequence

### Phase 1A — Foundation
- Add Search Console ingestion
- Add PageSpeed ingestion
- Normalize keyword + page performance objects
- Build SEO / AEO panel from normalized data

### Phase 1B — Analytics Layer
- Add GA4 normalized analytics layer
- Wire landing page and executive summary sections

### Phase 1C — Local Layer
- Add Google Business Profile integration
- Add local visibility + reputation panels

### Phase 2 — Semrush Enrichment
- Add competitor gap objects
- enrich keyword and content modules
- build true competitor intelligence panel

## 10. Build Rule

Do not hard-code any module to a single vendor.

Every module should be able to accept:
- free-source-only data in Phase 1
- richer mixed-source data in Phase 2
- replacement paid source later if Semrush changes

## 11. Immediate Implementation Recommendation

Start with:
1. normalized SEO data model
2. Search Console ingestion
3. PageSpeed ingestion
4. SEO / AEO page rebuild around normalized objects

That gives Kate a meaningful live SEO module quickly, without waiting on Semrush or the full analytics stack.
