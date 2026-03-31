# HEARTBEAT.md

## Step 0: Autonomy Check (FIRST)
- Read `memory/heartbeat-state.json` → check `autonomy.lastHumanMessage`
- Calculate time since last human message
- Set autonomy level: responsive (<30m) | ambient (30m-2h) | proactive (2-8h) | dormant (8h+ or 23:00-08:00)
- If **dormant**: skip ALL checks below. Return `HEARTBEAT_OK` immediately unless server health fails.
- If **responsive**: only do Memory File Check + Server Health. Don't initiate background work.
- If **ambient** or **proactive**: do all applicable checks below.

## Memory File Check
- Check if `memory/YYYY-MM-DD.md` exists for today. If not, create it with a timestamp header.
- If it exists but hasn't been updated in this session, add a note that a heartbeat ran.

## Server Health (Quick)
- Run: `bash /home/jonny/.openclaw/workspace/scripts/server-health.sh`
- If it reports issues (exit code 1), fix what you can (kill Chrome, orphan processes) and alert Jonny if critical
- If OK, no action needed — the cron job logs it every 4 hours

## Session Context Check (TUI + Telegram)
Check both active sessions for bloat. Run:
```
for f in $(ls -t /home/jonny/.openclaw/agents/main/sessions/*.jsonl 2>/dev/null | head -3); do
  msgs=$(grep -c '"role"' "$f" 2>/dev/null || echo 0)
  echo "$msgs $f"
done
```
Thresholds (apply to both TUI and Telegram sessions):
- **> 100 messages**: ⚠️ Alert Jonny — "Session getting large (X msgs). Consider /new to avoid overloaded errors."
- **> 200 messages**: 🚨 Escalate — "Session critically large (X msgs) — likely causing API 529 errors. Reset with /new now."

Note: Telegram caches better so can tolerate slightly more, but same rules apply. Current Telegram session hit 420 msgs before causing issues (Mar 27).
