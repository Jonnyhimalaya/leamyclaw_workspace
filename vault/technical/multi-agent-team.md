# Multi-Agent Team — Architecture & Status

## Overview (LIVE since March 26, 2026)
- Orchestrator (Opus 4.6) = single point of contact for Jonny
- Linode: 8GB RAM (upgraded from 4GB on Mar 26)

## Agents
| ID | Name | Emoji | Model | Role | Status |
|----|------|-------|-------|------|--------|
| main | Orchestrator | 🧠 | claude-opus-4-6 | Strategy, delegation, Jonny's direct contact | Active |
| sitemgr | Wrench | 🔧 | claude-sonnet-4-6 | WordPress/WooCommerce admin | Ready |
| marketing | Prism | 📊 | claude-sonnet-4-6 | Analytics, ads, copy, strategy | Ready |
| scout | Radar | 🔍 | xai/grok-3-mini | Twitter/AI research | Ready |
| content | Pixel | 🎨 | openai/gpt-5.4 | Social media, graphics | Ready |

## Architecture
- Each agent: own workspace (`~/.openclaw/workspace-{id}/`), own SOUL.md, AGENTS.md, tool permissions
- Sub-agent spawning: `sessions_spawn(agentId=...)`, they report back
- Tool restrictions: specialists have denied tools to keep them in lane
- Fallback chain: cross-provider (Opus → Sonnet → GPT-5.4 → GPT-4o)

## Discord Bindings (Completed Mar 30)
- 6 channel bindings: #orchestrator→main, #sitemgr→sitemgr, #marketing→marketing, #scout→scout, #content→content, #task-log→main
- Thread bindings enabled (spawnSubagentSessions: true, idleHours: 24)
- First real Wrench delegation: Josephine Lijo → Revision 2026 bundle, post #79548

## Lessons Learned
- Don't spawn all agents in parallel — rate limits cascade. Stagger 1-2 at a time.
- Fallbacks must cross providers or rate limits compound
- WooCommerce membership bug: post_status saves as "publish" not "wcm-active"
- For Jonny to watch agent conversations: use Discord #orchestrator, not Telegram

## Scout Cron Jobs
- Morning (8am Dublin) + evening (6pm Dublin) scans
- xAI API key configured (XAI_API_KEY env var in systemd)

## TODO
- OpenAI quota needs topping up (GPT-5.4 + GPT-4o failing)
- noVNC install for Meta login
- Marketing weekly Monday report cron
