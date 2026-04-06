# Server Resource Tracking

## VPS: 172.239.114.188 (Main + Nexus)
- **RAM:** 8GB total. As of 2026-04-05 08:07 UTC: only 259MB free, 46MB swap in use. CRITICAL.
  - Root cause: Nexus deployment added ~740MB (gateway 597MB + next-server 143MB)
  - Main gateway: ~770MB across 2 processes
  - SearXNG, Docker, PM2 dashboards also running
- **Disk:** 56% as of 2026-04-05. Was 41% on 2026-04-04 morning. +15pp in one day.
  - Nexus npm/node caches: ~9.3GB (safe to clear)
  - Two Next.js mission controls + git repos
- **Action needed:** Upgrade to 16GB RAM, or stop Nexus gateway when not testing. Clear npm caches for disk.

## VPS: 172.239.98.61 (Kilmurry / Kate)
- Kate's gateway deployed 2026-04-04
- Resource usage unknown — need SSH password to check
- Running: openclaw-kate gateway, kilmurry-kate-mc (PM2), health crons

## Trends
| Date | RAM Free | Disk % | Notes |
|------|----------|--------|-------|
| Apr 3 | ~512MB | 41% | Pre-deployment baseline |
| Apr 4 07:04 | 512MB | 41% | Morning |
| Apr 4 23:04 | — | 56% | Post Nexus+Kate deployments |
| Apr 5 06:07 | 389MB | 56% | Swap starting |
| Apr 5 08:07 | 259MB | 56% | Critical — 46MB swap |
