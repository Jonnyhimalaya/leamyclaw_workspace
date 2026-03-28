# Isolation and Boundaries Model
**Purpose:** Prevent cross-contamination between Leamy Maths, the new consultancy business, and future client deployments.

---

## Core Principle
There are **three layers of separation** we need to maintain:

1. **Business separation**
   - Leamy Maths and the consultancy are distinct businesses
2. **Client separation**
   - each consultancy client must be isolated from every other client
3. **Operational separation**
   - memory, tasks, credentials, and agents should not bleed across contexts

---

## The Separation Rule
### Leamy Maths
- remains its own operating environment
- its agents, memory, credentials, and workflows stay specific to that business

### Consultancy business
- should become its **own workspace / own agent team / own memory layer**
- this is where playbooks, templates, research bank, and client pipeline should live
- consultancy intelligence should not be mixed into Leamy Maths operational memory long-term

### Client deployments
- each client gets their **own server / own gateway / own agent team / own data**
- never run multiple client businesses inside one shared client environment

---

## Practical Architecture

## Layer 1 — Jonny Personal / Leamy Maths
Current system:
- personal orchestrator
- Leamy Maths specialist agents
- Leamy Maths memory
- Leamy Maths credentials

## Layer 2 — Consultancy HQ
New system to build:
- consultancy orchestrator
- consultancy scout/research agent
- consultancy content / proposal / architecture helpers
- consultancy memory + research bank
- NO client production data stored here except discovery notes and design docs

## Layer 3 — Client Production Environments
Per client:
- dedicated Linode/VPS
- dedicated OpenClaw gateway
- dedicated Mission Control
- dedicated credentials
- dedicated memory
- dedicated agent team

---

## What should live in Consultancy HQ
Safe to store here:
- playbooks
- design frameworks
- opportunity libraries
- proposal templates
- client discovery notes
- architecture recommendations
- reusable SOPs
- anonymised lessons learned

Should NOT live here:
- production client credentials
- live client operational memory
- client PII beyond what is required for project management
- sensitive internal client data

---

## What should live in each client environment
- live operational memory
- client credentials
- client workflows
- client reports
- client artifacts
- client messaging / automation channels
- client business rules

---

## Recommended Future Workspace Structure

### Option A — Good enough short term
Continue using current workspace, but keep consultancy under:
- `consultancy/`

Only acceptable short-term while the business is very new.

### Option B — Better
Create a separate workspace:
- `~/.openclaw/workspace-consultancy/`

With its own:
- AGENTS.md
- SOUL.md
- USER.md
- MEMORY.md
- memory/
- consultancy-specific agents

This is the recommended next step once consultancy work becomes regular.

---

## Agent Separation Rules

### Leamy Maths agents
Should stay focused on:
- Leamy Maths operations
- education workflows
- existing business tasks

### Consultancy agents
Should focus on:
- research
- playbook creation
- client discovery support
- architecture design
- proposal generation
- security/cost/design standards

### Client agents
Should only know:
- that specific client's workflows
- that specific client's tools
- that specific client's memory and data

---

## Memory Separation Rules

### Consultancy memory should store
- business development for the consultancy
- client pipeline info
- design methodology
- framework evolution
- reusable patterns

### Consultancy memory should NOT become
- a dumping ground for live Leamy Maths operations
- a dumping ground for client production details

### Long-term principle
Reusable lessons get abstracted upward.
Client specifics stay local.

---

## Credential Separation Rules
Never reuse one credential store for multiple businesses if avoidable.

Recommended structure:
- consultancy HQ credentials
- client-specific credentials per deployment
- no shared passwords across client systems
- each client controls or can reclaim their credentials

---

## Messaging Separation Rules
- client-facing channels must belong to that client environment
- never send client operational messages from the wrong environment
- proposals/research can be handled from consultancy HQ
- production automations should always run from the client's own stack

---

## Security Boundary Checklist
Before a system is considered production-ready, confirm:
- [ ] separate server/VPS
- [ ] separate gateway
- [ ] separate credentials
- [ ] separate memory store
- [ ] separate messaging channels
- [ ] separate logs/artifacts
- [ ] clear approval model
- [ ] limited tool permissions per agent

---

## The Rule of Abstraction
If something is:
- **specific to a client** → keep it in the client environment
- **specific to Leamy Maths** → keep it in Leamy Maths
- **reusable across businesses** → move it into consultancy frameworks/playbooks

This is the cleanest way to avoid contamination while still learning from each engagement.

---

## Summary
The correct model is:
- Leamy Maths = one operating environment
- Consultancy HQ = one separate design/research environment
- Each client = one dedicated production environment

That gives us:
- privacy
- professionalism
- scalability
- lower contamination risk
- cleaner memory and agent roles
