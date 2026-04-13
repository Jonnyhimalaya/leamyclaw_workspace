# AI Consultancy Business

## Overview (Started Mar 28, 2026)
- Jonny launching second business: helping SMEs set up OpenClaw agentic systems
- Separate from Leamy Maths — own branding, own client relationships
- Architecture: separate Linode + gateway per client (full data isolation)
- Business model: setup fee + monthly retainer + pass-through infrastructure costs

## Vision (Mar 30)
- Portfolio model — each client teaches patterns that improve next onboarding
- Architecture schematics = standard deliverable per client
- Mission Control `/consultancy/clients` = portfolio dashboard
- Industry-specific templates compound over time (hospitality first via Kilmurry)
- Compounding expertise is the moat

## First Client: Kilmurry Lodge Hotel
- 109 rooms, Castletroy, Limerick — GM (Jack Hoare) is Jonny's friend
- Server: 172.239.98.61
- Kilmurry has evolved from a standard single-client deployment into both:
  - a live multi-surface OpenClaw deployment
  - a consultancy pattern lab for hospitality operations, intelligence products, and department dashboards
- The most current operational state should be tracked in `memory/topics/client-deployments-status.md` rather than spread across redundant docs
- Reusable Kilmurry patterns should be folded into existing playbooks/frameworks when proven, not parked in lots of separate one-off notes
- High-value reusable patterns already emerging:
  - department-module architecture
  - intelligence layer on top of existing business systems
  - human-in-the-loop review queues
  - correction-to-memory training flows
  - morning brief as a daily intelligence product
- See: `consultancy/clients/kilmurry-lodge/` for client-specific artefacts still worth keeping

## Workspace
- Playbooks: `consultancy/playbooks/` (universal, hotels, education, service-businesses)
- Frameworks: `consultancy/frameworks/` (agentic design, isolation, security)
- Templates: `consultancy/templates/` (audit worksheets, scoring sheets)
- Protocols: `consultancy/protocols/` (new company assessment)

## Key Principles
- Never accept credentials in chat
- Human logs in on server browser, agent uses session cookie
- Start with observation/drafting before automation
