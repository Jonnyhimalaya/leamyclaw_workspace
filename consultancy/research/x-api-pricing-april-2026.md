# X API Pricing Changes — April 20, 2026

## Summary
X overhauled API pricing effective 2026-04-20. Read-heavy agents benefit; write-heavy automation with links becomes expensive.

## New Pricing
| Action | Old (approx) | New | Change |
|--------|-------------|-----|--------|
| Owned Reads (GET /users/{id}/tweets, /mentions, /liked_tweets, /followers, etc.) | ~$0.01/req | $0.001/req | **90% cheaper** |
| Writes/Posts (POST /2/tweets) | $0.01/post | $0.015/post | 50% increase |
| Posts with URLs | $0.01/post | **$0.20/post** | **20x increase** |
| Summoned replies | — | $0.01/post | Unchanged |
| Following/unfollowing, liking/unliking, quote-posting | Available | **Removed from self-serve** | Blocked |

## Implications for Our Deployments

### Scout Agent (Positive)
- Scout does pure read operations via x_search/Grok
- Cost per scan drops significantly
- Can increase scan depth or frequency if needed

### Client Social Automation (Negative)
- Any automated X posting with links (hotel deals, course promotions) costs $0.20/post
- At 3 posts/day with links = $18/month — not catastrophic but 20x the old cost
- Link-free posts (engagement, replies) remain cheap at $0.015
- **Recommendation:** For client social automation, prefer link-in-bio / pinned post patterns over per-post links

### Consultancy Guidance
- Read-monitoring agents: now very cost-effective to offer
- Social posting agents: need cost modelling per client before deployment
- Quote-posting removed from API: impacts repost/amplification bots entirely
- Following/unfollowing removed: kills growth-hacking automation via API

## Source
@XDevelopers thread (April 16, 2026): https://devcommunity.x.com/t/x-api-pricing-update-owned-reads-now-0-001-other-changes-effective-april-20-2026/263025
