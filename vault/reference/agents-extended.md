# AGENTS.md Extended Reference
# Moved here to keep AGENTS.md lean (<10KB). These are still rules — just not needed in every prompt.

## 🏗️ Client Infrastructure Documentation Protocol

**Rule: Any time I make changes to a client's OpenClaw setup, I MUST update their documentation before considering the task done.**

### What triggers an update:
- Installing/changing systemd services, cron jobs, health scripts
- Changing models, channels, agent configuration
- Adding/removing skills or cron jobs
- Fixing infrastructure issues (PM2, Chrome, RAM, etc.)
- Deploying new tools, dashboards, or monitoring
- Any SSH work that changes the server state

### What to update:
1. **Architecture schematic** — `consultancy/clients/<client>/architecture-schematic.md`
2. **Workspace-consultancy copy** — keep in sync
3. **Mission Control** — rebuild so client page reflects current state
4. **MEMORY.md / vault pointers** — if significant

### The test:
*"If Jonny opens Mission Control right now, does the client page show the actual current state?"* If no → update it.

### Client Server Backups — MANDATORY

Every time I make changes to a client's server, commit and push before considering done.

| Client | Repo | What's backed up |
|--------|------|-----------------|
| Kilmurry Lodge | `github.com/Jonnyhimalaya/Kilmurry` | Workspace + config-backup/ |

## Standing Rules — Infrastructure Changes

1. **Verify CLI commands before writing them into service files.** Run `<command> --help` first.
2. **Check logs immediately when a service fails.** `journalctl -u <service-name> --no-pager -n 30`.
3. **Systemd services don't inherit shell env vars.** Use `EnvironmentFile=` or `Environment=` directives.
4. **Prefer hardcoded config or EnvironmentFile over bare env vars.** Shell exports are fragile.
5. **Test the migration before killing the old process.**

## Debugging Protocol — When Stuck

1. Search GitHub issues first (`github.com/openclaw/openclaw/issues`)
2. Search Twitter/X for the error + "openclaw"
3. Search Reddit (`r/openclaw`) and OpenClaw Discord
4. Check release notes for recent fixes/regressions
5. Stop theorising after 3 failed attempts — search externally

## Group Chat Rules (Extended)

### 💬 When to Speak
- Directly mentioned or asked a question
- Can add genuine value (info, insight, help)
- Something witty/funny fits naturally
- Correcting important misinformation

### Stay silent when:
- Casual banter between humans
- Someone already answered
- Your response would just be "yeah"
- The conversation flows fine without you

### 😊 Reactions
Use emoji reactions naturally on platforms that support them. One per message max.

## 💓 Heartbeat Details

### Heartbeat vs Cron
- **Heartbeat:** batch checks, conversational context, timing can drift
- **Cron:** exact timing, isolation from main session, different model/thinking

### Things to check (rotate 2-4x/day):
- Emails, calendar (next 24-48h), social mentions, weather

### When to reach out:
- Important email, calendar event <2h, interesting finding, >8h since last contact

### When to stay quiet:
- Late night (23:00-08:00), human busy, nothing new, checked <30 min ago

### Memory Maintenance (During Heartbeats)
Periodically review recent daily files → update MEMORY.md with distilled learnings → remove outdated info.

## Memory Protocols (Extended)

### Protocol C: Periodic Memory Checkpoint (every ~150 messages)
Every ~150 messages, flush unsaved events to `memory/YYYY-MM-DD.md` with marker:
`### Memory Checkpoint — HH:MM UTC (msg ~N)`
Track in `memory/heartbeat-state.json` under `session.lastCheckpointMsgCount`.

### Protocol D: Post-/new Transcript Rescan
On new session startup, check `ls -t ~/.openclaw/agents/main/sessions/*.reset.* | head -3`.
If newest is from today/yesterday: extract key events, compare against memory, append missing with `[RECOVERED]` tag.

Scan for: config changes, bug fixes, decisions, tool/access changes, bash commands Jonny ran.

## Artifacts Protocol
Central protocol: `/home/jonny/.openclaw/workspace/artifacts/PROTOCOL.md`
Artifact directory: `/home/jonny/.openclaw/workspace/artifacts/YYYY-MM-DD/`
