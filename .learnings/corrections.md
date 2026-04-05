# Corrections Log

## 2026-04-05 — Wasted €15 on Opus for bulk WooCommerce membership adds
- **What happened:** Added 11 PAYG students to membership plan #5220 using browser automation — all on Opus at $5/$25 per MTok
- **What I should have done:** Identified the user IDs and plan on Opus, then delegated the repetitive browser work to sitemgr (Wrench, Sonnet at ~$1/$5 per MTok). Or better yet, written a reusable script.
- **Rule going forward:** Any bulk WooCommerce membership work → delegate to sitemgr. Opus does the thinking (plan IDs, user lookups, strategy), Sonnet does the clicking.
- **Estimated waste:** ~€10-12 (task cost €15, should have been €3-5)

## 2026-04-04 — Deployed Nexus from memory instead of following playbook
- Missed ~50% of optimisations. Added mandatory "Client Deployments" rule to AGENTS.md.
- **Rule:** Always open universal-openclaw-implementation.md before deploying anything.
