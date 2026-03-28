# Security, Data Protection, Cost Control, and Optimisation Framework
**Purpose:** Standard guidance for designing consultancy-grade agentic systems responsibly.

---

# 1. Security Principles

## Principle 1 — Least privilege
Every agent should have the minimum tools and permissions needed.

Examples:
- review monitor should not have payment access
- content agent should not have site admin rights unless needed
- scout should not be able to send guest-facing messages

## Principle 2 — Approval before high-risk writes
High-risk actions should be gated:
- pricing changes
- refunds
- financial actions
- destructive edits
- sensitive customer replies
- permission/config changes

## Principle 3 — Client isolation
Each client should run on:
- separate VPS/server
- separate gateway
- separate memory
- separate credentials
- separate messaging surface

## Principle 4 — Observe first
Start new systems with:
- monitoring
- drafting
- summaries
- recommendations
before enabling action-taking

## Principle 5 — Auditability
For important actions, keep:
- artifacts
- logs
- reports
- before/after snapshots
- clear operator visibility

---

# 2. Data Protection Principles

## What to minimise
Collect/store only what is operationally necessary.

Avoid unnecessary storage of:
- sensitive customer data
- payment data
- legal/medical details unless explicitly required
- broad exports of client systems when smaller scoped data is enough

## What to segregate
Keep separate:
- consultancy research data
- client design docs
- client production data
- credentials
- logs containing personal data

## What to document
For each client system, define:
- what data the agents can access
- what is written to memory
- what is retained in artifacts/logs
- what must never be stored long-term
- who can access dashboards and reports

## Practical rule
If a workflow can succeed with metadata + summaries instead of raw sensitive data, prefer that.

---

# 3. Cost Control Principles

## Cost sources in agentic systems
- model/API usage
- server/VPS cost
- storage/log growth
- browser automation overhead
- monitoring services
- engineering maintenance time

## Main cost mistakes to avoid
- too many agents with overlapping roles
- loading too much context into every task
- spawning agents for trivial work
- no caching/reuse of research or decisions
- no budget awareness
- using top-tier models for low-value repetitive tasks

## Good cost discipline
- one orchestrator, few specialists
- narrow agent scopes
- files for durable context, not repeated long prompts
- route simple tasks to cheaper/faster models
- reserve best models for orchestration, difficult reasoning, sensitive design work
- artifact to disk, don't reload unless needed

---

# 4. Optimisation Principles

## Context optimisation
- keep agents narrow
- externalise memory into files
- avoid shared giant prompts
- use runbooks/templates instead of re-explaining workflows each time

## Workflow optimisation
- prefer one weekly workflow over many ad-hoc manual interventions
- automate recurring summaries
- add artifacts only at job level, not microtask level
- design reusable patterns per industry

## Operational optimisation
- start with one pilot that proves value
- standardise templates and playbooks
- reduce custom work by reusing patterns
- keep infrastructure simple until complexity is justified

---

# 5. Model Selection Heuristic

## Use the strongest models for:
- orchestration
- architecture/design work
- nuanced customer communication drafts
- difficult research synthesis
- proposal / strategy work

## Use cheaper/faster models for:
- routine summaries
- structured extraction
- content classification
- repetitive drafts
- low-risk internal reporting

## Rule
Match model cost to task value and risk.

---

# 6. Client Cost Model
For each client, separate:

## A. Infrastructure cost
- VPS/server
- domain/SSL
- storage
- monitoring

## B. Model/API cost
- Anthropic / OpenAI / xAI / Google etc.

## C. Consultancy fee
- setup
- design
- deployment
- maintenance
- optimisation

This makes the economics transparent.

---

# 7. Security and Risk Matrix

## Low-risk workflows
Good early automation candidates:
- summaries
- monitoring
- reports
- internal notifications
- draft responses
- non-destructive content suggestions

## Medium-risk workflows
Need approval or guardrails:
- guest/customer communication
- ad changes
- website edits
- release scheduling
- task routing

## High-risk workflows
Avoid early or keep tightly gated:
- payments
- refunds
- pricing changes in production systems
- contracts/legal commitments
- deleting records
- permission/config changes

---

# 8. Minimum Production Standards for Client Systems
Before going live, confirm:
- [ ] separate environment
- [ ] credentials stored safely
- [ ] clear approval matrix
- [ ] narrow agent scopes
- [ ] daily/long-term memory defined
- [ ] artifacts/logging in place
- [ ] human escalation path defined
- [ ] cost model estimated
- [ ] pilot workflow chosen and bounded
- [ ] failure modes considered

---

# 9. Design Rule for Consultancy Quality
A bespoke system is high quality if it is:
- secure enough to trust
- cheap enough to justify
- useful enough to keep
- observable enough to verify
- narrow enough to stay reliable
- extensible enough to grow later

---

# Summary
The best consultancy-grade agentic systems are not the most autonomous ones.
They are the ones with the best:
- boundaries
- controls
- memory discipline
- cost discipline
- risk awareness
- operational fit
