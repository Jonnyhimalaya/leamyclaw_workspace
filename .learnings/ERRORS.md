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
