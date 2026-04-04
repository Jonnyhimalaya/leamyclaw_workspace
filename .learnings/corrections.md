# Corrections Log
> Things the user corrected me on. Don't repeat these mistakes.


## 2026-04-03
- **Meta API access is NOT broken.** Jonny set up a developer app with API access token stored in `credentials/.env` (META_ACCESS_TOKEN) and `credentials/meta-api.json`. Mission Control dashboard already works with GA4 + Meta data (confirmed 2026-04-02). The "expired session" issue was from BEFORE this was set up. Don't describe Meta integration as broken again.

## 2026-04-04: Deployed Nexus without following playbook
- **What happened:** Built Nexus from memory, missed ~50% of optimisations (health.sh, SearXNG, HEARTBEAT.md, git init, vault structure, cron jobs, protocols C/D, etc.)
- **Jonny caught it:** He remembered health.sh. I should have caught ALL of them.
- **Root cause:** No structural rule forcing playbook-first deployment. Worked from memory instead of checklist.
- **Fix:** Added mandatory "Client Deployments" section to AGENTS.md. Every deployment must start by opening the playbook. Every deployment must produce a checked-off deployment-checklist.md. Every deployment must score 100% before being called "done."
- **Principle:** Checklists > memory. Always.
