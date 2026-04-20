# Corrections Log

## 2026-04-05 — Wasted €15 on Opus for bulk WooCommerce membership adds
- **What happened:** Added 11 PAYG students to membership plan #5220 using browser automation — all on Opus at $5/$25 per MTok
- **What I should have done:** Identified the user IDs and plan on Opus, then delegated the repetitive browser work to sitemgr (Wrench, Sonnet at ~$1/$5 per MTok). Or better yet, written a reusable script.
- **Rule going forward:** Any bulk WooCommerce membership work → delegate to sitemgr. Opus does the thinking (plan IDs, user lookups, strategy), Sonnet does the clicking.
- **Estimated waste:** ~€10-12 (task cost €15, should have been €3-5)

## 2026-04-04 — Deployed Nexus from memory instead of following playbook
- Missed ~50% of optimisations. Added mandatory "Client Deployments" rule to AGENTS.md.
- **Rule:** Always open universal-openclaw-implementation.md before deploying anything.

## 2026-04-08 — Locked myself out of a fresh client Linode by hardening SSH too early
- **What happened:** On Aidan's new Linode, I created `clawuser`, enabled UFW/fail2ban, then changed `sshd_config` to disable password auth and root password login before proving a working SSH key path from our machine. Result: remote SSH access was lost.
- **What I should have done:** Preserve access first. On any fresh client server where the only confirmed access is password SSH, the correct order is: create user, install confirmed public key, test a brand-new login successfully, then and only then harden SSH auth settings.
- **Permanent rule going forward:** Never modify `sshd_config`, root login mode, or password authentication on any client machine until a second verified access path exists and has been tested live. If the only known access is password SSH, leave it on until key access is proven. No exceptions.
- **Checklist addition:** Before any SSH hardening, explicitly confirm one of: Linode/Lish console access available, or tested key-based login from our machine, or another verified recovery path.

## 2026-04-20
- **Client doc placement:** Don't create new files in `vault/consultancy/` — use `consultancy/clients/<name>/` for client-specific docs. `vault/` is for internal ops only. Jonny caught duplication of Kilmurry Jack catalogue that already existed.
- **Model scope matters:** `agents.defaults.model` affects EVERYTHING (TUI, bot, non-ACP). Changing global default to fix crons also broke Jack's interactive bot. Use per-cron `--model` flag for cron-only reroutes. Don't change global default unless you specifically want all surfaces to change.
