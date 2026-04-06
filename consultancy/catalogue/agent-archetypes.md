# Agent Archetypes
**Version:** 1.0 — 2026-04-06
**Purpose:** Common agent deployment patterns mapped to catalogue items. Use during client discovery to quickly assemble a tailored deployment.

---

## 1. Personal Executive Assistant

**Description:** A 24/7 personal aide that manages email, calendar, tasks, and information. Runs proactively (morning briefings, end-of-day reviews) and reactively (answer questions, research, draft communications). The single most common OpenClaw deployment pattern.

**Essential Catalogue Items:**
- MEM-001 Three-Tier Memory Architecture
- MEM-002 MEMORY.md as Pointer Index
- MEM-003 Workspace File Size Budget
- MEM-008 Protocol A — Search-First
- MEM-009 Protocol C — Periodic Checkpoints
- MEM-011 autoDream Nightly Consolidation
- IDN-001 SOUL.md Personality Configuration
- IDN-002 USER.md
- IDN-003 IDENTITY.md
- SEC-001 Gateway Authentication
- SEC-010 Channel allowFrom
- AUT-001 Morning Briefing Cron
- MON-001 Server Health Script
- ARC-001 systemd Gateway Service

**Recommended Catalogue Items:**
- UX-002 Anti-Sycophancy Rule
- UX-003 Anti-Echo-Chamber Mandate
- UX-013 Autonomy Levels
- AUT-002 End-of-Day Review
- AUT-005 Inbox Triage Cron
- AUT-007 Cost Review Cron
- INT-003 Email Integration
- INT-005 Calendar Integration
- UX-011 Voice Integration (ElevenLabs + Twilio)
- MEM-004 QMD Memory Backend
- CST-004 Sub-Agent Model Tiering

**Typical Model:** Claude Sonnet 4.6 (daily), Opus for weekly deep analysis
**Typical Channel:** Telegram (primary), WhatsApp (family comms)

**Example Deployments:**
- Nat Eliason's "Felix" — autonomous business builder ($14,718 in 3 weeks)
- TechNickAI's openclaw-config — 14 skills, 6 workflows, 3-tier memory
- Ryan Carson's ClawChief — Chief of Staff pattern with priority map
- Agency manager running 4 Slack workspaces through one agent

---

## 2. Customer Service Bot

**Description:** A multi-channel customer-facing agent handling FAQs, booking/reservation management, review responses, and inquiry qualification. Designed for minimum risk (no exec, workspace-only filesystem) with human escalation for complex issues. Runs 24/7 with sub-2-minute response times.

**Essential Catalogue Items:**
- SEC-001 Gateway Authentication
- SEC-010 Channel allowFrom
- SEC-012 Workspace-Only Filesystem
- SEC-013 exec: deny for Customer-Facing Agents
- IDN-001 SOUL.md Personality Configuration
- IDN-003 IDENTITY.md
- IDN-012 Context-Specific SOUL.md (Customer-Facing)
- INT-006 WhatsApp Business API
- INT-024 Multi-Language Detection
- AUT-013 WhatsApp Reservation/Booking Handler
- AUT-014 Appointment Reminder Automation
- MON-001 Server Health Script
- ARC-001 systemd Gateway Service

**Recommended Catalogue Items:**
- AUT-012 Google Review Auto-Response
- AUT-015 No-Show Follow-Up
- AUT-019 Lead Qualification Bot
- AUT-030 Parent/Customer Nudges
- AUT-036 Inactive Client Recovery
- INT-019 Google Business Profile API
- INT-020 Instagram Graph API
- UX-015 Telegram Streaming
- SEC-015 Plugin Tool Approval Hooks
- SEC-014 Two-Way Door Principle

**Typical Model:** Claude Sonnet 4.6 (best balance of quality and cost for customer-facing)
**Typical Channel:** WhatsApp Business (primary), Instagram DMs, Telegram (owner ops)

