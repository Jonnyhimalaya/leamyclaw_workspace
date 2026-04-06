# Optimisations & Features Catalogue — Index
**Version:** 1.0 — 2026-04-06

---

## Quick Reference

| Metric | Count |
|--------|-------|
| **Total Entries** | **191** |

### By Category

| Category | Prefix | Count |
|----------|--------|-------|
| Memory | MEM | 19 |
| Cost | CST | 16 |
| Security | SEC | 26 |
| UX | UX | 18 |
| Automation | AUT | 37 |
| Integration | INT | 25 |
| Monitoring | MON | 14 |
| Identity | IDN | 15 |
| Architecture | ARC | 21 |

### By Status

| Status | Count | Meaning |
|--------|-------|---------|
| implemented-ours | 19 | Running on our own Leamy Maths deployment |
| in-playbook | 58 | Documented in universal-openclaw-implementation.md or security-hardening-playbook.md |
| catalogued | 114 | Identified and documented; not yet implemented or playbooked |

### By Complexity

| Complexity | Count | Meaning |
|-----------|-------|---------|
| quick-win (< 1 hour) | 52 | Immediate client value, minimal setup |
| moderate (1-4 hours) | 85 | Standard implementation items |
| major (4+ hours) | 52 | Deep integrations, multi-agent setups, custom builds |
| ongoing | 2 | Continuous processes (skill vetting, consultancy model) |

---

## Files

| File | Description |
|------|-------------|
| [optimisations-catalogue.md](./optimisations-catalogue.md) | Full catalogue with 191 entries across 9 categories |
| [agent-archetypes.md](./agent-archetypes.md) | 8 common agent deployment patterns with recommended catalogue items |

---

## How to Use This Catalogue

### The Workflow: Discovery → Archetype → Essential → Recommended → Customise

The catalogue is designed to accelerate client deployments from discovery to production. Start every engagement with the **New Company AI Assessment Protocol** (from the universal playbook). During discovery, identify the client's primary use case, industry, technical capability, and budget. These four factors determine the deployment scope.

Once discovery is complete, **select an archetype** from [agent-archetypes.md](./agent-archetypes.md) that best matches the client's primary use case. Each archetype lists **essential** catalogue items (the non-negotiable foundation) and **recommended** items (high-value additions). Every client gets the essential items from their archetype plus the universal foundation (Phase 1-4 of the universal playbook). Recommended items are proposed based on budget and priorities — these are the upsell opportunities and the items that differentiate a basic deployment from a transformative one.

After assembling the essential + recommended items, **customise** for the client's specific business. This is where sector modules (hotels, education, services) and business-specific integrations come in. Check each catalogue item's dependencies to ensure prerequisites are in place before attempting implementation. Items marked `in-playbook` have step-by-step instructions in the universal or security playbooks. Items marked `implemented-ours` have been proven on our own deployment and can be replicated with high confidence. Items marked `catalogued` may need evaluation or prototyping before client deployment — factor this into timeline estimates. The catalogue is a living document: update statuses as items are evaluated, implemented, and proven.
