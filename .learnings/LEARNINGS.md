# Learnings
> Patterns, discoveries, things worth remembering.

## 2026-04-03
- GEO-SEO: leamymaths.ie scores 74/100 — missing FAQ schema, ai.txt, external links
- OnlyTerp autoDream pattern: Memory consolidation system from Claude Code leak — gates trigger consolidation every 5+ sessions / 24h+
- Gonto EA Skills: Full EA replacement with 6 skills (meeting-prep, action-items, email-drafting, executive-digest, todoist-due-drafts, humanizer)
- SlowMist: Red line / yellow line command classification — proper security architecture for high-privilege agents
- OnlyTerp anti-patterns: "Don't give 5 options when 1 is clearly right — just do it"

## 2026-04-08
- When a bug lives inside a remote app on its own server, the local/server-native agent often has a much better execution path than remote SSH patching. Use the central agent for diagnosis and orchestration, but prefer the server-local agent for repetitive edit-build-restart-debug loops when remote quoting, SCP, or cross-machine patching adds friction.

## 2026-04-20
- **MiroFish report cheap iteration:** `/api/report/generate` with `force_regenerate: true` reruns only the Report Agent on existing simulation data. Sim rounds are preserved. Never rerun a full sim just to fix a shallow report.
- **MiroFish agent cap is hardcoded:** `max_agents_allowed = int(num_entities * 0.9)`. Seed density drives agent count. Not a Zep tier issue.
- **Kilmurry Kate gateway restart pattern:** Her gateway does NOT auto-restart on upgrade like Jack's does. Must manually `pkill -f "openclaw-gateway" -u kateuser` then spawn fresh with nohup.
- **Anthropic Apr 4 cutoff scope:** Direct API cron jobs fail. ACP→Claude Code interactive bots continue working on Max subscription. Route crons through Codex OAuth (free via existing subscription) for instant fix.
- **Telegram authorised relay pattern:** Prefix content with `[From Stephen, authorised relay to Jack]` + paste into Kilmurry TUI. Jack's bot correctly distinguishes ambient requests from authorised relays and forwards cleanly.
- **Jack's bot graceful long-message handling:** Hit Telegram 4096 char limit → bot auto-split into 1/2 + 2/2 and attached file separately, all delivered successfully in sequence.