**Example Deployments:**
- Multi-channel restaurant AI: response time from 4+ hours to <2 minutes, 80% auto-handled
- Dental clinic AI: 50% no-show reduction, 40 calls/day automated
- Futurist Systems: multi-channel customer service for local businesses
- Wazzy.io pattern: WhatsApp AI for clinics and salons

---

## 3. Operations Agent (Internal Ops)

**Description:** An internal operations agent that monitors systems, manages team workflows, coordinates multi-agent tasks, and produces operational reports. Not customer-facing — optimised for directness, speed, and proactive problem detection. Often the orchestrator in multi-agent setups.

**Essential Catalogue Items:**
- MEM-001 Three-Tier Memory Architecture
- MEM-002 MEMORY.md as Pointer Index
- MEM-004 QMD Memory Backend
- MEM-019 NDD Structured Logging
- UX-005 AGENTS.md as Decision Tree
- UX-013 Autonomy Levels
- AUT-001 Morning Briefing Cron
- AUT-008 Advisor Model Cron
- AUT-009 Intel Sweep Cron
- MON-001 Server Health Script
- MON-003 Session Size Monitoring
- MON-010 Cost Review & Spend Tracking
- SEC-001 Gateway Authentication
- ARC-001 systemd Gateway Service

**Recommended Catalogue Items:**
- ARC-006 Multi-Agent Team Architecture
- ARC-010 Sequential Filesystem Handoff
- CST-001 Model Routing Layer
- CST-004 Sub-Agent Model Tiering
- AUT-003 Competitor Monitoring
- AUT-004 Weekly Deep Analysis
- MON-006 Git Backup
- MON-007 Post-Update Verification
- SEC-019 Append-Only Audit Logs
- INT-001 OpenClaw + n8n

**Typical Model:** Claude Opus 4.6 (orchestrator), Sonnet (sub-agents), Grok-mini (intel)
**Typical Channel:** Telegram (owner DMs), Discord (team ops channels)

**Example Deployments:**
- 10-agent "Mission Control" with shared Convex DB, 15-minute heartbeats
- 8 specialised agents running 50+ cron jobs (ScottSparkwave)
- Leamy Maths multi-agent setup: Opus orchestrator, Sonnet site manager, Grok scout
- BretJutras COO agent managing 4-agent content/marketing team

---

## 4. Content Factory

**Description:** A content generation pipeline producing social media posts, blog articles, email newsletters, podcast assets, and video content. Often runs as a multi-agent system with a research agent, writing agent, and design agent working in sequence or parallel.

**Essential Catalogue Items:**
- IDN-001 SOUL.md Personality Configuration
- UX-007 DESIGN.md Markdown Design System
- ARC-010 Sequential Filesystem Handoff
- ARC-012 Review Loop Pattern (Draft → Critique → Revise)
- AUT-018 Daily Specials Broadcaster
- MEM-001 Three-Tier Memory Architecture
- SEC-001 Gateway Authentication
- MON-001 Server Health Script
- ARC-001 systemd Gateway Service

**Recommended Catalogue Items:**
- AUT-025 TikTok Marketing Pipeline
- AUT-026 Podcast Production Pipeline
- AUT-027 Video Editing via Natural Language
- UX-012 OpenAI Whisper Local STT
- INT-020 Instagram Graph API
- ARC-011 Fan-Out Parallel Agent Pattern
- CST-005 Batch Processing (50% Discount)
- CST-004 Sub-Agent Model Tiering
- IDN-006 Agent Naming as Business Strategy

