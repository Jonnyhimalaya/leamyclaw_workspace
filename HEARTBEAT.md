# HEARTBEAT.md

## Memory File Check
- Check if `memory/YYYY-MM-DD.md` exists for today. If not, create it with a timestamp header.
- If it exists but hasn't been updated in this session, add a note that a heartbeat ran.

## Server Health (Quick)
- Run: `bash /home/jonny/.openclaw/workspace/scripts/server-health.sh`
- If it reports issues (exit code 1), fix what you can (kill Chrome, orphan processes) and alert Jonny if critical
- If OK, no action needed — the cron job logs it every 4 hours
