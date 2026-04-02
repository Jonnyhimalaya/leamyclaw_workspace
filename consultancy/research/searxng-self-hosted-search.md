# SearXNG as Self-Hosted Search for OpenClaw Deployments

**Created:** 2026-04-02
**Source:** OpenClaw v2026.4.1 release (#57317), real-world Brave rate-limit failures

## Problem
Brave Search Free plan has a 1 req/sec rate limit and 2,000 queries/month quota. Any multi-agent setup doing regular web research will hit this quickly. We hit it on day 1 of our daily intel pipeline.

Paid Brave plans exist but add recurring cost and still have rate limits.

## Solution: SearXNG
SearXNG is an open-source meta-search engine. It aggregates results from Google, Bing, DuckDuckGo, and 70+ other engines. Self-hosted, no API keys, no rate limits.

As of v2026.4.1, OpenClaw has first-party SearXNG support as a `web_search` provider plugin.

## Deployment

### Docker (recommended)
```bash
docker run -d --name searxng -p 8888:8080 \
  -v searxng-data:/etc/searxng \
  searxng/searxng
```

### OpenClaw Configuration
In `openclaw.json`:
```json
{
  "plugins": {
    "web_search": {
      "provider": "searxng",
      "host": "http://localhost:8888"
    }
  }
}
```

## Advantages for Client Deployments
1. **Zero recurring cost** — no API subscription
2. **No rate limits** — search as aggressively as needed
3. **Privacy** — searches don't go through third-party APIs
4. **Redundancy** — if Google is throttling, SearXNG falls back to other engines
5. **Air-gapped compatible** — for security-conscious clients

## Considerations
- Adds a Docker container to maintain (~50MB RAM)
- Google may occasionally CAPTCHA the SearXNG instance; DuckDuckGo/Bing provide backup
- Should configure `searxng/settings.yml` to disable unnecessary engines and enable JSON output format

## Consultancy Recommendation
Make SearXNG deployment a standard step in our `universal-openclaw-implementation.md` playbook. For clients on Brave Free, this eliminates a class of reliability issues entirely.
