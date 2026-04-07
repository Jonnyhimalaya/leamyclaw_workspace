# Tool/Command Errors
> Things that broke and how they were fixed.

## 2026-04-03
- `geo` CLI: First run failed on Python deps — needed `--break-system-packages` flag
- Browser login to X/Twitter: Blocked by bot detection — use BookmarkSave extension instead
- Kilmurry Lodge site: Times out from VPS (blocks non-browser requests or geo-restricted)
- leamyclaw+1 WP account: Editor role only, cannot access AIOSEO settings or plugins

## 2026-04-07
- `chattr +i` on exec-approvals.json blocks gateway from reading the file entirely (EPERM on open). Immutable flag prevents ALL file operations, not just writes. Only use on truly static files (SOUL.md, AGENTS.md). Never on config files the gateway reads at runtime.
- Protocol C failure: did significant Kate TG bot + Whisper setup work across an entire session without checkpointing to memory. When Jonny did /new, all context was lost. Always checkpoint after significant work blocks.
