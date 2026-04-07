# OpenClaw Upgrade Safety Checklist — v2026.4.5

_Created: 2026-04-07 | Source: Community X posts + own analysis_

## Pre-Upgrade
- [ ] `cp openclaw.json openclaw.json.bak` (and any custom agent configs)
- [ ] Disable dreaming mode if enabled (agents can corrupt configs during upgrade)
- [ ] Note current version: `openclaw --version`
- [ ] Run `openclaw doctor --fix` on current version first (catches pre-existing issues)

## Upgrade
- [ ] `openclaw update` (or `git pull && npm install` for git installs)
- [ ] On macOS: `openclaw gateway install --force` (entrypoint changed entry.js → index.js)

## Post-Upgrade
- [ ] Run `openclaw doctor --fix` — **repeat 2-3 times** (some fixes are iterative)
- [ ] Run `openclaw doctor` (no --fix) to verify clean
- [ ] Run `openclaw status --verbose` to check all services
- [ ] Manual checks needed (doctor doesn't fix):
  - Discord channel configs: `allow` → `enabled`
  - Stale plugin paths (XAI x_search, Firecrawl web_fetch moved to plugin-owned paths)
  - Remove `personalityOverlay` if present
  - Remove `agents.defaults.cliBackends` if present
  - Remove `agents.*.sandbox.perSession` if present
- [ ] Test exec approvals flow
- [ ] Test plugin functionality (web_search, x_search, etc.)
- [ ] Re-enable dreaming mode

## Breaking Changes (Full List)
Legacy config aliases removed:
- `talk.voiceId` / `talk.apiKey`
- `agents.*.sandbox.perSession`
- `browser.ssrfPolicy.allowPrivateNetwork`
- `hooks.internal.handlers`
- Channel/group/room `allow` toggles (now `enabled`)
- `agents.defaults.cliBackends` (CLI backends like Claude CLI purged)

## Bug Fixes Worth Knowing
- Gateway/exec loopback: restored legacy-role fallback for empty paired-device token maps (fixes `pairing-required` errors)
- Subagents: pinned admin-only calls to `operator.admin` (fixes `sessions_spawn` dying on loopback scope-upgrade)
- Exec approvals: strips invalid security/ask values from `exec-approvals.json` (fixes corrupted runtime policy)

## Rollback
If things break badly: `cp openclaw.json.bak openclaw.json && openclaw restart`
Then seek help on GitHub issues or X (@openclaw).
