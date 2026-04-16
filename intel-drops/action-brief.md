# 🧠 Morning Action Brief — 2026-04-16

## 🔴 Fix Now

### 1. Jack's Claude Code ACP Harness Is Broken (or Silently Burning Credits)
- **Intel:** Anthropic cut off Claude Pro/Max/Team subscription coverage for third-party harnesses on April 4. One-time credit ($200 for Max) expires **tomorrow, April 17**.
- **Our exposure:** Jack's Kilmurry ACP harness was specifically architected to route build work through his Claude Max team subscription to avoid API billing. That subscription path has been blocked for 12 days. Either Jack's builds are failing, or he's unknowingly burning "extra usage" credits at pay-per-token rates. We set this up for him — we need to fix it.
- **Recommended action:**
  1. Contact Jack TODAY — confirm whether his Claude Code builds are still working and what billing he's seeing.
  2. If his one-time credit hasn't been redeemed, help him claim it before the April 17 deadline (tomorrow).
  3. Migrate his ACP harness to one of: (a) Anthropic API key billing (cleanest), (b) "extra usage bundles" at the current 30% discount, or (c) the Cowork bridge workaround (sub-safe, Claude Cowork reads shared files — 15-min setup per community reports). Option (a) is most robust long-term.
  4. Re-evaluate whether Claude is still the right model for Jack's builds — the bundled Codex provider in v2026.4.10 means `codex/gpt-*` models use Codex-managed auth with native threads. Could be a cost-neutral alternative.
- **Effort:** Low (1-2 hours including client call)
- **Research:** Community workarounds are proliferating (Dario proxy, OpenClaude, Cowork bridge). OpenClaw team officially recommends API keys or switching providers. The Cowork bridge is the only fully sub-safe option but it's clunky. API key migration is the cleanest path.

### 2. Upgrade Both Servers: v2026.4.12 → v2026.4.14
- **Intel:** v2026.4.14 (April 14) includes 5 security fixes: ReDoS in markdown parser, Slack allowlist bypass, realpath file restriction bypass, dangerous config.patch flags, and broader SSRF protection. The next pre-release (April 15) adds credential redaction in exec approval prompts.
- **Our exposure:** Both servers (main VPS + Kilmurry) are on v2026.4.12 as of April 14. The realpath file restriction bypass is concerning — it could allow agents to read files outside their workspace. The config.patch flag fix prevents unsafe gateway config mutations. Kate's Telegram bot would also benefit from the topic persistence fix (human-readable names survive restarts).
- **Recommended action:** Upgrade main VPS to v2026.4.14 stable first, verify 24h, then Kilmurry. Don't jump to pre-release on production servers. Command: `npm update -g openclaw && openclaw gateway restart`.
- **Effort:** Low (30 min total, including verification)
- **Research:** Community reports no breakages on v2026.4.14. Releasebot confirms it's a reliability + security focused release. X community sentiment is "upgrade ASAP."

### 3. GA4 Key Rotation — 13 Days Overdue
- **Intel:** Not from today's intel — this is a persistent open item that keeps compounding.
- **Our exposure:** GA4 service account key has been exposed in git history since ~April 3. Key is NOT rotated in Google Cloud. This blocks Kate's GA4 dashboard page (needs service account permissions for property 4940940). Every day this stays open is another day a leaked credential is live. This is also blocking the "Blocked by Jonny" panel items on Mission Control.
- **Recommended action:** This needs to be escalated differently. Jonny has been asked multiple times. Options: (a) Add it as a standing item at the top of every brief until done, (b) Pre-stage the rotation — write a step-by-step with screenshots so Jonny can do it in 3 minutes, (c) If Jonny grants temporary IAM access, an agent could rotate it directly.
- **Effort:** Low (3 minutes for Jonny in Google Cloud Console → IAM → Service Accounts → Keys → Add Key → Delete Old Key)

---

## 🟡 Improve

### 4. Restore Agent Pipeline — OpenAI + xAI Credits Empty
- **Intel:** From our own operational state. Scout (Grok) agent depends on xAI credits. Content (Pixel) agent depends on GPT-5.4/GPT-4o. Hybrid search embeddings need OpenAI.
- **Our exposure:** Half the agent team is non-functional. This morning's Scout scan likely ran on fumes or failed. The intel pipeline that feeds THIS brief is degraded. Content agent can't produce social media assets. Hybrid search upgrade is blocked.
- **Recommended action:**
  1. Top up xAI credits (Scout + x_search — powers our daily intel pipeline).
  2. Top up OpenAI credits (GPT-5.4 for Pixel + embeddings for hybrid search).
  3. Consider setting up Gemini embedding API key as a free fallback for hybrid search (already noted in todo — `searchMode: "search"` → `"query"` config change).
- **Effort:** Low (10 min to top up, 15 min for Gemini embedding fallback config)

---

## 🟢 Opportunities

### 5. Consultancy Play: Anthropic Billing Migration Service
- **Intel:** The Anthropic subscription cut-off is the biggest story in the OpenClaw community right now. Reddit and X are full of confusion, frustration, and half-baked workarounds. Community is fragmented between API keys, extra usage bundles, proxy hacks, and provider switching.
- **Our exposure:** This is pure opportunity. We're living this transition ourselves (Jack's harness). We're about to develop hands-on expertise in the migration path. Every OpenClaw user running Claude is facing this right now.
- **Recommended action:**
  1. Document our Jack migration as a case study (anonymised).
  2. Write a "Claude to API Key Migration Guide for OpenClaw" — position it as consultancy content. Cover: cost modelling (subscription vs. pay-per-token), extra usage bundle math, alternative model options (Codex provider, GPT-5.4, local Gemma 4), and the Cowork bridge for teams that want to keep subs.
  3. Publish on the consultancy site/socials. Lenny's Newsletter coverage + DataCamp tutorials signal mainstream OpenClaw interest is peaking — ride that wave.
  4. Offer a paid "billing migration audit" service: review client's usage, model their new costs, recommend optimal billing path. 1-hour engagement, high value.
- **Effort:** Medium (4-6 hours for guide + case study)
- **Research:** Lenny's Newsletter just published a comprehensive OpenClaw guide (Claire Vo). DataCamp published 9 project templates. The ecosystem is at peak attention — now is the time to publish.

---

## 📋 Summary
- 5 items flagged (3 critical, 1 improvement, 1 opportunity)
- Estimated total implementation effort: ~8-10 hours
- **Priority recommendation:** Jack's ACP harness first — the credit deadline is tomorrow and this is a client-facing issue we architected. Then upgrade servers (30 min, high security ROI). Then top up credits to restore the agent pipeline. GA4 rotation and the consultancy content can follow.
- **Pattern I'm seeing:** We have 4 items that are blocked on Jonny taking a small action (credit top-ups, GA4 rotation, Jack outreach). Consider batching these into a single "15-minute admin block" — top up xAI, top up OpenAI, rotate GA4 key, message Jack about credits. All done in one sitting.