**Typical Model:** Sonnet 4.6 (content generation), Opus (editorial review), Haiku (formatting/scheduling)
**Typical Channel:** Discord (multi-channel content pipeline — #research, #drafts, #design)

**Example Deployments:**
- Multi-platform content manager: 4 X accounts, LinkedIn, YouTube Shorts on Mac Mini
- Discord Content Factory: research → drafts → design pipeline
- Indonesian AI news portal via WhatsApp automation
- TikTok marketing pipeline: 1.2M views/week, $670/mo MRR

---

## 5. Sales & Outreach Agent

**Description:** A sales agent that handles lead discovery, qualification, outreach, follow-up, and CRM management. Runs pipeline stages from initial contact through to booked demo or closed deal. Often integrates with LinkedIn, email, and CRM systems.

**Essential Catalogue Items:**
- SEC-001 Gateway Authentication
- SEC-010 Channel allowFrom
- SEC-014 Two-Way Door Principle
- IDN-001 SOUL.md Personality Configuration
- IDN-003 IDENTITY.md
- AUT-019 Lead Qualification Bot
- AUT-016 Quote Follow-Up Automation
- AUT-017 Invoice Payment Reminders
- INT-002 CRM Integrations
- INT-003 Email Integration
- MON-001 Server Health Script
- ARC-001 systemd Gateway Service

**Recommended Catalogue Items:**
- AUT-023 LinkedIn Prospecting (BeReach)
- AUT-024 24/7 Sales Outreach
- AUT-034 Automated Bidding Workflow
- AUT-035 CRM Migration
- INT-025 Vibe-Coded Lead Gen Tool
- INT-001 OpenClaw + n8n
- INT-016 DenchClaw Local CRM
- CST-004 Sub-Agent Model Tiering
- MEM-012 Vault for Sensitive Data

**Typical Model:** Claude Sonnet 4.6 (outreach), Grok-mini (lead research)
**Typical Channel:** WhatsApp (client-facing), Telegram (internal), Email (outreach)

**Example Deployments:**
- Lead capture at scale: CRM + LinkedIn + HunterIO + BrightData pipeline
- 24/7 sales team: data prep → research → email writing → sending → flagging
- Automated bidding: bid → review → vendors → costs → margins
- CRM migration: 1,500 contacts + 200 proposals between CRMs

---

## 6. Dev/Ops Agent

**Description:** A development and infrastructure agent that manages code repos, reviews PRs, deploys applications, monitors servers, and orchestrates coding agents (Codex, Claude Code, Gemini CLI) via ACP. Often the most technical deployment with full exec access.

**Essential Catalogue Items:**
- SEC-001 Gateway Authentication
- SEC-023 exec-approvals.json
- SEC-026 Exec Security Allowlist
- MEM-001 Three-Tier Memory Architecture
- MEM-004 QMD Memory Backend
- ARC-001 systemd Gateway Service
- ARC-004 Auth Profile Rotation
- ARC-005 SearXNG Self-Hosted Search
- INT-012 ACP/ACPX Agent Orchestration
- INT-017 GitHub/Vercel/Netlify Dev Integration
- MON-001 Server Health Script
- MON-007 Post-Update Verification

**Recommended Catalogue Items:**
- ARC-016 Self-Healing Home Server
- ARC-017 Self-Hosted Git (Gitea)
- AUT-011 Client Website Management via Chat
- AUT-029 n8n Workflow Generation via Chat
- INT-001 OpenClaw + n8n
- INT-021 Todoist/Jira/Linear Task Management
- CST-006 Local Models (Ollama/LM Studio)
- CST-016 Claude Code Subscription
- UX-006 ARCHITECTURE.md for Model Choices
- ARC-008 STATE.yaml Autonomous Project Management

**Typical Model:** Claude Opus 4.6 (coding), Sonnet (routine tasks), local models (zero-cost)
**Typical Channel:** Slack (team), Discord (multi-agent), Telegram (personal)

**Example Deployments:**
- Fully automated software dev team: Slack → agents → Jira → TDD → merge
- Game dev DevOps: asset management, log debugging, Kubernetes on Slack
- Client website management via Telegram voice messages
- Agent-run SaaS: 5 paid customers at ~$550/month MRR

---

## 7. Industry Specialist (Hospitality, Legal, Healthcare, etc.)

**Description:** A vertically-specialised agent with deep domain knowledge for a specific industry. Combines customer-facing and ops capabilities with industry-specific workflows, compliance requirements, and terminology. Each vertical has distinct needs.

**Essential Catalogue Items:**
- All Customer Service Bot essentials (see archetype #2)
- MEM-012 Vault for Sensitive Data
- SEC-019 Append-Only Audit Logs (for regulated industries)
- IDN-014 Daimon Legal Identity Pattern
- AUT-014 Appointment Reminder Automation
- AUT-012 Google Review Auto-Response
- ARC-003 Layered Playbook Architecture
- ARC-002 Dedicated VPS Per Client

**Recommended Catalogue Items:**

*Hospitality:*
- AUT-028 Review Response Pipeline
- AUT-031 Competitive Intel Sweep
- AUT-013 WhatsApp Reservation Handler
- UX-011 Voice Integration (dinner reservations)
- ARC-010 Sequential Filesystem Handoff

*Legal:*
- SEC-018 NemoClaw Enterprise Security
- AUT-020 Document Collection Chaser
- IDN-014 Daimon Legal Identity Pattern
- AUT-021 Email Triage

*Healthcare:*
- INT-010 FHIR/Epic Health Data
- INT-011 Apple Health/Garmin
- SEC-012 Workspace-Only Filesystem
- AUT-014 Appointment Reminders (50% no-show reduction)

**Typical Model:** Claude Sonnet 4.6 (customer-facing), Opus (legal analysis, compliance review)
**Typical Channel:** WhatsApp (customer/patient/guest), Telegram (owner/staff ops)

**Example Deployments:**
- Daimon Legal: 24/7 law firm deployment with legislative review and vendor workflows
- Dental clinic: 50% no-show reduction, 40 calls/day handled
- Airbnb guest management: guest messaging, FAQ, review management
- Hotel morning briefing pipeline: reviews + weather + events + occupancy

---

## 8. Research & Intelligence Agent

**Description:** A research-focused agent that monitors sources, analyses trends, and synthesises intelligence reports. Often runs as a scout in a multi-agent setup, gathering data that other agents process. Particularly strong for competitive intelligence, market research, and ecosystem monitoring.

**Essential Catalogue Items:**
- ARC-005 SearXNG Self-Hosted Search
- AUT-009 Intel Sweep Cron
- AUT-003 Competitor Monitoring
- ARC-010 Sequential Filesystem Handoff
- MEM-001 Three-Tier Memory Architecture
- MEM-004 QMD Memory Backend
- IDN-001 SOUL.md Personality Configuration
- SEC-001 Gateway Authentication
- MON-001 Server Health Script
- ARC-001 systemd Gateway Service

**Recommended Catalogue Items:**
- ARC-011 Fan-Out Parallel Agent Pattern
- AUT-004 Weekly Deep Analysis
- AUT-006 Reddit/YouTube Digest
- AUT-031 Competitive Intel Sweep (Multi-Agent)
- MEM-006 Cognee Knowledge Graph Memory
- MEM-015 ByteRover Portable Memory Layer
- CST-004 Sub-Agent Model Tiering
- UX-008 /btw Side Conversations
- INT-001 OpenClaw + n8n

**Typical Model:** Grok-mini (fast X/Twitter search), Sonnet (synthesis), Opus (deep weekly analysis)
**Typical Channel:** Telegram (report delivery), Discord (research pipeline channels)

**Example Deployments:**
- Leamy Maths intel sweep: Scout (Grok, 40s) → Main (Sonnet, 118s) = ~$0.053/day
- Product Decision Intelligence across 29 retail stores, 40TB data
- Options flow analysis: 6 months institutional data → SQLite + vector → NL queries
- MiroFish: 2,200 agents self-improving across 750K simulations
