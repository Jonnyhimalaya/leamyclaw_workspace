echo "memory + learnings logged"

## Next.js hydration mismatch — the date pattern (2026-04-22)
Symptom: "Application error: a client-side exception has occurred" on a Next.js 14 page.
Root cause: `new Date().toLocaleDateString()` (or any `Math.random`) during render body produced different output server (UTC) vs client (local TZ) → React hydration mismatch → crash.
Fix: Move time/random values into useEffect; add suppressHydrationWarning on rendered values.
Rule: NEVER call new Date / Date.now / Math.random in a component's render body if it's part of SSR output.

## API schema collision between report + deep-dive components (2026-04-22)
Landing report component and deep-page component both fetched /api/X but expected different shapes. Landing did data.rows.map() → crash when API returned the deep-page shape.
Rule: when splitting a component into a report summary + deep-dive page, give each its own API route (e.g. /api/pickup-velocity vs /api/pickup). Don't overload one route with two consumers.
Diagnostic pattern that worked: app/error.tsx Error Boundary + /api/client-error POST endpoint that logs the error to a file on the server. Screen shows the real error, server gets a copy.

## 2026-04-25 — Media/file handling silent failure on claude-cli provider
- **Context:** Aidan's bot deployed using `claude-cli` provider (Claude Code OAuth). Worked for text. Silently failed for images and files with "Something went wrong" — Aidan experienced this but couldn't diagnose it.
- **What failed:** `claude-cli` (headless `--print` subprocess) discards image/file attachments. The agent run blows up silently. Non-technical clients don't know why, they just stop using it.
- **Root cause:** Deployed using `claude-cli` OAuth path. Transport doesn't support vision. Text-only confirmation during setup masked this.
- **Fix:** Switch to `anthropic` provider using the OAuth bearer token directly. Same wallet, same account, but via Anthropic API (which handles vision). Run `openclaw models auth login --provider anthropic` → setup-token → paste the `sk-ant-oat01-...` token.
- **New constraint (Anthropic April 4, 2026 policy):** Even with `anthropic` provider, if client account has no "extra usage" funded (separate from subscription), API calls get billing error. Subscription quota does NOT cover third-party API use.
- **Prevention:** Section 1.4 added to universal playbook. Three mandatory tests before any deployment is marked done: (1) text, (2) image from phone, (3) PDF/doc. Fail any → not done.
