# Optimisations & Features Catalogue
**Version:** 1.0 — 2026-04-06
**Source files:** power-user-patterns, community-use-cases, llm-cost-routing-2026-04, easy-wins-by-industry, ecosystem-state-march2026, universal-openclaw-implementation, security-hardening-playbook, multi-agent-coordination-playbook, claude-code-channels-competitive-analysis, twitter-research-2026-04-05

---

## Summary Table

### Counts by Category

| Category | Prefix | Count |
|----------|--------|-------|
| Memory | MEM | 19 |
| Cost | CST | 19 |
| Security | SEC | 26 |
| UX | UX | 20 |
| Automation | AUT | 37 |
| Integration | INT | 25 |
| Monitoring | MON | 15 |
| Identity | IDN | 18 |
| Architecture | ARC | 21 |
| Marketing | MKT | 3 |
| Memory | MEM | 2 |
| **TOTAL** | | **211** |

### Counts by Status

| Status | Count |
|--------|-------|
| implemented-ours | 19 |
| in-playbook | 58 |
| catalogued | 129 |

### Counts by Complexity

| Complexity | Count |
|-----------|-------|
| quick-win (< 1 hour) | 52 |
| moderate (1-4 hours) | 85 |
| major (4+ hours) | 52 |
| ongoing | 2 |

---

## MEMORY

---

### [MEM-001] Three-Tier Memory Architecture
- **Category:** memory
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md (TechNickAI/OnlyTerp), universal-openclaw-implementation.md
- **Description:** Organise memory into three tiers: MEMORY.md (always-loaded index, <3KB), daily files `memory/YYYY-MM-DD.md` (recent logs), and `vault/` (deep structured knowledge accessed via search). Each tier has a different access pattern and cost profile.
- **Value Proposition:** Keeps injected context lean (cheaper, faster responses) while retaining unlimited long-term knowledge accessible in ~45ms via search.
- **Implementation Notes:** Restructure any existing MEMORY.md into a pointer index. Move all detailed knowledge to `vault/` subdirectories. Configure QMD to search vault as an extra path.
- **Dependencies:** QMD or other memory backend for vault search; vault directory structure.

---

### [MEM-002] MEMORY.md as Pointer Index
- **Category:** memory
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 2.2), power-user-patterns.md
- **Description:** MEMORY.md should contain only brief pointers to vault files, not full content. Example: "Revenue data → vault/financial/revenue.md" rather than the actual figures. Detailed knowledge lives in vault files and is loaded on demand.
- **Value Proposition:** Leamy deployment reduced MEMORY.md from 13KB to 2KB (86% reduction) with zero information loss. Every message becomes cheaper and faster.
- **Implementation Notes:** Target <3KB for MEMORY.md. Keep: key facts (2-3 lines), active project pointers, key people pointers, known issues (brief), preferences (brief). Move everything else to vault.
- **Dependencies:** vault/ directory structure; memory search backend.

---

### [MEM-003] Workspace File Size Budget (<8KB Total)
- **Category:** memory
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md (OnlyTerp), universal-openclaw-implementation.md
- **Description:** Every byte in SOUL.md, AGENTS.md, MEMORY.md, and TOOLS.md is injected into every single message. Target total under 8KB: SOUL.md <1KB, AGENTS.md <3KB, MEMORY.md <3KB, TOOLS.md <1KB.
- **Value Proposition:** OnlyTerp reports going from 15-20KB context per message to 4-5KB, cutting response time from 4-8s to 1-2s and token cost from ~5,000 to ~1,500 tokens per message.
- **Implementation Notes:** Audit current file sizes with `wc -c SOUL.md AGENTS.md MEMORY.md TOOLS.md`. Aggressively prune anything that doesn't need to be in every message.
- **Dependencies:** vault/ for offloaded content; QMD for retrieval.

---

### [MEM-004] QMD Memory Backend (Hybrid Retrieval)
- **Category:** memory
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 2.2 QMD section), power-user-patterns.md
- **Description:** QMD is a memory backend that provides BM25 keyword search (free, no API) or hybrid BM25+vector+reranking with temporal decay. Install via `bun install -g @tobilu/qmd`, configure in openclaw.json with `memory.backend: "qmd"` and vault as an extra search path.
- **Value Proposition:** Eliminates external API dependency for memory search. BM25 mode is free; hybrid mode costs ~$0.01/day. Dramatically improves recall accuracy over raw file scanning.
- **Implementation Notes:** Start with `searchMode: "search"` (BM25, free). Upgrade to `searchMode: "query"` (hybrid) only when vault grows large (50+ files) or semantic matching is needed. Requires unzip + bun first. Add `extraPaths: ["vault"]` so vault files are searchable.
- **Dependencies:** Bun runtime; unzip package; optional: OpenAI or Gemini API key for hybrid mode.

---

### [MEM-005] ClawVault Typed Memory System
- **Category:** memory
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | ops-agent | dev-ops
- **Status:** catalogued
- **Source:** power-user-patterns.md (Versatly/clawvault on GitHub)
- **Description:** Typed memory entries (fact, decision, lesson, commitment, preference, relationship, project) with auto-recall and auto-capture. Session commands: `clawvault wake`, `clawvault checkpoint`, `clawvault sleep "summary"`. Includes context death detection on startup.
- **Value Proposition:** Reduces memory recall overhead from ~5,000 tokens to ~200 tokens. Auto-capture observes conversations and stores durable knowledge automatically without manual prompting.
- **Implementation Notes:** Install from Versatly/clawvault on GitHub. Configure auto-recall to inject relevant memories before each turn; enable auto-capture for passive knowledge extraction.
- **Dependencies:** OpenClaw gateway; compatible memory backend.

---

### [MEM-006] Cognee Knowledge Graph Memory
- **Category:** memory
- **Complexity:** major (4+ hours)
- **Use Case Tags:** research-agent | ops-agent | dev-ops
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Cognee provides knowledge-graph-based memory that understands relationships between entities, not just semantic similarity. Rather than retrieving similar text chunks, it maps connections between people, projects, decisions, and concepts.
- **Value Proposition:** Superior for complex deployments where relationships matter — law firm clients, enterprise ops, research agents. Understands that "Alice manages the X project which depends on Y contract" rather than just finding files mentioning "Alice".
- **Implementation Notes:** Install and configure Cognee as a memory backend. Requires more setup than QMD but provides richer structured recall for complex knowledge graphs.
- **Dependencies:** Cognee installation; graph database backend.

---

### [MEM-007] Mem0 Automatic Fact Extraction
- **Category:** memory
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | customer-service
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Mem0 automatically extracts and stores facts from conversations in long-term memory. Available in cloud and self-hosted modes. Passively observes conversations and identifies durable knowledge without requiring explicit memory commands.
- **Value Proposition:** Zero-effort memory building — the agent gets smarter over time without requiring users to explicitly say "remember this."
- **Implementation Notes:** Self-hosted mode preferred for privacy. Configure as memory backend; Mem0 intercepts conversation flow and extracts facts. Cloud mode is faster to set up.
- **Dependencies:** Mem0 installation (cloud account or self-hosted instance).

---

### [MEM-008] Protocol A — Search-First, Write-Last
- **Category:** memory
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 2.2 Memory Protocols)
- **Description:** AGENTS.md protocol requiring the agent to call `memory_search` before answering any question about past facts, decisions, or preferences. After every meaningful exchange, the agent evaluates whether the information needs to survive the next session.
- **Value Proposition:** Eliminates "the agent forgot" failures. Without this protocol, agents confidently guess rather than checking their notes.
- **Implementation Notes:** Add Protocol A verbatim to AGENTS.md. Key rule: "BEFORE answering any question about past facts, call memory_search — never rely solely on conversation history."
- **Dependencies:** QMD or other memory backend configured.

---

### [MEM-009] Protocol C — Periodic Memory Checkpoints
- **Category:** memory
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 2.2 Protocol C), incident: Session Freeze 2 Apr 2026
- **Description:** Every ~150 messages, flush all unsaved events to `memory/YYYY-MM-DD.md`. Track last checkpoint in `heartbeat-state.json`. Prevents catastrophic context loss when sessions die unexpectedly under API pressure.
- **Value Proposition:** On 2 Apr 2026, a Telegram session hit 516 messages, froze on 429 errors, required /new, and lost the entire exec-access-loss event from memory. Checkpoints prevent this loss.
- **Implementation Notes:** Add checkpoint counter to `heartbeat-state.json`. At message counts 150, 300, 450, write checkpoint with marker `### Memory Checkpoint — HH:MM UTC (msg ~N)`.
- **Dependencies:** heartbeat-state.json; daily memory file.

---

### [MEM-010] Protocol D — Post-/new Transcript Rescan
- **Category:** memory
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 2.2 Protocol D)
- **Description:** On every new session startup, check for `.reset` archives from today/yesterday, extract user messages and assistant actions, compare against today's memory file, and append missing events with `[RECOVERED]` tag.
- **Value Proposition:** Safety net for Protocol C failures. Even if checkpoints were missed, the transcript is always recoverable from the `.reset` archive.
- **Implementation Notes:** Add to session startup sequence: `ls -t ~/.openclaw/agents/main/sessions/*.reset.* | head -3`. If found from today/yesterday, scan and recover missing events.
- **Dependencies:** Protocol C (MEM-009); access to session archive files.

---

### [MEM-011] autoDream — Nightly Memory Consolidation
- **Category:** memory
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 3.5.4)
- **Description:** A nightly cron job (2am local time) that reads today's daily log, distils key decisions/lessons/facts into MEMORY.md, archives daily logs older than 7 days to `memory/archive/`, and trims MEMORY.md if it's getting bloated.
- **Value Proposition:** MEMORY.md stays lean automatically. Important context survives beyond daily logs. Self-healing memory — the agent gets smarter over time without manual curation.
- **Implementation Notes:** `openclaw cron add --cron "0 2 * * *" --model "anthropic/claude-sonnet-4-6" --session isolated --timeout-seconds 300 --message "DREAM CYCLE: [see playbook prompt]"`. Create `memory/archive/` directory first.
- **Dependencies:** Daily memory files; MEMORY.md; `memory/archive/` directory.

---

### [MEM-012] Vault Directory Structure for Sensitive Data
- **Category:** memory
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** finance | ops-agent | customer-service
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 3), universal-openclaw-implementation.md
- **Description:** Segregate sensitive data into isolated vault subdirectories: `vault/financial/`, `vault/customers/`. Apply restrictive file permissions (700 for directories, 600 for files). MEMORY.md references but never contains raw financial/PII data.
- **Value Proposition:** Sensitive data only enters context when explicitly needed via memory search. MEMORY.md is injected into every message — if it contains revenue figures, those figures leak into every API call.
- **Implementation Notes:** `chmod 700 vault/financial/ vault/customers/`, `chmod 600 vault/financial/*`. Add SOUL.md directives: "Never put raw financial data in MEMORY.md or daily logs — use references."
- **Dependencies:** vault/ directory structure; SOUL.md and AGENTS.md data security directives.

---

### [MEM-013] Memory Criteria Filter (4-Question Test)
- **Category:** memory
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md (TechNickAI)
- **Description:** Before storing any information, apply four filters: Durability (will this matter in 30+ days?), Uniqueness (is this new?), Retrievability (will I want to recall this?), Authority (is this reliable?). Only items passing all four get stored to long-term memory.
- **Value Proposition:** Prevents memory pollution with trivial information. Keeps vault/MEMORY.md focused on genuinely useful long-term knowledge.
- **Implementation Notes:** Add the four-question filter to AGENTS.md memory protocols. Agent applies it before any `edit` or `write` to memory files.
- **Dependencies:** AGENTS.md memory protocols.

---

### [MEM-014] Auto-Capture Hook (Post-Session Knowledge Extraction)
- **Category:** memory
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | ops-agent
- **Status:** catalogued
- **Source:** power-user-patterns.md (OnlyTerp vault system)
- **Description:** An automatic knowledge extraction process that runs after every session and observes the conversation transcript to identify and store durable knowledge. Creates a self-improving micro-learning loop without requiring the user to explicitly trigger memory writes.
- **Value Proposition:** Passive knowledge building. The agent learns from every interaction automatically without workflow interruption.
- **Implementation Notes:** Configure as a post-session hook or end-of-session cron. Agent reads session transcript and extracts facts meeting the four-filter criteria (MEM-013) into vault files.
- **Dependencies:** Session transcripts accessible; memory criteria filter (MEM-013).

---

### [MEM-015] ByteRover Portable Memory Layer
- **Category:** memory
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal | dev-ops
- **Status:** catalogued
- **Source:** twitter-research-2026-04-05.md
- **Description:** ByteRover is a portable, local-first cross-agent shared memory layer with 92.2% retrieval accuracy on the LoCoMo benchmark. Allows multiple agents to share a unified memory store without coordination overhead.
- **Value Proposition:** Multi-agent deployments need shared memory. ByteRover provides this with high accuracy and local-first privacy. Especially useful for multi-agent teams where context needs to cross agent boundaries.
- **Implementation Notes:** See byterover.dev. Configure as shared memory backend for all agents in a multi-agent setup. Evaluate against QMD for single-agent deployments.
- **Dependencies:** byterover.dev installation; multi-agent setup.

---

### [MEM-016] `/context list` Diagnostic
- **Category:** memory
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md (VelvetShark)
- **Description:** The `/context list` command shows exactly what the model sees in its current context window and which files are truncated. The fastest diagnostic tool when an agent seems to be "forgetting" or behaving unexpectedly.
- **Value Proposition:** Eliminates guesswork in debugging. You can see exactly what context the model has, identify bloated files, and spot truncated content instantly.
- **Implementation Notes:** Run `/context list` any time agent behaviour seems off. Follow up with `/context detail` for per-file, per-tool-schema breakdown. Use `/compact` to manually free window space.
- **Dependencies:** None (built-in command).

---

### [MEM-017] Maps of Content (MOC) Vault Navigation
- **Category:** memory
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | research-agent | ops-agent
- **Status:** catalogued
- **Source:** power-user-patterns.md (OnlyTerp vault system)
- **Description:** Organise vault files using Obsidian-style Maps of Content — index files that link related vault files together. Also includes wiki-links, Agent Notes (observations), and a `.learnings/` directory for distilled wisdom.
- **Value Proposition:** Makes large vaults (50+ files) navigable. The agent can find any piece of knowledge by following MOC links rather than relying purely on search.
- **Implementation Notes:** Create `vault/MOC-*.md` index files for major domains (business, people, projects, technical). Use `[[wiki-link]]` syntax for cross-references. Update MOCs when adding new vault files.
- **Dependencies:** vault/ directory; QMD or other memory search backend.

---

### [MEM-018] Pre-Compaction Memory Flush
- **Category:** memory
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md (VelvetShark), ecosystem-state-march2026.md
- **Description:** OpenClaw has a built-in safety net that saves context before compaction occurs. This is enabled via the memory plugin contract (updated in v2026.3.28). Verify it is active and working for every deployment.
- **Value Proposition:** Prevents complete context loss when the context window fills up. Without this, compaction can silently discard critical information given only in chat.
- **Implementation Notes:** Verify with `/context list` after a long session. Check that pre-compaction flush is listed as active in memory plugin status. The v2026.3.28 Memory Plugin Overhaul moved this behind the active memory plugin contract.
- **Dependencies:** Active memory plugin; v2026.3.28+.

---

### [MEM-019] NDD Structured Logging Format
- **Category:** memory
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 3.5.2)
- **Description:** All meaningful actions logged as Noticed / Decision / Did. Every log entry records what triggered the action, what the agent chose to do and why, and what actually happened (with IDs, paths, outcomes).
- **Value Proposition:** Creates auditable, scannable, compliance-friendly logs. Future sessions understand context instantly. Essential for financial and legal clients.
- **Implementation Notes:** Document the NDD format in AGENTS.md. Enforce append-only principle: never edit existing log entries, only add corrections below. The format is: `### [Task] — HH:MM UTC` then three bullet points: Noticed, Decision, Did.
- **Dependencies:** Daily memory file; AGENTS.md logging protocol.

---

## COST

---

### [CST-001] Model Routing Layer (Intelligent Request Routing)
- **Category:** cost
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** llm-cost-routing-2026-04.md
- **Description:** A routing layer that classifies request complexity before routing to the appropriate model. Simple file reads and status checks go to cheap models (Gemini Flash); complex reasoning and code generation stay on premium models. The layer sits between the agent and the provider.
- **Value Proposition:** Claims of 40-80% cost reduction (claw-llm-router) to 92% (ClawRouter). Most multi-agent setups overpay by sending all requests to premium models regardless of complexity.
- **Implementation Notes:** Simple heuristic: <500 tokens + file ops/status checks → cheap model. Complex reasoning, strategic analysis, code generation → assigned premium model. Start with claw-llm-router (proven, local, privacy-preserving).
- **Dependencies:** Multiple model API keys; routing tool installed.

---

### [CST-002] claw-llm-router (Donn Felker)
- **Category:** cost
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** llm-cost-routing-2026-04.md
- **Description:** Local classification of request complexity before routing to appropriate model. All classification runs locally — no data sent to third parties. Published February 2026. Claims 40-80% cost savings. Available on GitHub.
- **Value Proposition:** Privacy-preserving cost optimisation. Classification happens on your hardware, so sensitive business data isn't sent to a routing API.
- **Implementation Notes:** Install from GitHub (Donn Felker). Test on highest-volume agent first (e.g., marketing agent). Measure costs before/after for one week. Recommended starting point per our research.
- **Dependencies:** Local compute for classification; multiple model API keys.

---

### [CST-003] ClawRouter (BlockRunAI)
- **Category:** cost
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** llm-cost-routing-2026-04.md
- **Description:** Analyses each request across 15 dimensions to route to the optimal model. Claims up to 92% cost reduction. Open-source on GitHub. Published April 2026 — very new at time of research.
- **Value Proposition:** Most sophisticated routing available. 15-dimension analysis catches edge cases that simpler routers miss.
- **Implementation Notes:** Evaluate after claw-llm-router (MEM-002). Give it 2-4 weeks to mature before production deployment. Open-source allows custom dimension tuning.
- **Dependencies:** Multiple model API keys.

---

### [CST-004] Sub-Agent Model Tiering
- **Category:** cost
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md, universal-openclaw-implementation.md
- **Description:** Use cheap models (Sonnet/Haiku) for sub-agents and routine tasks; reserve premium models (Opus) for the main orchestrator and complex reasoning. Configure via `agents.defaults.subagents.model` in openclaw.json.
- **Value Proposition:** 60%+ cost reduction on sub-agent workloads. Sub-agents doing file operations, data formatting, or routine checks don't need Opus.
- **Implementation Notes:** Set `agents.defaults.subagents.model: "anthropic/claude-haiku-4-5"` or similar. Override per-agent for tasks that need more capability. Use the model selection table: Haiku for 60-70% of tasks, Sonnet for complex, Opus only when required.
- **Dependencies:** Multiple model API keys configured.

---

### [CST-005] Batch Processing (50% Discount)
- **Category:** cost
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** content-creator | ops-agent | automation
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Anthropic offers 50% discount for batch processing, but with a 24-hour delivery window. Ideal for bulk content generation, analysis of large datasets, or non-time-sensitive processing tasks.
- **Value Proposition:** Halves API costs for any workload that can tolerate next-day delivery. Content backlogs, weekly reports, large-scale analysis are prime candidates.
- **Implementation Notes:** Identify all tasks where results aren't needed immediately. Schedule these as batch jobs. The 24-hour window fits most overnight processing patterns.
- **Dependencies:** Anthropic API access; ability to structure work as batch requests.

---

### [CST-006] Local Models for Sub-Agents (Ollama/LM Studio)
- **Category:** cost
- **Complexity:** major (4+ hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md, ecosystem-state-march2026.md
- **Description:** Run local models (Qwen3.5 27B via Ollama, or LM Studio) for zero-marginal-cost sub-agent work. Local models handle 60-70% of workload for routine tasks, background checks, and low-stakes processing.
- **Value Proposition:** Zero API cost per token. Monthly costs can drop from $600 to $20 (extreme case). Requires hardware investment but pays off quickly at scale.
- **Implementation Notes:** Qwen 3.5 32B via LM Studio — zero marginal cost but needs 28GB+ RAM. Minimum 16K context, 14B+ parameter model for reliable agent behavior. Mac Studio or Nvidia Jetson are common hardware choices.
- **Dependencies:** Sufficient local hardware (28GB+ RAM for 32B models); Ollama or LM Studio installed.

---

### [CST-007] reserveTokensFloor Configuration
- **Category:** cost
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Set `reserveTokensFloor: 24000` in openclaw.json. This prevents context-limit errors that cascade into retries, which multiply costs. Without this, the model tries to fit too much into context and fails, burning tokens on failed attempts.
- **Value Proposition:** Prevents expensive cascade retry failures. A context limit error that triggers 3 retries costs 4x what a clean request would.
- **Implementation Notes:** Add `"reserveTokensFloor": 24000` to the model configuration in openclaw.json. This is one of the five settings that matter most per community consensus.
- **Dependencies:** openclaw.json access.

---

### [CST-008] Context Pruning (Cache-TTL Mode)
- **Category:** cost
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Cache-TTL context pruning mode auto-trims old tool results without destroying conversation context. Auto-enabled for Anthropic. Reduces token count for long sessions without losing the conversational thread.
- **Value Proposition:** Long sessions accumulate large tool call results (especially browser and exec outputs). Pruning these reduces context size by 20-40% in typical usage.
- **Implementation Notes:** Verify it's active with `/context detail`. For non-Anthropic providers, may need to enable manually in model config.
- **Dependencies:** Anthropic model (auto-enabled) or manual config for other providers.

---

### [CST-009] Disable Unused Plugins
- **Category:** cost
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Every enabled plugin adds context overhead through its tool schema injection. Disable any plugin the agent doesn't use for a given deployment.
- **Value Proposition:** Each disabled plugin saves 200-500 tokens per message. For a high-volume deployment (100+ messages/day), this adds up quickly.
- **Implementation Notes:** Audit enabled plugins with `openclaw config get plugins`. Disable any not actively used. Customer-facing bots especially should have minimal plugins (no browser, no exec for safety AND cost).
- **Dependencies:** openclaw.json access.

---

### [CST-010] Compaction Model — Use Cheaper Model for Summarisation
- **Category:** cost
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** When context compaction runs (summarising old conversation to free window space), it doesn't need to use the same premium model as the main agent. Configure Haiku or similar cheap model for compaction summarisation.
- **Value Proposition:** Compaction can be triggered multiple times in long sessions. Using Haiku instead of Opus for summarisation reduces compaction cost by ~25x.
- **Implementation Notes:** Configure `compaction.model: "anthropic/claude-haiku-4-5"` in model settings. The compaction model only needs to summarise conversation history — full reasoning capability is not required.
- **Dependencies:** Haiku API access; compaction enabled.

---

### [CST-011] Session Resets for Cost Control
- **Category:** cost
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** For Opus, reset the session after each major task. For Sonnet, reset when context exceeds 50% or after 2-3 hours. Long sessions with large context windows burn tokens on irrelevant history from earlier in the session.
- **Value Proposition:** Each reset clears accumulated context overhead. A session that's been running for 4 hours and grown to 80k tokens can be reset with only the relevant task context reloaded.
- **Implementation Notes:** Use `/new` command to reset. Brief the agent with only what's needed for the current task after reset. Combine with Protocol C (MEM-009) to ensure memory is saved before resetting.
- **Dependencies:** Memory protocols to preserve context before reset.

---

### [CST-012] `/usage tokens` Footer
- **Category:** cost
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** The `/usage tokens` command appends per-reply token usage to every response. Enables real-time cost monitoring and helps identify expensive patterns.
- **Value Proposition:** You can't optimise what you can't measure. Token footers make it immediately visible when a particular workflow is disproportionately expensive.
- **Implementation Notes:** Enable with `/usage tokens`. Use cost review cron (AUT-008) to aggregate weekly for trend analysis.
- **Dependencies:** None (built-in command).

---

### [CST-013] Per-Session Context Budget Configuration
- **Category:** cost
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Different sessions can use different context budgets. Main session: 200k context window. Sub-agents: 32k. This prevents sub-agents from accidentally loading large contexts when they only need a small task scope.
- **Value Proposition:** Sub-agents with 32k context cost less per message than sub-agents with 200k context, even on the same model.
- **Implementation Notes:** Configure `context.maxTokens` per agent in the agents list. Set sub-agents to 32k by default unless the task requires more.
- **Dependencies:** Per-agent configuration support.

---

### [CST-014] SaladCloud Distributed GPU Inference
- **Category:** cost
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | dev-ops | content-creator
- **Status:** catalogued
- **Source:** llm-cost-routing-2026-04.md
- **Description:** Run models on distributed GPU infrastructure via SaladCloud instead of API calls. Significant cost reduction for high-volume production workloads. More suitable for large-scale deployments.
- **Value Proposition:** Can reduce inference costs by 70-90% vs API pricing for high-volume workloads. Trades setup complexity for major ongoing savings.
- **Implementation Notes:** Evaluate for deployments processing 100k+ tokens/day where API costs exceed $100/month. SaladCloud provides per-minute GPU pricing.
- **Dependencies:** High-volume workload to justify setup; compatible open-source model.

---

### [CST-015] Cross-Provider Model Fallback Chain
- **Category:** cost
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 1.2 Auth Failover)
- **Description:** Configure a full fallback chain across providers so that rate limits on one provider automatically route to cheaper alternatives. Example chain: Anthropic Opus → Anthropic Sonnet → OpenRouter Opus → Google Gemini → OpenAI GPT.
- **Value Proposition:** Prevents agent downtime from rate limits. Also naturally routes to cheaper providers when premium ones are rate-limited.
- **Implementation Notes:** Configure `agents.defaults.model.fallbacks` array with full chain. Combine with auth profile rotation (ARC-004) within the same provider before falling to a different provider.
- **Dependencies:** Multiple provider API keys; auth.order and auth.cooldowns configured.

---

### [CST-016] Claude Code Subscription for Higher Limits
- **Category:** cost
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** dev-ops
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md
- **Description:** Claude Code subscription provides higher usage limits for serious development use cases. More cost-effective than pure API billing for developers making heavy use of Claude for coding tasks.
- **Value Proposition:** Fixed monthly cost vs variable API billing. Predictable budgeting for dev-ops agents doing continuous coding work.
- **Implementation Notes:** Evaluate based on expected monthly API spend. Break-even point depends on usage volume.
- **Dependencies:** Anthropic account.

---

## SECURITY

---

### [SEC-001] Gateway Authentication (Non-Default — Must Enable)
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md (42,665 exposed instances), security-hardening-playbook.md
- **Description:** OpenClaw authentication is not enabled by default. Anyone who finds the gateway address can use the agent. Must explicitly enable via `gateway.auth.enabled: true` and configure an auth token.
- **Value Proposition:** 42,665 OpenClaw instances were found exposed in one scan. Unauthenticated = anyone can use your agent, access your memory, and potentially execute commands.
- **Implementation Notes:** Set `"gateway": {"auth": {"enabled": true}}` in openclaw.json. Verify with `openclaw doctor`. This is non-negotiable for any deployment.
- **Dependencies:** openclaw.json access; gateway restart.

---

### [SEC-002] Non-Root User for OpenClaw Service
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md, security-hardening-playbook.md, universal-openclaw-implementation.md
- **Description:** Create a dedicated non-root user for OpenClaw: `useradd -r -m -d /home/openclaw -s /bin/bash openclaw`. Never run OpenClaw as root on a VPS. Running as root means any security breach = complete server compromise.
- **Value Proposition:** Limits blast radius of any agent compromise, prompt injection, or security vulnerability to the openclaw user's permissions, not full system access.
- **Implementation Notes:** `useradd -r -m -d /home/openclaw -s /bin/bash openclaw`. Configure systemd service to run as this user (User= in service file). Add user to any needed groups (docker, etc.) but keep group membership minimal.
- **Dependencies:** VPS or server access; sudo/root for initial setup.

---

### [SEC-003] SSH Key-Only Authentication
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 1.3)
- **Description:** Disable SSH password authentication, enable key-only auth. Set `PermitRootLogin no`, `PasswordAuthentication no`, `PubkeyAuthentication yes`, `MaxAuthTries 3` in `/etc/ssh/sshd_config`.
- **Value Proposition:** Password brute-force attacks are constant (thousands per day on any public IP). Key-only auth makes SSH brute-force effectively impossible.
- **Implementation Notes:** Add SSH public key to `~/.ssh/authorized_keys` BEFORE disabling password auth to avoid lockout. Reload SSH: `systemctl reload ssh`. Add Fail2Ban for additional protection.
- **Dependencies:** SSH public key available; server access.

---

### [SEC-004] UFW Firewall Configuration
- **Category:** security
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 1.2), universal-openclaw-implementation.md
- **Description:** Configure UFW with default deny incoming, allow outgoing. Only permit SSH and Mission Control from Tailscale network (100.64.0.0/10). Block everything else.
- **Value Proposition:** Makes the server invisible to internet scanners. The gateway runs on localhost only (127.0.0.1), so even if the firewall fails, it's not publicly accessible.
- **Implementation Notes:** `ufw default deny incoming`, `ufw default allow outgoing`, `ufw allow from 100.64.0.0/10 to any port 22`. Enable AFTER Tailscale is connected to avoid lockout. Verify with `ufw status verbose`.
- **Dependencies:** Tailscale (SEC-007) installed first; current SSH session must not be locked out.

---

### [SEC-005] Fail2Ban for Brute Force Protection
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md, universal-openclaw-implementation.md
- **Description:** Install and enable Fail2Ban to automatically block IP addresses showing signs of brute-force attacks (repeated failed SSH logins). Standard Ubuntu package: `apt install -y fail2ban`.
- **Value Proposition:** Automated response to brute-force attempts. Bans attacking IPs after configurable failure threshold.
- **Implementation Notes:** `apt install -y fail2ban && systemctl enable fail2ban`. Default configuration protects SSH. Review `/etc/fail2ban/jail.conf` for custom thresholds. Health script should monitor auth failure count (SEC-020).
- **Dependencies:** UFW (SEC-004); server access.

---

### [SEC-006] Unattended Security Upgrades
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md, universal-openclaw-implementation.md
- **Description:** Enable automatic security updates via `unattended-upgrades` package. Ensures the OS receives security patches without manual intervention.
- **Value Proposition:** Most server compromises exploit known, patched vulnerabilities. Unattended upgrades close these automatically.
- **Implementation Notes:** `apt install -y unattended-upgrades && dpkg-reconfigure --priority=low unattended-upgrades`. Configure to auto-install security updates only (not full dist-upgrades).
- **Dependencies:** Debian/Ubuntu server; root access.

---

### [SEC-007] Tailscale VPN for Private Access
- **Category:** security
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 1.1), power-user-patterns.md
- **Description:** Install Tailscale on the server and all client devices. Makes the server accessible only to authorized Tailscale network members. No port forwarding required, works through NATs. Free for up to 100 devices.
- **Value Proposition:** Makes the server invisible to the public internet. Only authorized devices with Tailscale installed can reach it. Zero-config VPN with device-level authentication.
- **Implementation Notes:** `curl -fsSL https://tailscale.com/install.sh | sh && tailscale up`. Use Tailscale IP (100.x.x.x) for all internal access. Mission Control accessible only via Tailscale IP or `tailscale serve`.
- **Dependencies:** Client installs Tailscale on their phone/laptop; Tailscale account.

---

### [SEC-008] nativeSkills: false (Disable Auto-Download)
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md, security-hardening-playbook.md
- **Description:** Set `nativeSkills: false` in agents.defaults to prevent automatic download and installation of community skills. Vet every skill before installation.
- **Value Proposition:** ~10.8% of ClawHub plugins were flagged as malicious before ClawNet scanning. Cisco research found data exfiltration and prompt injection in third-party skills. Auto-install is dangerous.
- **Implementation Notes:** Set `"agents": {"defaults": {"nativeSkills": false}}` in openclaw.json. Review skill source code before installation. Have OpenClaw analyse suspicious skills. ClawNet by Silverfort provides additional scanning.
- **Dependencies:** openclaw.json access.

---

### [SEC-009] ClawSec — Skill Security Suite
- **Category:** security
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md (prompt-security/clawsec on GitHub)
- **Description:** ClawSec provides SOUL.md drift detection, live security recommendations, automated audits, and skill integrity verification. Detects if agent personality or security settings have drifted from their configured state.
- **Value Proposition:** Detects prompt injection attacks that subtly modify agent behaviour. SOUL.md drift is a real attack vector — an attacker who can manipulate SOUL.md can reprogram agent behaviour.
- **Implementation Notes:** Install from prompt-security/clawsec on GitHub. Enable drift detection for periodic checks. Configure alerts when drift is detected.
- **Dependencies:** OpenClaw installation; GitHub access.

---

### [SEC-010] Channel allowFrom / dmPolicy / groupPolicy
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 2), universal-openclaw-implementation.md
- **Description:** Configure each channel to only respond to authorised user IDs. Set `dmPolicy: "allowlist"`, `allowFrom: ["<USER_ID>"]`, and `groupPolicy: "deny"` (or allowlist specific groups).
- **Value Proposition:** Prevents unauthorised users from accessing the agent via discoverable Telegram/Discord bots. Without allowFrom, any user who finds the bot can interact with it.
- **Implementation Notes:** Get client Telegram ID via @userinfobot. For Discord, enable Developer Mode, right-click user → Copy User ID. Test with an unauthorised account — should get no response.
- **Dependencies:** User IDs from client; channel configuration access.

---

### [SEC-011] Gateway Bound to Localhost (127.0.0.1)
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 1.4), universal-openclaw-implementation.md
- **Description:** Verify the OpenClaw gateway only listens on 127.0.0.1, not 0.0.0.0 (all interfaces). If bound to 0.0.0.0, anyone with network access can reach the gateway directly.
- **Value Proposition:** Even if UFW is misconfigured, a gateway bound to localhost is not publicly reachable.
- **Implementation Notes:** Check: `grep bind ~/.openclaw/openclaw.json` and `ss -tlnp | grep 18789`. If showing 0.0.0.0, set `"gateway": {"bind": "127.0.0.1:18789"}` in openclaw.json. Restart gateway.
- **Dependencies:** openclaw.json access; gateway restart.

---

### [SEC-012] Workspace-Only Filesystem Restriction
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** customer-service | sales-agent
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 4.1)
- **Description:** Set `tools.fs.workspaceOnly: true` for agents that don't need system-wide file access. Restricts file read/write/edit to the workspace directory only — agents can't browse /etc/, home directories, or other system files.
- **Value Proposition:** Contains the blast radius of a compromised or prompt-injected customer-facing agent. An agent that can only read workspace files can't exfiltrate system credentials or configuration.
- **Implementation Notes:** Set per-agent in `agents.list[*].tools.fs.workspaceOnly: true`. Exception: the main orchestrator may need broader access. Grant per-agent, not globally.
- **Dependencies:** Per-agent configuration.

---

### [SEC-013] exec: deny for Customer-Facing Agents
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** customer-service | sales-agent | hospitality
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 4.2)
- **Description:** Set `exec.security: "deny"` for any agent that handles untrusted input (customer messages, public inquiries). Customer-facing bots should never be able to run shell commands.
- **Value Proposition:** Eliminates prompt injection → command execution attack vector. An attacker who can inject into a customer message cannot run arbitrary commands if exec is denied entirely.
- **Implementation Notes:** Per-agent config: `"exec": {"security": "deny"}`. Use `"allowlist"` for agents that need specific commands. Full exec only for the trusted main orchestrator.
- **Dependencies:** Per-agent configuration.

---

### [SEC-014] Two-Way Door Principle (Reversible vs Irreversible Actions)
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Agent configuration principle: act freely on reversible decisions (drafting, searching, reading), pause and confirm with the human before irreversible actions (sending emails, deleting data, making purchases, publishing content).
- **Value Proposition:** Balances autonomy with safety. Prevents the agent from taking unrecoverable actions based on misunderstood instructions.
- **Implementation Notes:** Document in AGENTS.md: list reversible actions (can proceed without approval) and irreversible actions (must confirm). Combine with tool approval hooks (SEC-015) for automated enforcement.
- **Dependencies:** AGENTS.md definition of reversible/irreversible actions list.

---

### [SEC-015] Plugin Tool Approval Hooks (requireApproval)
- **Category:** security
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 4.4), ecosystem-state-march2026.md
- **Description:** Configure `hooks.before_tool_call.requireApproval` for high-risk tools (exec, browser, message). When triggered, execution pauses and prompts the user for approval via Telegram buttons or Discord interactions.
- **Value Proposition:** Provides a human checkpoint before any high-risk operation. Introduced in v2026.3.22. Prevents automated actions from proceeding without explicit human sign-off.
- **Implementation Notes:** Configure in hooks section of openclaw.json. Specify which tools and which agents require approval. Requires v2026.3.22+. Test with a triggering action to verify the approval UI appears.
- **Dependencies:** v2026.3.22+; interactive channel (Telegram/Discord) for approval UI.

---

### [SEC-016] Secrets in .env (Never in openclaw.json)
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 5), universal-openclaw-implementation.md
- **Description:** All secrets (API keys, bot tokens) in `~/.openclaw/.env` with `chmod 600`. Never in openclaw.json (world-readable by default), workspace files (loaded into AI context), git repos, or chat messages.
- **Value Proposition:** openclaw.json can be accidentally committed to git or left world-readable. .env with 600 permissions is owner-only and excluded from git by default.
- **Implementation Notes:** Create `~/.openclaw/.env`, add all secrets, `chmod 600 ~/.openclaw/.env`. Reference in systemd service via `EnvironmentFile=`. Check: `stat -c %a ~/.openclaw/.env` should return 600.
- **Dependencies:** systemd service (ARC-001); .gitignore for .env.

---

### [SEC-017] Mission Control Authentication
- **Category:** security
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 1.5)
- **Description:** Mission Control (Next.js dashboard, port 3333) has no built-in authentication. Options: Tailscale-only (bind to 127.0.0.1, access via Tailscale IP), Nginx reverse proxy with basic auth, or Tailscale Serve for zero-config HTTPS.
- **Value Proposition:** Without protection, anyone who can reach port 3333 can see full business operations data. Tailscale Serve is the recommended zero-config option.
- **Implementation Notes:** Recommended: `tailscale serve https:3333 / http://127.0.0.1:3333`. Client accesses via `https://<hostname>.<tailnet>.ts.net:3333` — encrypted and authenticated by Tailscale identity.
- **Dependencies:** Tailscale (SEC-007); Mission Control deployed.

---

### [SEC-018] NVIDIA NemoClaw Enterprise Security Sandboxing
- **Category:** security
- **Complexity:** major (4+ hours)
- **Use Case Tags:** finance | hospitality | education | universal
- **Status:** catalogued
- **Source:** power-user-patterns.md, ecosystem-state-march2026.md
- **Description:** NVIDIA's NemoClaw stack runs OpenClaw inside OpenShell with managed inference, policy-based security, network guardrails, and privacy isolation. Single-command install adding Nemotron models. Announced at GTC 2026. Runs on DGX Station, DGX Spark, RTX workstations.
- **Value Proposition:** Enterprise-grade security for on-premises AI. All inference runs locally — data never leaves the premises. Ideal for law firms, medical practices, financial institutions with strict data sovereignty requirements.
- **Implementation Notes:** Requires NVIDIA hardware (DGX Station/Spark or RTX workstation). Follow NemoClaw installation guide from GTC 2026 materials. Network/privacy guardrails configurable via policy files.
- **Dependencies:** NVIDIA hardware; NemoClaw distribution; sufficient GPU VRAM.

---

### [SEC-019] Append-Only Audit Logs
- **Category:** security
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** finance | ops-agent | education
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 3.5.5), security-hardening-playbook.md (Layer 7)
- **Description:** Make daily memory files append-only after creation using `chattr +a`. Even root can't modify existing content without removing the flag. Creates tamper-proof audit trail for compliance-sensitive deployments.
- **Value Proposition:** Genuine audit trail for financial data access. Satisfies compliance requirements for record-keeping. NDD format (MEM-019) combined with append-only ensures complete, unmodifiable action history.
- **Implementation Notes:** Add to health script: `chattr +a /path/to/memory/$(date -d "yesterday" +%Y-%m-%d).md`. Combine with log retention/archival: compress logs older than 90 days while retaining them.
- **Dependencies:** Linux filesystem with chattr support; health script (MON-001).

---

### [SEC-020] SSH Auth Failure Monitoring
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 6.2)
- **Description:** Add SSH auth failure monitoring to the health script. Count failed SSH attempts from `journalctl` in the last 4 hours. Alert if >10 failures — possible brute force indicator.
- **Value Proposition:** Early warning of targeted attacks or compromised credentials. Combined with Fail2Ban (SEC-005) provides both detection and automated response.
- **Implementation Notes:** Add to health script: `AUTH_FAILS=$(journalctl -u ssh --since "4 hours ago" --no-pager | grep -c "Failed password\|Invalid user")`. Alert via Telegram if threshold exceeded.
- **Dependencies:** Health script (MON-001); Fail2Ban (SEC-005); journalctl access.

---

### [SEC-021] Unexpected Port Detection
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 6.2)
- **Description:** Health script check for unexpected publicly-facing listening ports. `ss -tlnp` filtered to exclude localhost and Tailscale addresses. Alert if any public-facing ports appear unexpectedly.
- **Value Proposition:** Detects if an agent or malicious process has opened a backdoor. Any new public-facing port is a potential security incident.
- **Implementation Notes:** Add to health script: `ss -tlnp | grep -v "127.0.0.1\|::1" | grep -v "tailscale"`. Alert on any unexpected entries.
- **Dependencies:** Health script (MON-001); UFW baseline.

---

### [SEC-022] File Permission Integrity Checks
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 6.2)
- **Description:** Health script checks that sensitive files (.env, auth-profiles.json) maintain correct permissions (600). Alerts if permissions have drifted.
- **Value Proposition:** Permission drift can happen after package updates or accidental operations. Automated checks ensure sensitive files never become world-readable.
- **Implementation Notes:** Add to health script: `stat -c %a ~/.openclaw/.env` and `stat -c %a ~/.openclaw/auth-profiles.json`. Alert if either is not 600.
- **Dependencies:** Health script (MON-001).

---

### [SEC-023] exec-approvals.json (Post-Update Exec Policy)
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 1.2 Exec Approvals), incident: Exec Lockout 2 Apr 2026
- **Description:** v2026.4.1+ requires an explicit `exec-approvals.json` host-local policy file. Without it, exec defaults to deny regardless of openclaw.json settings. Must be configured after every OpenClaw update that touches exec policies.
- **Value Proposition:** Without this, agents lose all exec access after updates — including basic commands like `ls`. The 2 Apr 2026 incident required the human to run all diagnostic commands manually.
- **Implementation Notes:** `openclaw approvals set --stdin` with policy JSON. For client deployments, use allowlist with ask:on-miss for sub-agents; full/off for main agent. Test with `echo test` after every update.
- **Dependencies:** v2026.4.1+; OpenClaw installed.

---

### [SEC-024] SlowMist Security Practice Guide
- **Category:** security
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md (slowmist/openclaw-security-practice-guide)
- **Description:** An agent-facing security guide from SlowMist that the agent itself can internalise via a SOUL.md or skill. Covers prompt injection defence, credential handling, social engineering resistance, and safe action patterns.
- **Value Proposition:** Security knowledge the agent carries with it. Rather than relying solely on configuration, the agent actively resists manipulation and applies security best practices.
- **Implementation Notes:** Review the guide at slowmist/openclaw-security-practice-guide on GitHub. Extract key rules for inclusion in SOUL.md or AGENTS.md. Periodically update as the guide evolves.
- **Dependencies:** Access to the guide; SOUL.md update.

---

### [SEC-025] Session Audit Trail and Archival
- **Category:** security
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** finance | ops-agent | education
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 6.3)
- **Description:** Archive session JSONL files monthly to a dedicated archive directory. Retain for 12 months. Session files contain full conversation history including any sensitive data discussed.
- **Value Proposition:** Compliance requirement for financial and legal clients. Also enables post-incident investigation.
- **Implementation Notes:** Monthly cron: `find ~/.openclaw/agents/*/sessions/ -name "*.jsonl" -mtime +30 -exec mv {} $ARCHIVE_DIR/ \;`. Consider encryption for highly sensitive deployments.
- **Dependencies:** systemd cron or crontab; archive directory.

---

### [SEC-026] Exec Security Allowlist Pattern
- **Category:** security
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** ops-agent | dev-ops
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 4.2), universal-openclaw-implementation.md
- **Description:** For agents that need some exec access but shouldn't have unrestricted shell: configure `exec.security: "allowlist"` with an explicit list of permitted commands. Principle of least privilege for exec.
- **Value Proposition:** Sub-agents that need to run specific commands (e.g., `openclaw`, `git`, `curl`) can be given exactly those without full shell access.
- **Implementation Notes:** In agent config: `"exec": {"security": "allowlist", "allowedCommands": ["git", "curl", "openclaw"]}`. Test each command in the allowlist. Sub-agents default to allowlist; main orchestrator gets full.
- **Dependencies:** Per-agent configuration; exec-approvals.json (SEC-023).

---

## UX

---

### [UX-001] SOUL.md Concrete Examples (Not Abstract Rules)
- **Category:** ux
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md, universal-openclaw-implementation.md
- **Description:** SOUL.md should use concrete example exchanges to define tone and behaviour, not abstract directives like "be friendly." Include example conversations showing exactly how the agent should respond in key scenarios.
- **Value Proposition:** Models follow examples far better than rules. A SOUL.md with "Here's how to handle a frustrated customer: [example]" produces more consistent behaviour than "Be empathetic and professional."
- **Implementation Notes:** For each major scenario (greeting, bad news, uncertainty, disagreement), include a short example exchange. Keep total SOUL.md under 1KB — examples should be brief.
- **Dependencies:** SOUL.md file.

---

### [UX-002] Anti-Sycophancy Rule in SOUL.md
- **Category:** ux
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md, universal-openclaw-implementation.md
- **Description:** Widely-adopted rule in SOUL.md: "Have opinions. Disagree when warranted. No sycophancy." Prevents the agent from reflexively agreeing with everything the user says.
- **Value Proposition:** Sycophantic agents give bad advice and are less useful. An agent that pushes back thoughtfully on bad ideas is genuinely more valuable — especially for business decisions.
- **Implementation Notes:** Add to SOUL.md (1 line): "Have opinions. Disagree when warranted. If you think a plan is flawed, say so clearly before offering to help execute it."
- **Dependencies:** SOUL.md file.

---

### [UX-003] Anti-Echo-Chamber Mandate
- **Category:** ux
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** personal-assistant | ops-agent
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Kilmurry lessons learned)
- **Description:** Distinct from anti-sycophancy: define what the agent should challenge vs defer on. Examples: challenge market assumptions, push back on timeline estimates, defer on personal preferences. Makes the agent a genuine thinking partner.
- **Value Proposition:** Clients love an agent that pushes back thoughtfully. It differentiates the deployment from a glorified autocomplete and produces better business decisions.
- **Implementation Notes:** Add to SOUL.md: "Challenge: market assumptions, time estimates, cost projections. Defer: personal preferences, aesthetic choices, final decisions." Adjust per client.
- **Dependencies:** SOUL.md file.

---

### [UX-004] Multiple SOUL.md Files for Different Contexts
- **Category:** ux
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | ops-agent
- **Status:** catalogued
- **Source:** power-user-patterns.md (Reza Rezvani)
- **Description:** Maintain multiple SOUL.md profiles in `~/.openclaw/souls/`: default.md, work.md, casual.md, customer-service.md. Switch with `openclaw soul use <name>`. Different contexts warrant different personas.
- **Value Proposition:** A personal assistant that handles both business strategy and casual conversation benefits from context-switching. Customer-service mode is more patient and formal; casual mode is warmer.
- **Implementation Notes:** Create `~/.openclaw/souls/` directory with named profiles. Each should be <1KB. Switch profiles as needed. Consider auto-switching based on time of day or channel.
- **Dependencies:** Soul profile directory; `openclaw soul` command support.

---

### [UX-005] AGENTS.md as Decision Tree
- **Category:** ux
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md (TechNickAI), universal-openclaw-implementation.md
- **Description:** AGENTS.md should function as an explicit decision tree: "If task is X → use sub-agent with model Y. If task is Z → handle directly." Removes ambiguity about when to delegate vs handle directly.
- **Value Proposition:** Consistent, predictable agent routing. Without a decision tree, the agent makes ad-hoc decisions about delegation that produce inconsistent results.
- **Implementation Notes:** Structure AGENTS.md with a "Routing Rules" section. Use `|Task Type|Action|Model|` table format. Keep the tree shallow (2-3 levels) to fit within the <3KB budget.
- **Dependencies:** AGENTS.md file; sub-agent configuration.

---

### [UX-006] ARCHITECTURE.md for Model Choices
- **Category:** ux
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** ops-agent | dev-ops
- **Status:** catalogued
- **Source:** power-user-patterns.md (DEV Community)
- **Description:** A separate `ARCHITECTURE.md` file documenting model choices, resource budgets, and when to use local vs cloud models. Not injected into every message — consulted on demand.
- **Value Proposition:** Documents the "why" behind infrastructure decisions. Valuable when onboarding new team members, reviewing deployments, or troubleshooting unexpected model behaviour.
- **Implementation Notes:** Store outside the workspace (not loaded every message). Cover: model assignments per agent, context budget per agent, cost thresholds, local vs cloud decision criteria.
- **Dependencies:** Multi-model deployment; maintenance discipline.

---

### [UX-007] DESIGN.md Markdown Design System
- **Category:** ux
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** content-creator | ops-agent
- **Status:** catalogued
- **Source:** twitter-research-2026-04-05.md (Google Stitch / VoltAgent/awesome-design-md)
- **Description:** DESIGN.md files encode brand guidelines, visual standards, and design patterns for AI agents. 55+ pre-built templates available via VoltAgent/awesome-design-md on GitHub.
- **Value Proposition:** Consistent brand output from AI-generated content. Design constraints prevent the agent from producing content that conflicts with brand guidelines.
- **Implementation Notes:** Download relevant template from VoltAgent/awesome-design-md. Customise with client brand colours, fonts, tone. Reference in SOUL.md or skills that handle content generation.
- **Dependencies:** Brand guidelines from client; GitHub access.

---

### [UX-008] /btw Side Conversations
- **Category:** ux
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (v2026.3.22)
- **Description:** The `/btw` command handles lightweight tangents without polluting main context or consuming excessive tokens. Introduced in v2026.3.22. Keeps the main conversation thread clean.
- **Value Proposition:** Reduces context pollution and token waste from tangential questions. Tangents don't push important context out of the window.
- **Implementation Notes:** Use `/btw` for quick factual questions, side queries, or clarifications during a main task. Context stays separate and doesn't affect the main thread.
- **Dependencies:** v2026.3.22+.

---

### [UX-009] ClawSuite Desktop UI / Command Center
- **Category:** ux
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | personal-assistant | dev-ops
- **Status:** catalogued
- **Source:** twitter-research-2026-04-05.md (@outsource_/Eric, 30K clones)
- **Description:** ClawSuite (github.com/outsourc-e/clawsuite) is a full desktop UI and command center for OpenClaw. 30,000 clones. Could replace custom Mission Control dashboards for clients who prefer a native desktop experience.
- **Value Proposition:** Ready-made UI reduces the need to build custom Mission Control. 30K clones suggests strong community validation.
- **Implementation Notes:** Evaluate against custom Mission Control (ARC-015). May be better for non-technical clients who need a polished interface without custom development.
- **Dependencies:** Compatible OS; OpenClaw gateway running.

---

### [UX-010] ClawChief — Chief of Staff Pattern
- **Category:** ux
- **Complexity:** major (4+ hours)
- **Use Case Tags:** personal-assistant | ops-agent
- **Status:** catalogued
- **Source:** twitter-research-2026-04-05.md (Ryan Carson, 844K views)
- **Description:** ClawChief (github.com/snarktank/clawchief) deploys OpenClaw as a Chief of Staff with a priority map and auto-resolver. Identifies the most important task, resolves dependencies automatically, and executes in priority order.
- **Value Proposition:** Transforms the agent from reactive (answers questions) to proactive (identifies and executes highest-priority work). Highly viewed — 844K — suggesting strong market interest.
- **Implementation Notes:** Review Ryan Carson's ClawChief implementation. Adapt priority map and auto-resolver for the client's specific workflow. Especially relevant for busy executives or ops leads.
- **Dependencies:** OpenClaw installation; priority system integration.

---

### [UX-011] Voice Integration (ElevenLabs + Twilio)
- **Category:** ux
- **Complexity:** major (4+ hours)
- **Use Case Tags:** personal-assistant | customer-service | hospitality
- **Status:** catalogued
- **Source:** power-user-patterns.md (Section 10), community-use-cases.md
- **Description:** Full voice stack: ElevenLabs for TTS with custom voice synthesis, Vapi for call management (STT, TTS, turn-taking), Twilio for real phone numbers. Agent can make and receive phone calls. Setup: enable chatCompletions endpoint, expose with ngrok, point ElevenLabs/Vapi at that URL.
- **Value Proposition:** Phone-based customer service, dinner reservation booking, morning briefings via phone call. Premium differentiator — most consultants don't offer voice integration yet.
- **Implementation Notes:** Enable `chatCompletions` endpoint in openclaw.json → expose with ngrok → point ElevenLabs/Vapi at that URL → add Twilio for real phone number. OpenClaw whisper skill available for local STT (no API key needed).
- **Dependencies:** ElevenLabs API, Vapi account, Twilio account; ngrok or public endpoint.

---

### [UX-012] OpenAI Whisper Local STT
- **Category:** ux
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | education | hospitality
- **Status:** catalogued
- **Source:** power-user-patterns.md (Section 10)
- **Description:** Local speech-to-text using the Whisper CLI with no API key required. Process voice messages from Telegram/WhatsApp without sending audio to third-party APIs.
- **Value Proposition:** Privacy-preserving voice transcription. Zero marginal cost per transcription. Supports multilingual transcription.
- **Implementation Notes:** Install Whisper CLI (Python package). Configure as STT backend for voice message processing. Available as a skill from ClawHub or the openai-whisper skill in the skills directory.
- **Dependencies:** Python; Whisper CLI; sufficient CPU/GPU for transcription.

---

### [UX-013] Autonomy Levels (Responsive/Ambient/Proactive/Dormant)
- **Category:** ux
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 3.5.1)
- **Description:** Four autonomy levels based on time since last human message: Responsive (<30 min, answer only), Ambient (30 min-2h, light proactive work), Proactive (2-8h, run analyses, send summaries), Dormant (8h+/overnight, critical alerts only). Tracked in `heartbeat-state.json`.
- **Value Proposition:** Prevents token waste overnight (dormant) while enabling useful background work during away periods. Makes the agent's behaviour predictable and explainable.
- **Implementation Notes:** Add autonomy tracking to `heartbeat-state.json`: `{"autonomy": {"lastHumanMessage": null, "level": "responsive"}}`. Document level rules in AGENTS.md and HEARTBEAT.md. HEARTBEAT.md Step 0 checks level before taking any action.
- **Dependencies:** heartbeat-state.json; HEARTBEAT.md; AGENTS.md.

---

### [UX-014] Multi-Surface Message Delivery
- **Category:** ux
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (v2026.3.2)
- **Description:** Single agent can deliver rich messages (text + screenshots + PDFs) across multiple channels simultaneously. Introduced in v2026.3.2.
- **Value Proposition:** A morning briefing can be sent as text to Telegram, PDF to email, and a summary card to Slack — all from one agent task.
- **Implementation Notes:** Use `--deliver` flag with multiple `--channel` targets. Combine text, file attachments, and screenshots in a single delivery action.
- **Dependencies:** v2026.3.2+; multiple channels configured.

---

### [UX-015] Telegram Streaming (Live Typing Previews)
- **Category:** ux
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** personal-assistant | customer-service
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (v2026.3.2)
- **Description:** Telegram channel now defaults to streaming partial live typing previews — users see the response being generated in real time, not a delay followed by the full response.
- **Value Proposition:** Significantly improves perceived responsiveness. Users know the agent is working rather than waiting for a complete response.
- **Implementation Notes:** Enabled by default in v2026.3.2+ for Telegram. No configuration needed. Verify it's not disabled by a legacy setting in channel config.
- **Dependencies:** v2026.3.2+; Telegram channel.

---

### [UX-016] Socratic Tutor Persona (Education)
- **Category:** ux
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** education
- **Status:** catalogued
- **Source:** community-use-cases.md (@judsoder on X)
- **Description:** AI tutor configured with Socratic method — pulls assignments from Canvas LMS, knows each student's interests and learning styles, guides without giving answers, speaks in parent's cloned voice.
- **Value Proposition:** Learning-theory-aligned tutoring that promotes understanding over answer delivery. Custom voice in the parent's cloned style creates trust and familiarity.
- **Implementation Notes:** Configure SOUL.md with Socratic questioning patterns. Integrate Canvas LMS for assignment data. Add student profiles to vault/people/. ElevenLabs for cloned parent voice.
- **Dependencies:** Canvas LMS integration; ElevenLabs for voice; student/learning profiles.

---

### [UX-017] Savage Roaster Mode (Fitness Motivation)
- **Category:** ux
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** personal-assistant
- **Status:** catalogued
- **Source:** community-use-cases.md (r/AI_Agents fitness coach)
- **Description:** Adaptive tone in fitness/health agent: agent adjusts communication style based on progress. Includes a "Savage Roaster" mode that activates when progress is poor — harsh-but-motivating feedback style.
- **Value Proposition:** Personalized engagement styles dramatically improve adherence. Some users respond better to tough love than encouragement.
- **Implementation Notes:** Add to SOUL.md: tone adaptation rules based on progress metrics. Define "Savage Roaster" trigger conditions (e.g., missed workouts >3 days). Needs progress data from Apple Health or similar.
- **Dependencies:** Health/fitness data integration; progress tracking.

---

### [UX-018] IDENTITY.md Persona System
- **Category:** ux
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md (Reza Rezvani), universal-openclaw-implementation.md
- **Description:** IDENTITY.md defines the agent's name, creature archetype, vibe, and emoji. Multiple IDENTITY.md personas possible for different contexts — professional, creative, customer-facing.
- **Value Proposition:** A named agent with a distinct personality is more memorable and engaging for end users. "Ask Wrench" is stickier than "ask the AI."
- **Implementation Notes:** Keep under 200 bytes. Include: Name, Creature (metaphor), Vibe (2-3 adjectives), Emoji. Distinct from SOUL.md — IDENTITY.md is the "what am I" file, SOUL.md is the "how do I behave" file.
- **Dependencies:** SOUL.md (separate from identity).

---

## AUTOMATION

---

### [AUT-001] Morning Briefing Cron
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | ops-agent | hospitality
- **Status:** in-playbook
- **Source:** power-user-patterns.md, universal-openclaw-implementation.md
- **Description:** Daily 7am cron delivering weather, calendar, unread emails, top news, pending tasks, and sector-specific data (e.g., hotel occupancy, overnight reviews). Uses Sonnet or Opus depending on depth required.
- **Value Proposition:** The most universally valuable automation. Clients start every day informed without any manual work. Immediate demonstrable value.
- **Implementation Notes:** `openclaw cron add --cron "0 7 * * 1-5"`. Customise sources per client (calendar API, email, weather API, sector data). Deliver via Telegram. Use Sonnet for standard briefings, Opus + high thinking for weekly deep reviews.
- **Dependencies:** Channel configured; relevant integrations; client timezone.

---

### [AUT-002] End-of-Day Review Cron
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | ops-agent
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Daily 6pm cron recapping tasks completed, flagging pending items, and preparing tomorrow's priority list. Uses today's memory file as input.
- **Value Proposition:** Closure ritual that ensures no tasks fall through the cracks. Prepares the agent for the next day with context already loaded.
- **Implementation Notes:** `openclaw cron add --cron "0 18 * * 1-5"`. Agent reads today's memory file, compares against task list, drafts end-of-day summary. Deliver to Telegram.
- **Dependencies:** Morning briefing (AUT-001) for baseline; task tracking system.

---

### [AUT-003] Competitor Monitoring Cron
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** ops-agent | hospitality | retail | sales-agent
- **Status:** in-playbook
- **Source:** power-user-patterns.md, multi-agent-coordination-playbook.md
- **Description:** Every 4 hours (or weekly for deeper analysis), check competitor websites for pricing and feature changes. Snapshot pricing pages, scrape tables, log changes.
- **Value Proposition:** Continuous competitive intelligence without human effort. Price changes are caught within hours, not days.
- **Implementation Notes:** `openclaw cron add --cron "0 */4 * * *"`. Use browser tool for pricing page snapshots. Store results in vault/business/competitors.md. Alert only when changes detected.
- **Dependencies:** Browser automation; competitor URL list; vault structure.

---

### [AUT-004] Weekly Deep Analysis Cron
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** ops-agent | finance | personal-assistant
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Weekly Monday 6am cron using Opus + high thinking for full project progress review, strategic analysis, and forward planning.
- **Value Proposition:** Expensive Opus reasoning justified for weekly strategic work. Cheaper models handle daily tasks; Opus handles the big picture once a week.
- **Implementation Notes:** `openclaw cron add --cron "0 6 * * 1" --model "anthropic/claude-opus-4-6" --thinking high`. Customise analysis scope per client — hotel revenue, software project progress, financial review.
- **Dependencies:** Opus API access; relevant data sources.

---

### [AUT-005] Inbox Triage Cron
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | ops-agent | customer-service
- **Status:** catalogued
- **Source:** power-user-patterns.md (TechNickAI Email Steward workflow)
- **Description:** Every 2 hours: archive noise, label important emails, alert on emails requiring action, draft responses to standard inquiries. Agent handles the 80% of email that doesn't need the human.
- **Value Proposition:** SMB owners lose 96 minutes/day to unproductive tasks — email triage is a large component. Recovering even 30 minutes/day is worth thousands per year.
- **Implementation Notes:** Requires email integration (Gmail API, Mailtrap for testing). Configure AGENTS.md rules for what constitutes noise vs important. Use Sonnet for triage decisions.
- **Dependencies:** Email integration; Gmail API access or equivalent; email labelling rules.

---

### [AUT-006] Reddit/YouTube Digest Cron
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | research-agent
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Daily 8am cron summarising favourite subreddits and YouTube channels. Extracts key posts, new videos, and notable discussions. Delivers a curated digest to Telegram.
- **Value Proposition:** Information consumption without endless scrolling. The agent surfaces the signal, filtering the noise from high-volume communities.
- **Implementation Notes:** Configure a list of subreddits and YouTube channels. Use web_search and web_fetch tools to retrieve new content. Summarise with Sonnet.
- **Dependencies:** web_search; web_fetch; YouTube/Reddit accessible via search.

---

### [AUT-007] Cost Review Cron
- **Category:** automation
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md, universal-openclaw-implementation.md
- **Description:** Weekly Friday cron analysing token spend, comparing to previous weeks, identifying expensive patterns, and alerting if costs exceed thresholds.
- **Value Proposition:** Prevents surprise API bills. Monthly costs can vary 10x between optimised and unoptimised deployments. Weekly monitoring catches runaway patterns early.
- **Implementation Notes:** `openclaw cron add --cron "0 10 * * 5"`. Agent uses `/usage tokens` data or provider billing API to compile spend report. Alert on >20% week-over-week increase.
- **Dependencies:** Provider billing API access or `/usage tokens` data collection.

---

### [AUT-008] Advisor Model Cron (Meta-Oversight)
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 3.5.3)
- **Description:** Every 6 hours, a cheap model (Gemini) reviews today's memory file checking for mistakes, unverified tasks, security concerns, and unfulfilled promises. Appends advisory notes only when issues are found. Read-only except for advisory notes.
- **Value Proposition:** Automated quality control catches errors before they compound. Using a different model as the reviewer provides genuine independent perspective.
- **Implementation Notes:** `openclaw cron add --cron "0 */6 * * *" --model "google/gemini-3.1-pro-preview" --session isolated`. Prompt: "You are the ADVISOR. Read today's memory file. If issues found, append Advisor Notes. If clean, do nothing." Crucial: "can't take actions, only flag."
- **Dependencies:** Google Gemini API key; daily memory files.

---

### [AUT-009] Intel Sweep Cron
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** ops-agent | dev-ops | research-agent
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 3.5 Standard Cron Suite)
- **Description:** Weekly Wednesday 8am cron using Grok-mini to scan X/Twitter, GitHub releases, Reddit, and community channels for OpenClaw updates, security advisories, new community patterns, and competitor movements.
- **Value Proposition:** On 2 Apr 2026, the intel sweep caught v2026.4.1 and 33 security vulnerabilities before they were noticed manually. Pays for itself the first time it catches a breaking change.
- **Implementation Notes:** `openclaw cron add --cron "0 8 * * 3" --model "xai/grok-3-mini" --session isolated`. Write findings to `memory/intel-sweep-latest.md`. If critical findings (security, breaking changes), alert the user immediately.
- **Dependencies:** xAI API key for Grok; x_search tool; web_search.

---

### [AUT-010] Automated Weekly Shopping
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** personal-assistant
- **Status:** catalogued
- **Source:** power-user-patterns.md (r/openclaw community use case), community-use-cases.md
- **Description:** Agent accesses grocery store account via browser, syncs with shared shopping list (Todoist), adds items to basket, applies substitutions, checks delivery slots, and confirms the order.
- **Value Proposition:** Eliminates the weekly grocery ordering task entirely. Works while you sleep.
- **Implementation Notes:** Browser tool with authenticated grocery store profile. Connect Todoist via API or browser. Schedule as Friday night cron. Handle edge cases (out-of-stock, substitutions).
- **Dependencies:** Browser automation; grocery store account; Todoist or equivalent list app.

---

### [AUT-011] Client Website Management via Chat
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** dev-ops | ops-agent
- **Status:** catalogued
- **Source:** power-user-patterns.md, community-use-cases.md (@ad_astra999)
- **Description:** Client sends voice message requesting a website change → agent transcribes → spins up coding agent → pushes test branch → sends preview link → on approval, deploys. Support emails auto-generate change reports.
- **Value Proposition:** Eliminates the technical barrier for client-initiated site changes. The client just describes what they want; the full dev pipeline happens automatically.
- **Implementation Notes:** Voice message → Whisper STT → coding agent (ACP) → git push test branch → preview URL → Telegram approval button → deploy. Requires Whisper STT and ACP coding agent integration.
- **Dependencies:** Voice STT; ACP coding agent; git deployment pipeline; preview environment.

---

### [AUT-012] Google Review Auto-Response
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** hospitality | customer-service | education | personal-assistant
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (Tier 1 Restaurants), community-use-cases.md
- **Description:** AI drafts personalised responses to every Google (and TripAdvisor) review. Positive reviews get warm thank-yous with menu/service mentions. Negative reviews get empathetic responses plus an owner alert.
- **Value Proposition:** One Reddit restaurant owner automated this and went from unranked to #1 on Google Places. Competitors charge $100-200/mo just for this feature (Reviewly, RepliFast). 88% review response rate correlates with higher bookings.
- **Implementation Notes:** Google Business Profile API for review access. Configure response templates per sentiment category. Human approval flow for negative reviews. Alert owner on 1-2 star reviews.
- **Dependencies:** Google Business Profile API; channel for owner alerts.

---

### [AUT-013] WhatsApp Reservation/Booking Handler
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** hospitality | customer-service | education
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md, community-use-cases.md
- **Description:** Customers WhatsApp to book, change, or cancel. AI checks availability, confirms, sends reminders 24h before. Eliminates phone tag during busy service hours.
- **Value Proposition:** Restaurants and salons see 30-50% no-show reduction with automated reminders. Zero staff time for booking management.
- **Implementation Notes:** WhatsApp Business API via WAHA or 360dialog. Connect to calendar/booking system. Configure confirmation templates. Set up reminder cron at -48h and -24h.
- **Dependencies:** WhatsApp Business API; calendar/booking system integration; WAHA or 360dialog.

---

### [AUT-014] Appointment Reminder Automation
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** customer-service | hospitality | education | finance
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (universal pattern), community-use-cases.md
- **Description:** Automated 48h + 24h reminders via WhatsApp for appointments. Dental practice case study: 50% no-show reduction. Each prevented no-show = €100-300 recovered revenue.
- **Value Proposition:** "15 no-shows/week × €100 = €78,000/year. Cut that in half = €39,000 saved annually." The most direct ROI calculation in the consultancy.
- **Implementation Notes:** Cron with appointment data source. Templates per appointment type. One-tap confirm/reschedule response. No-show follow-up 1h after missed slot ("We missed you, want to rebook?").
- **Dependencies:** Booking/appointment data source; WhatsApp Business API; calendar integration.

---

### [AUT-015] No-Show Follow-Up Automation
- **Category:** automation
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** customer-service | education | hospitality
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (Salons/Barbers), community-use-cases.md
- **Description:** 1 hour after a missed appointment, send a friendly "We missed you! Want to rebook?" via WhatsApp. Recovers approximately 20% of lost appointments passively.
- **Value Proposition:** Passive revenue recovery with minimal setup. A salon with 10 no-shows per week recovering 20% = 2 extra bookings/week without any staff effort.
- **Implementation Notes:** Trigger from missed appointment event. Configure timing (1 hour post-slot). Warm, non-accusatory template. Track rebooking rate in vault/business/.
- **Dependencies:** Appointment system with missed-appointment detection; WhatsApp API.

---

### [AUT-016] Quote Follow-Up Automation (Trades)
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** ops-agent | sales-agent | customer-service
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (Trades)
- **Description:** Automatic follow-up 48 hours after quote sent, then 7 days. "Hi Sarah, just checking if you had any questions about the quote for the bathroom refit?" Converts fence-sitters with minimal effort.
- **Value Proposition:** Tradespeople rarely follow up on quotes. Adding automated follow-up can convert 15-25% of non-responding quotes.
- **Implementation Notes:** Trigger on quote creation event. Store quote details in vault. Schedule follow-up crons at +48h and +7 days. Stop sequence if booking confirmed.
- **Dependencies:** Quote tracking system; customer contact data; WhatsApp/SMS channel.

---

### [AUT-017] Invoice Payment Reminders
- **Category:** automation
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** ops-agent | finance
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (Trades, Accountants)
- **Description:** Escalating payment reminders: friendly at 1 day overdue, firmer at 7 days, "please contact us" at 14 days. Via WhatsApp (98% read rate vs email's 20%).
- **Value Proposition:** WhatsApp messages are read. Email reminders are ignored. Switching channels dramatically improves collection rates.
- **Implementation Notes:** Connect to invoicing system (Wave, Xero, etc.) via API or browser automation. Trigger on overdue flag. Escalating templates per day-overdue threshold.
- **Dependencies:** Invoicing system integration; WhatsApp API; customer phone numbers.

---

### [AUT-018] Daily Specials Broadcaster
- **Category:** automation
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** hospitality | customer-service
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (Restaurants)
- **Description:** Owner sends a voice note or photo of today's specials → AI formats and posts to WhatsApp broadcast list, Instagram, Facebook, and Google Business Profile simultaneously.
- **Value Proposition:** Consistent social presence without hiring a content manager. Owner just needs to speak or photograph.
- **Implementation Notes:** Voice → Whisper STT → content generation → multi-channel post. Requires WhatsApp Business API, Instagram Graph API, Facebook API, Google Business Profile API. Format templates per platform.
- **Dependencies:** Whisper STT; social media APIs; WhatsApp Business API.

---

### [AUT-019] Lead Qualification Bot
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** sales-agent | customer-service | real-estate
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (Real Estate), community-use-cases.md
- **Description:** Website/WhatsApp inquiries get immediate response with qualifying questions: budget, timeline, requirements. Qualifies leads before the agent ever picks up the phone.
- **Value Proposition:** Agent only speaks to pre-qualified leads. Time saved on unqualified inquiries repaid many times over on converted leads.
- **Implementation Notes:** Configure qualifying question sequence in AGENTS.md. Score leads based on responses (budget range, decision timeline, specific needs). Route qualified leads to human; handle unqualified autonomously.
- **Dependencies:** WhatsApp/web chat integration; lead scoring criteria; CRM for storage.

---

### [AUT-020] Document Collection Chaser (Accountants)
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** finance | ops-agent
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (Accountants)
- **Description:** "Hi Mike, just a reminder we still need your P60 and bank statements for year-end. Can you upload them here?" Automated, escalating reminders starting November for January deadlines. Tracks per-client document status.
- **Value Proposition:** Eliminates the January hell of chasing clients for documents. Starting automated chasing in November converts a crisis into a managed process.
- **Implementation Notes:** Client document checklist in vault per client. Cron schedule starting 60 days before deadline. Escalating templates. Mark documents as received on upload confirmation.
- **Dependencies:** Per-client document tracking; WhatsApp API; document upload workflow.

---

### [AUT-021] Email Triage + Autonomous Inbox Management
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | ops-agent
- **Status:** catalogued
- **Source:** community-use-cases.md (Daimon Legal, TechNickAI), power-user-patterns.md
- **Description:** Autonomous inbox triage — archive noise, label important, alert on time-sensitive, auto-draft responses to standard types. Human approval gate for sending.
- **Value Proposition:** The #1 time suck for professionals. Recovering 30-60 minutes/day on email management = enormous productivity gain.
- **Implementation Notes:** Integrate with Gmail API or similar. Define triage rules (noise = newsletters, marketing; important = client names, action words). Human approval for all outbound emails.
- **Dependencies:** Email API; triage rules; human approval flow.

---

### [AUT-022] Bookkeeping Automation (Invoice → Accountant)
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** finance | ops-agent
- **Status:** catalogued
- **Source:** community-use-cases.md (Codebridge), power-user-patterns.md
- **Description:** Agent monitors email for invoices, identifies them, parses PDFs (extracting vendor, amount, date, category), and prepares structured data for accountant. Also: Zoho Books browser automation for logging transactions.
- **Value Proposition:** Eliminates manual bookkeeping data entry. Turns a 4-hour weekly task into an automated background process.
- **Implementation Notes:** Email monitoring for PDF attachments. PDF parsing with vision model. Browser automation for Zoho Books or Wave. Human review before finalisation.
- **Dependencies:** Email integration; PDF vision model; Zoho Books/Wave access.

---

### [AUT-023] LinkedIn Prospecting Automation (BeReach)
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** sales-agent
- **Status:** catalogued
- **Source:** community-use-cases.md (BeReach skill, r/openclaw)
- **Description:** Intent signal detection from LinkedIn feed, lead scoring against ICP, conversation handling from connection request to booked demo, warm-up and rate limiting for account safety.
- **Value Proposition:** End-to-end LinkedIn prospecting without manual work. Rate limiting prevents account ban.
- **Implementation Notes:** Install BeReach skill from ClawHub. Configure ICP criteria in vault. Set rate limits to avoid LinkedIn detection. Human review gate before booking demos.
- **Dependencies:** BeReach skill; LinkedIn account; ICP definition; CRM for lead storage.

---

### [AUT-024] 24/7 Sales Outreach Automation
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** sales-agent
- **Status:** catalogued
- **Source:** community-use-cases.md (@krishlogy, CRM integrations)
- **Description:** Data prep, research, email writing, email sending, flagging out-of-office/unsubscribes, helping sales team close. Full end-to-end outreach pipeline running around the clock.
- **Value Proposition:** Sales team focuses on closing while automation handles the top of the funnel. Scales outreach without headcount.
- **Implementation Notes:** CRM + LinkedIn Sales Navigator + HunterIO integration. Personalised email generation. Bounce/OOO/unsubscribe handling. Human takeover trigger on engaged leads.
- **Dependencies:** CRM (HubSpot or similar); email sending infrastructure; LinkedIn API access.

---

### [AUT-025] TikTok Marketing Pipeline
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** content-creator | sales-agent
- **Status:** catalogued
- **Source:** community-use-cases.md (r/LocalLLM — 1.2M views/week, $670/mo MRR)
- **Description:** Automated TikTok marketing pipeline generating 1.2M views/week and $670/month MRR from a community deployment. Full pipeline from content idea → script → post scheduling.
- **Value Proposition:** Proven community result: $670/mo MRR with 1.2M weekly views. Content marketing at scale without a social media team.
- **Implementation Notes:** Research the Reddit post at r/LocalLLM for implementation details. Key components: trend monitoring, script generation, scheduling, performance tracking.
- **Dependencies:** TikTok API access; content generation pipeline; video creation tools.

---

### [AUT-026] Podcast Production Pipeline
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** content-creator
- **Status:** catalogued
- **Source:** community-use-cases.md (awesome-openclaw-usecases)
- **Description:** Guest research, episode outlines, show notes generation, social media promotion posts — from topic selection to publish-ready assets.
- **Value Proposition:** Podcast production is highly time-intensive. Automating research, notes, and promotion frees the host for the actual recording.
- **Implementation Notes:** Pipeline: topic → web_search for guest research → outline generation → recording (human step) → transcript → show notes → social posts. Deliver all assets to Telegram on completion.
- **Dependencies:** Web search; transcript processing; social media API access.

---

### [AUT-027] Video Editing via Natural Language
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** content-creator
- **Status:** catalogued
- **Source:** community-use-cases.md (awesome-openclaw-usecases)
- **Description:** Video editing by natural language description — trim, merge, add music, subtitles, colour grade, crop to vertical. Agent translates instructions to ffmpeg commands.
- **Value Proposition:** Non-technical content creators can edit videos via chat. "Trim the first 30 seconds, add captions, export as vertical" becomes a single message.
- **Implementation Notes:** ffmpeg for video processing. Agent generates ffmpeg commands from natural language. video-frames skill available for frame extraction. Preview before finalising.
- **Dependencies:** ffmpeg installed; video files accessible; sufficient disk space.

---

### [AUT-028] Review Response Pipeline (Draft → Review → Approve)
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** hospitality | customer-service
- **Status:** catalogued
- **Source:** multi-agent-coordination-playbook.md (Kilmurry proposed workflows)
- **Description:** Two-agent pipeline for hotel/business review responses. Sonnet drafts response → Opus quality-checks negative reviews only → delivers to owner for approval. Positive reviews go straight to owner with Sonnet draft.
- **Value Proposition:** High-quality review responses without the full cost of running Opus on every response. Opus only engages on negative reviews where it matters most.
- **Implementation Notes:** Sequential handoff pattern (ARC-010). Sonnet drafts → saves to `drafts/review-response-{id}.md` → Opus reads and reviews negative only → delivers approved drafts to owner via Telegram.
- **Dependencies:** Review monitoring (AUT-012); multi-agent coordination (ARC-010); Opus API access.

---

### [AUT-029] n8n Workflow Generation via Chat
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | dev-ops
- **Status:** catalogued
- **Source:** community-use-cases.md (r/n8n — production n8n workflow via WhatsApp)
- **Description:** Text description → WhatsApp → OpenClaw agent generates and deploys production-ready n8n workflow automatically. Agent understands n8n-as-code CLI.
- **Value Proposition:** Non-technical users can describe an automation and the agent builds it in n8n. Dramatically reduces the barrier to workflow automation.
- **Implementation Notes:** Requires n8n CLI access. Agent generates n8n JSON configuration from natural language, validates, and deploys. Requires deep n8n integration.
- **Dependencies:** n8n installation; n8n CLI; OpenClaw + n8n stack (INT-001).

---

### [AUT-030] Parent/Regular Customer Nudges
- **Category:** automation
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** customer-service | education | hospitality
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (Salons — "Your Appointment is Due" pattern)
- **Description:** Track when regular customers are overdue for their usual service (6-week haircut, monthly facial, quarterly review). Send personalised nudge at the right time. Passive rebooking engine.
- **Value Proposition:** "You have 200 regular clients. 30% forget to rebook. What if they all got a friendly nudge at exactly the right time?" Direct revenue recovery with no staff effort.
- **Implementation Notes:** Track last visit date per customer in vault/customers/. Schedule cron to check and identify overdue customers. Personalised message referencing their usual service.
- **Dependencies:** Customer visit history; WhatsApp API; vault/customers/ data.

---

### [AUT-031] Competitive Intel Sweep (Multi-Agent Fan-Out)
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** hospitality | retail | ops-agent
- **Status:** catalogued
- **Source:** multi-agent-coordination-playbook.md (Kilmurry proposed workflows)
- **Description:** Weekly fan-out pattern: Scout A scrapes competitor prices, Scout B scrapes competitor reviews, Main agent merges and analyses. Price comparison + sentiment comparison + recommendations delivered as weekly competitive report.
- **Value Proposition:** Continuous competitive intelligence without a competitive intelligence team. Catches pricing gaps and sentiment trends before they affect bookings.
- **Implementation Notes:** Fan-out variant (ARC-011). Three cron jobs: ScoutA (Sunday 6am), ScoutB (Sunday 6:05am), Main (Sunday 6:15am). Each writes to intel-drops/. Main reads both files and synthesises.
- **Dependencies:** Multi-agent coordination (ARC-010); browser for competitor site access; intel-drops folder.

---

### [AUT-032] Membership Renewal Reminders
- **Category:** automation
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** customer-service | education
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (Gyms/Fitness Studios)
- **Description:** 30 days before membership expiry: "Your membership renews on April 15th. Want to continue or discuss options?" Reduces churn by prompting renewal before lapse.
- **Value Proposition:** Reducing membership churn by even 10% has compounding effects on MRR. Automated reminders capture renewals that would otherwise silently lapse.
- **Implementation Notes:** Connect to membership management system. Query for members expiring in 14-30 days. Personalised template with renewal link or response option.
- **Dependencies:** Membership system integration; WhatsApp API.

---

### [AUT-033] Back-in-Stock Notifications
- **Category:** automation
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** customer-service | retail
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (Retail Shops)
- **Description:** When a customer asks about an out-of-stock item, log their interest. When stock is replenished, automatically notify all interested customers via WhatsApp.
- **Value Proposition:** Converts interested-but-couldn't-buy into sales without any staff effort. Also signals high-demand items for reorder planning.
- **Implementation Notes:** Store interest in vault/customers/. Monitor inventory system for stock updates. Trigger notification on stock restore event.
- **Dependencies:** Inventory system integration; customer contact data; WhatsApp API.

---

### [AUT-034] Automated Bidding Workflow
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | finance
- **Status:** catalogued
- **Source:** community-use-cases.md (@CryptoBababooey — procurement/sales)
- **Description:** Client bid received → review specs → identify vendors by trust score → send for approval → email vendors → collect costs → calculate margins → deliver final bid. End-to-end procurement automation.
- **Value Proposition:** Compresses a multi-day procurement workflow to hours. Vendor trust scoring ensures quality while automation handles the coordination.
- **Implementation Notes:** Structured handoff between stages. Human approval gate before emailing vendors. Margin calculation in vault/financial/. Email integration for vendor outreach.
- **Dependencies:** Vendor database with trust scores; email integration; approval workflow.

---

### [AUT-035] CRM Migration Automation
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | sales-agent
- **Status:** catalogued
- **Source:** community-use-cases.md (@BadBrainCode — 1,500 contacts migrated)
- **Description:** Migrated 1,500 contacts, 200 proposals, and metadata between CRMs using headless browsing and custom scripts. Saved hundreds of hours over manual data migration.
- **Value Proposition:** CRM migrations are a common pain point for growing businesses. A bespoke automation saves 100+ hours vs manual data entry.
- **Implementation Notes:** Browser automation for source CRM export. Custom scripts for data transformation. Browser automation for target CRM import. Verify data integrity post-migration.
- **Dependencies:** Browser automation; access to both CRM systems; transformation mapping.

---

### [AUT-036] Inactive Patient/Client Recovery
- **Category:** automation
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** customer-service | education | hospitality
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md (Medical/Dental — "Inactive Patient Recovery")
- **Description:** Identify patients/clients overdue for their scheduled check-up or service and send personalised re-engagement messages. Works for dental (6/12-month check-ups), salons (6-week cycles), gyms (lapsed memberships).
- **Value Proposition:** Passive revenue recovery from the existing customer base. Much cheaper to reactivate a lapsed customer than acquire a new one.
- **Implementation Notes:** Query customer database for last visit date. Filter by appropriate overdue threshold (e.g., >8 months for annual dental check-up). Personalised templates referencing their history.
- **Dependencies:** Customer history data; WhatsApp API.

---

### [AUT-037] Autonomous Business Builder (Nat Eliason Pattern)
- **Category:** automation
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | content-creator | sales-agent
- **Status:** catalogued
- **Source:** community-use-cases.md (Nat Eliason — "Felix" agent, $14,718 in ~3 weeks)
- **Description:** Agent ("Felix") given a budget and brief to autonomously build a business. Launched website, info product, X account. Made $14,718 in ~3 weeks. Uses 3-layer memory, multi-threaded chats, security best practices.
- **Value Proposition:** Proof-of-concept for fully autonomous business operations. Demonstrates the ceiling of what's possible. Useful as a reference case study for clients.
- **Implementation Notes:** Review the creatoreconomy.so post and YouTube tutorial. Key: 3-layer memory system, multi-threaded chat approach, clear business brief. Not for first deployments — requires mature agent setup.
- **Dependencies:** Full agent stack; multiple channels; financial tool integration; high trust level.

---

## INTEGRATION

---

### [INT-001] OpenClaw + n8n (Killer Combo)
- **Category:** integration
- **Complexity:** major (4+ hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md (most popular integration pattern)
- **Description:** OpenClaw handles reasoning (intent parsing, decision-making, NLU); n8n handles execution (API calls, webhooks, data transformation, multi-step workflows). Agent never touches credentials — n8n manages all API keys. Integrations are visual and lockable in n8n.
- **Value Proposition:** Separates AI reasoning from integration plumbing. Each does what it does best. n8n's visual workflow editor makes integrations manageable by non-developers.
- **Implementation Notes:** Start with the openclaw-n8n-stack Docker compose (caprihan/openclaw-n8n-stack on GitHub). Common patterns: email triage → n8n webhook → auto-reply/Slack/CRM. Meeting transcript → n8n creates Jira/Linear/Todoist tasks.
- **Dependencies:** n8n installation; Docker (for stack); relevant API credentials in n8n.

---

### [INT-002] CRM Integrations (FollowUpBoss, HubSpot, Asana)
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** sales-agent | ops-agent | real-estate
- **Status:** catalogued
- **Source:** power-user-patterns.md, community-use-cases.md
- **Description:** Connect OpenClaw to CRM systems for contacts, deals, and pipeline management. FollowUpBoss for real estate, HubSpot for B2B sales, Asana for task and project management via MCP.
- **Value Proposition:** Agent can create leads, update deal stages, log activities, and query pipeline — all via natural language in Telegram.
- **Implementation Notes:** Use MCP integrations where available (Asana MCP). For others, use n8n as the integration layer (INT-001). DenchClaw provides a fully local CRM using DuckDB for zero third-party dependency.
- **Dependencies:** CRM API access; MCP or n8n integration layer.

---

### [INT-003] Email Integration (Gmail API / gog CLI)
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | ops-agent | customer-service
- **Status:** catalogued
- **Source:** power-user-patterns.md, community-use-cases.md
- **Description:** Connect OpenClaw to email via Gmail API or gog CLI for reading, labelling, drafting, and sending emails. Foundation for email triage (AUT-005) and inbox management (AUT-021).
- **Value Proposition:** Email is the primary business communication channel. Without email integration, the agent can't participate in the most important workflow.
- **Implementation Notes:** Gmail API via OAuth. Configure scopes carefully (least privilege). Use Mailtrap (INT-004) for testing. Never connect to corporate email without explicit approval.
- **Dependencies:** Gmail API credentials; OAuth flow; Mailtrap for testing.

---

### [INT-004] Mailtrap Email Sandbox
- **Category:** integration
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** ops-agent | customer-service
- **Status:** catalogued
- **Source:** power-user-patterns.md, community-use-cases.md (Daimon Legal)
- **Description:** Email sandbox for testing email-sending functionality safely. All emails go to a virtual inbox, not real recipients. Essential for testing email automations before going live.
- **Value Proposition:** Prevents accidental emails to real customers during development. The Daimon Legal deployment uses this as a standard safety practice.
- **Implementation Notes:** Register at Mailtrap.io. Point email-sending integrations at Mailtrap SMTP during development. Switch to production SMTP only after thorough testing.
- **Dependencies:** Mailtrap account; email integration.

---

### [INT-005] Calendar Integration (Google Calendar / Family Calendar Hub)
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | ops-agent
- **Status:** catalogued
- **Source:** power-user-patterns.md, community-use-cases.md
- **Description:** Connect to Google Calendar (and other calendar sources) for the Calendar Steward workflow: daily briefings with travel time, meeting prep, conflict detection. Family Calendar Hub: aggregate all family calendars, morning briefings, monitor for new appointments.
- **Value Proposition:** Calendar context transforms morning briefings from generic to genuinely useful. Agent can pre-research meeting attendees and flag schedule conflicts before they happen.
- **Implementation Notes:** Google Calendar API via OAuth. Configure read access initially; write access only with explicit approval gate. Family Calendar Hub: each family member shares their calendar, agent aggregates.
- **Dependencies:** Google Calendar API credentials; OAuth flow.

---

### [INT-006] WhatsApp Business API (WAHA / 360dialog)
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** customer-service | hospitality | education | universal
- **Status:** catalogued
- **Source:** community-use-cases.md, easy-wins-by-industry.md
- **Description:** WhatsApp Business API integration via WAHA (self-hosted) or 360dialog (managed). Enables bi-directional WhatsApp messaging for customer-facing bots. Used for booking, reminders, FAQ, and review management.
- **Value Proposition:** WhatsApp has 98% message read rate vs 20% for email. Customer-facing automations on WhatsApp dramatically outperform email equivalents.
- **Implementation Notes:** WAHA for self-hosted (cost savings, data control); 360dialog for managed (easier setup, less maintenance). Configure webhook to receive messages, API for sending. Test with Mailtrap equivalent.
- **Dependencies:** WhatsApp Business account; WAHA server or 360dialog account; phone number.

---

### [INT-007] Shopify MCP Integration (via Composio)
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** retail | sales-agent
- **Status:** catalogued
- **Source:** community-use-cases.md (Composio — Shopify MCP + OpenClaw)
- **Description:** Shopify integration via Composio's MCP toolkit. Enables product management, order tracking, inventory monitoring, price changes, and customer service for Shopify stores.
- **Value Proposition:** Agent can handle "Is item X in stock?" "What's the status of order #12345?" "Alert me when product Y drops below 5 units" — all common e-commerce support queries.
- **Implementation Notes:** Install Composio Shopify MCP. Configure Shopify API credentials via Composio (agents never touch credentials directly). Map common queries to Shopify API calls.
- **Dependencies:** Shopify store; Composio account; Shopify API key.

---

### [INT-008] Home Assistant Smart Home Integration
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant
- **Status:** catalogued
- **Source:** power-user-patterns.md, ecosystem-state-march2026.md
- **Description:** OpenClaw integration with Home Assistant for smart home control via natural language. Available as a ClawHub skill. Control lights, locks, thermostats, etc. via Telegram.
- **Value Proposition:** "Turn off all lights before I leave" or "Is the back door locked?" via Telegram. Natural language smart home control.
- **Implementation Notes:** Install Home Assistant skill from ClawHub. Configure Home Assistant webhook or REST API access. Set up entity mappings for common commands.
- **Dependencies:** Home Assistant setup; ClawHub skill; Home Assistant API access.

---

### [INT-009] Voice Call Stack (ElevenLabs + Vapi + Twilio)
- **Category:** integration
- **Complexity:** major (4+ hours)
- **Use Case Tags:** customer-service | hospitality | personal-assistant
- **Status:** catalogued
- **Source:** power-user-patterns.md (Section 10), community-use-cases.md
- **Description:** Full voice call integration: ElevenLabs for custom TTS voice synthesis, Vapi for call management (STT, TTS, turn-taking, phone calls), Twilio for real inbound/outbound phone numbers.
- **Value Proposition:** Phone-based customer service, dinner reservations, after-hours support. The single most differentiated capability most consultants don't offer.
- **Implementation Notes:** Enable chatCompletions endpoint → ngrok/reverse proxy → ElevenLabs/Vapi configuration → Twilio phone number. Test with soft-phone before going live.
- **Dependencies:** ElevenLabs account; Vapi account; Twilio account; public endpoint.

---

### [INT-010] FHIR / Epic Health Data Integration
- **Category:** integration
- **Complexity:** major (4+ hours)
- **Use Case Tags:** personal-assistant
- **Status:** catalogued
- **Source:** community-use-cases.md (Substack — OpenClaw Meets Healthcare)
- **Description:** FHIR data integration for personal health workflow orchestration. Epic health data download for patient timeline analysis. Stored behind HIPAA-compliant GCP database to bypass EHR system limitations.
- **Value Proposition:** Physicians can query their own patient records via natural language. "What were John's last three glucose readings?" bypasses the cumbersome EHR interface.
- **Implementation Notes:** FHIR API for health data access. GCP Cloud SQL for HIPAA-compliant storage. Agent queries structured health data on demand. Strict data access controls required.
- **Dependencies:** FHIR API access; GCP account; HIPAA compliance setup; medical context.

---

### [INT-011] Apple Health / Garmin Connect Integration
- **Category:** integration
- **Complexity:** major (4+ hours)
- **Use Case Tags:** personal-assistant
- **Status:** catalogued
- **Source:** community-use-cases.md (multiple X users), easy-wins-by-industry.md
- **Description:** Integration with Apple Health and Garmin Connect for fitness data: glucose, activity, sleep (EightSleep), gym performance. Vision model for food photo calorie tracking.
- **Value Proposition:** Personal health intelligence — "How has my sleep affected my workout performance?" becomes a real question the agent can answer.
- **Implementation Notes:** Apple Health export (XML) or HealthKit API. Garmin Connect API. Store in vault/health/. Vision model for food photo analysis. Scheduled health briefings.
- **Dependencies:** Apple Health/Garmin API access; vault structure; vision model for food photos.

---

### [INT-012] ACP / ACPX Agent Orchestration Protocol
- **Category:** integration
- **Complexity:** major (4+ hours)
- **Use Case Tags:** dev-ops | ops-agent
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (Section 5), power-user-patterns.md
- **Description:** ACP (Agent Communication Protocol) lets OpenClaw orchestrate external coding agents (Codex, Claude Code, Gemini CLI, OpenCode, Pi, Kimi) through a structured protocol. ACPX is the headless CLI client. Agents elevated to first-class runtimes in v2026.2.26.
- **Value Proposition:** Coding team orchestration — one interface for all agents. ACP provides structure vs PTY scraping which is fragile and debug-unfriendly.
- **Implementation Notes:** Install `openclaw/acpx` from GitHub. Configure target agents. Use `sessions_spawn` for thread creation. Current-conversation binds available for Discord, BlueBubbles, iMessage (v2026.3.28).
- **Dependencies:** ACPX installed; compatible coding agent; v2026.2.26+.

---

### [INT-013] Accounting Software Integration (Wave, Zoho Books)
- **Category:** integration
- **Complexity:** major (4+ hours)
- **Use Case Tags:** finance | ops-agent
- **Status:** catalogued
- **Source:** community-use-cases.md (NYC Claw Wave integration, accounting discussion)
- **Description:** Integration with Wave (via API) and Zoho Books (via browser automation) for logging transactions, recording asset purchases, depreciation, bank statement uploads, and reconciliation.
- **Value Proposition:** Automates the daily bookkeeping grind. Agent processes transactions while the accountant reviews summaries.
- **Implementation Notes:** Wave has a public API. Zoho Books requires browser automation. Build transaction log in vault/financial/. Human review gate before posting.
- **Dependencies:** Wave or Zoho Books account; API credentials or browser automation setup.

---

### [INT-014] Microsoft Teams Integration
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** ops-agent | customer-service
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (v2026.3.24 Teams overhaul), power-user-patterns.md
- **Description:** Microsoft Teams integration via Bot Framework SDK. Major overhaul in v2026.3.24 makes it production-ready. Enables OpenClaw deployment in enterprise Teams environments with file upload support.
- **Value Proposition:** SMEs using Teams as their primary comms channel can have OpenClaw natively integrated. No Telegram setup required.
- **Implementation Notes:** Configure Teams Bot Framework credentials. Channel configuration in openclaw.json. File upload via new `upload-file` action (v2026.3.28). Test in dev Teams workspace before production.
- **Dependencies:** Microsoft Teams account; Bot Framework credentials; v2026.3.24+.

---

### [INT-015] Tencent WeChat Integration
- **Category:** integration
- **Complexity:** major (4+ hours)
- **Use Case Tags:** customer-service | ops-agent
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (Tencent March 2026)
- **Description:** WeChat integration via Tencent iLink Bot (plugin-based). Tencent launched a full suite of OpenClaw-compatible AI products integrated with WeChat in March 2026.
- **Value Proposition:** Access to WeChat's 1.3 billion monthly active users. Critical for any business with Chinese market presence or Chinese-speaking customer base.
- **Implementation Notes:** Install WeChat plugin. Configure via Tencent iLink Bot framework. Follow Tencent's documentation for OpenClaw-compatible integration.
- **Dependencies:** WeChat Business account; Tencent developer account; WeChat plugin.

---

### [INT-016] DenchClaw — Local CRM with DuckDB
- **Category:** integration
- **Complexity:** major (4+ hours)
- **Use Case Tags:** sales-agent | ops-agent
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** DenchClaw turns OpenClaw into a fully local CRM and sales automation platform using DuckDB as the backend. No third-party CRM subscription required.
- **Value Proposition:** Zero SaaS subscription cost for CRM. Data sovereignty — all customer data stays on your infrastructure. DuckDB provides fast analytical queries over customer data.
- **Implementation Notes:** Install DenchClaw. Configure DuckDB data store. Build customer, deal, and pipeline schemas. Connect to communication channels for automatic interaction logging.
- **Dependencies:** DenchClaw installation; DuckDB; data schema design.

---

### [INT-017] GitHub / Vercel / Netlify Dev Integration
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** dev-ops
- **Status:** catalogued
- **Source:** community-use-cases.md, ecosystem-state-march2026.md
- **Description:** Integration with GitHub (PRs, issues, CI/CD), Vercel (preview deployments), and Netlify (deploy hooks). Agent can review PRs, trigger deployments, and manage the development lifecycle via chat.
- **Value Proposition:** Development workflow management via Telegram. "Deploy the staging branch" or "What PRs are pending review?" become natural language commands.
- **Implementation Notes:** GitHub MCP for PR/issue management. Vercel/Netlify webhook triggers via n8n or direct API calls. Deploy notifications back to Telegram.
- **Dependencies:** GitHub/Vercel/Netlify API keys; n8n or direct API access.

---

### [INT-018] SecretRef (64+ Credential Targets)
- **Category:** integration
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (v2026.3.2)
- **Description:** SecretRef supports 64 credential targets (Stripe, Slack, GitHub, etc.) with fail-fast on unresolved refs. Prevents wasted tokens on failed credential lookups — if a secret isn't configured, the tool call fails immediately rather than burning tokens on a doomed request.
- **Value Proposition:** Clean credential management with immediate failure feedback. Saves tokens and debugging time when integrations are misconfigured.
- **Implementation Notes:** Configure via `openclaw secrets`. Map each integration's credential to a SecretRef target. Unresolved refs fail fast rather than silently passing null/empty values.
- **Dependencies:** v2026.3.2+; credentials for target services.

---

### [INT-019] Google Business Profile API (Review Monitoring)
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** hospitality | customer-service | education
- **Status:** catalogued
- **Source:** easy-wins-by-industry.md, community-use-cases.md
- **Description:** Google Business Profile API for monitoring new reviews, responding to reviews, and tracking rating changes. Foundation for the review auto-response automation (AUT-012).
- **Value Proposition:** Hotels with >50% review response rate see significantly higher booking rates. Automated monitoring ensures no review goes unanswered.
- **Implementation Notes:** Google Business Profile API credentials. OAuth flow. Configure webhook or polling cron for new reviews. Feed into AUT-012 response pipeline.
- **Dependencies:** Google Business Profile API access; OAuth credentials.

---

### [INT-020] Instagram Graph API / Meta Business Suite
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** customer-service | content-creator | hospitality
- **Status:** catalogued
- **Source:** community-use-cases.md (Multi-Channel Customer Service)
- **Description:** Instagram DM management via Meta Business Suite/Graph API. Part of the unified multi-channel customer service inbox alongside WhatsApp, Gmail, and Google Reviews.
- **Value Proposition:** Restaurant case study: response time dropped from 4+ hours to under 2 minutes, handling 80% of inquiries automatically across all channels including Instagram.
- **Implementation Notes:** Meta Business Suite API credentials. Configure webhook for new DMs. Route to agent for triage and auto-response. Requires Meta app review for production.
- **Dependencies:** Meta Business Suite account; API credentials; app review approval.

---

### [INT-021] Todoist / Jira / Linear Task Management
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** ops-agent | dev-ops | personal-assistant
- **Status:** catalogued
- **Source:** power-user-patterns.md, community-use-cases.md
- **Description:** Task management integration for creating, updating, and querying tasks via natural language. Meeting transcripts auto-create Jira/Linear/Todoist tasks assigned to the right person.
- **Value Proposition:** Eliminates manual task creation from meetings and conversations. Agent handles the admin; humans handle the work.
- **Implementation Notes:** Todoist API, Jira REST API, or Linear GraphQL API via n8n or direct MCP. Configure task creation templates per context (meeting → Jira story, personal → Todoist task).
- **Dependencies:** Task management API credentials; n8n (INT-001) or MCP integration.

---

### [INT-022] Spotify / Media Playback Control
- **Category:** integration
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** personal-assistant
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (ClawHub skills)
- **Description:** Spotify playback control via ClawHub skill. Play, pause, skip, queue tracks, and get recommendations via natural language in Telegram.
- **Value Proposition:** Quality-of-life personal assistant feature. "Play something chill" via Telegram while working.
- **Implementation Notes:** Install Spotify skill from ClawHub. Configure Spotify API credentials (OAuth). Vet skill source code before installation (SEC-008).
- **Dependencies:** Spotify Premium account; ClawHub skill; Spotify API credentials.

---

### [INT-023] OpenClaw Android App (Mobile Companion)
- **Category:** integration
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | ops-agent
- **Status:** catalogued
- **Source:** power-user-patterns.md (AidanPark/openclaw-android), ecosystem-state-march2026.md
- **Description:** Run OpenClaw on Android without proot or Linux. Also: companion app for iOS/macOS. Enables mobile management and direct interaction with the agent from phone.
- **Value Proposition:** Mobile-native agent interaction without relying solely on Telegram/WhatsApp. Direct access to agent capabilities from the phone.
- **Implementation Notes:** Install from AidanPark/openclaw-android on GitHub. Connect to gateway via Tailscale or direct network access. v2026.2.26 added official Android support.
- **Dependencies:** Android device; OpenClaw gateway running and accessible.

---

### [INT-024] Multi-Language Detection (ES/EN/UA)
- **Category:** integration
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** customer-service | hospitality
- **Status:** catalogued
- **Source:** community-use-cases.md (Multi-Channel Customer Service)
- **Description:** Automatic language detection for customer messages, with responses in the detected language. The multi-channel customer service deployment supports ES/EN/UA natively.
- **Value Proposition:** Serve multilingual customer bases without separate agents per language. One agent handles all languages, routing to the right response template.
- **Implementation Notes:** Claude and GPT models handle multilingual natively. Configure SOUL.md: "Detect the customer's language and respond in the same language." Add language-specific templates for common responses.
- **Dependencies:** Multilingual model (Claude/GPT); language-aware response templates.

---

### [INT-025] Vibe-Coded Lead Gen Tool (Google Maps Scraper)
- **Category:** integration
- **Complexity:** major (4+ hours)
- **Use Case Tags:** sales-agent | ops-agent
- **Status:** catalogued
- **Source:** twitter-research-2026-04-05.md (348K views)
- **Description:** Google Maps scraper → review analysis → cold email generation pipeline. Built with Claude Code in 2 weeks, 348K views on Twitter. Template for a consultancy lead generation offering.
- **Value Proposition:** Automated local business lead generation. Scrape local businesses, analyse their review profile, generate personalised outreach emails highlighting pain points the agent can solve.
- **Implementation Notes:** Browser automation for Google Maps scraping. Sentiment analysis on reviews. Cold email template generation. Volume: respect rate limits and Google ToS.
- **Dependencies:** Browser automation; email sending infrastructure; Google Maps access.

---

## MONITORING

---

### [MON-001] Server Health Script (RAM, Disk, Chrome, Gateway)
- **Category:** monitoring
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 3.1)
- **Description:** Comprehensive health monitoring script checking RAM usage (>80% warning, >90% critical), swap, disk usage (>75% alert), Chrome/Chromium orphan processes (auto-kill), PM2 health, gateway liveness, system load, and orphan node processes. Runs every 4 hours via system crontab.
- **Value Proposition:** Chrome orphan processes WILL eat all your RAM. Auto-kill is essential. Gateway liveness checks prevent silent failures. Proactive monitoring prevents outages.
- **Implementation Notes:** Adapt from `scripts/server-health.sh` (Leamy version). Schedule via system crontab every 4 hours. Alert delivery via Telegram bot API (direct curl, independent of OpenClaw).
- **Dependencies:** System crontab; Telegram bot token and chat ID for alerts; curl.

---

### [MON-002] Health Cron with Telegram Alerts
- **Category:** monitoring
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 3.2)
- **Description:** Health script wrapped with Telegram alert delivery. Only sends alerts when issues are found — no spam on healthy checks. Uses direct Telegram Bot API (not OpenClaw) so alerts work even if the gateway is down.
- **Value Proposition:** Health monitoring that actually reaches you when things break. Gateway-independent delivery means you'll know about crashes.
- **Implementation Notes:** Wrapper script with `TELEGRAM_BOT_TOKEN` and `CHAT_ID` variables. `curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage"`. Only call when health script returns non-empty output.
- **Dependencies:** Telegram bot token; health script (MON-001); system crontab.

---

### [MON-003] Session Size Monitoring (HEARTBEAT.md)
- **Category:** monitoring
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 3.3)
- **Description:** HEARTBEAT.md configured with session size checks. Alert thresholds: >100 messages warning, >200 critical. Heartbeat interval: 30 minutes. Session bloat causes API 529 errors and degraded performance.
- **Value Proposition:** On 2 Apr 2026, a Telegram session hit 516 messages and froze. Session monitoring would have alerted at 200 and prevented the incident.
- **Implementation Notes:** Add session message count check to HEARTBEAT.md. Track in `heartbeat-state.json`. Alert via channel delivery when thresholds exceeded. Suggest `/new` when critical.
- **Dependencies:** HEARTBEAT.md; heartbeat-state.json; channel for alerts.

---

### [MON-004] Cron Session Bloat Cleanup
- **Category:** monitoring
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md (OnlyTerp — Cron Session Bloat Warning)
- **Description:** Cron jobs accumulate session files over time. Isolated cron sessions pile up and consume disk space and slow the gateway. Periodic cleanup of old cron session files is necessary.
- **Value Proposition:** Prevents gradual disk usage growth and gateway slowdown from accumulated session artifacts.
- **Implementation Notes:** Add to weekly health/cleanup: `find ~/.openclaw/agents/*/sessions/ -name "*.jsonl" -mtime +30 -size +1M -exec rm {} \;`. Conservative: archive instead of delete.
- **Dependencies:** System crontab; session directory access.

---

### [MON-005] Security Audit Cron (Daily)
- **Category:** monitoring
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 6.1)
- **Description:** Daily 3am cron running `openclaw security audit --deep`. System crontab (independent of OpenClaw) logs to JSON file. If critical or warn findings, alert via Telegram.
- **Value Proposition:** Automated daily security posture verification. Catches permission drift, configuration changes, and new vulnerabilities.
- **Implementation Notes:** System cron: `0 3 * * * clawuser /usr/local/bin/openclaw security audit --deep --json >> ~/logs/security-audit.json 2>&1`. Parse JSON for CRITICAL/WARN and alert.
- **Dependencies:** `openclaw security audit` command; system crontab; Telegram alerts (MON-002).

---

### [MON-006] Git Backup (Workspace Version Control)
- **Category:** monitoring
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 3.4)
- **Description:** Every client workspace backed up to a private GitHub repo. One repo per client with `config-backup/` folder. Every config change is committed and pushed. Full version history + rollback ability.
- **Value Proposition:** If the server dies, `git clone` rebuilds the workspace. If a change breaks something, `git revert` fixes it. Complete audit trail of all configuration changes.
- **Implementation Notes:** `github.com/Jonnyhimalaya/<ClientName>` private repo. `.gitignore` excludes credentials, .env, session data. Copy `openclaw.json` + `cron/` + `skills/` to `config-backup/`. Commit after every change.
- **Dependencies:** GitHub account; git installed; SSH key for push access.

---

### [MON-007] Post-Update Verification Checklist
- **Category:** monitoring
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 7.2)
- **Description:** Mandatory checklist after every `npm install -g openclaw@latest`: verify version, check gateway status, test exec access, check auth failover config, verify SearXNG, run `openclaw doctor --fix`, test agent exec, commit config changes.
- **Value Proposition:** Three separate incidents on 2 Apr 2026 were caused by post-update configuration drift. The checklist prevents all of them.
- **Implementation Notes:** Execute steps sequentially. Track known breaking changes per version (e.g., v2026.3.31+ exec approvals, v2026.4.1 auth cooldowns). Commit to git after verification.
- **Dependencies:** OpenClaw installation; git backup (MON-006).

---

### [MON-008] `openclaw doctor` Diagnostic
- **Category:** monitoring
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** ecosystem-state-march2026.md, universal-openclaw-implementation.md
- **Description:** Built-in diagnostic command that audits DM policies, validates configuration, and auto-fixes common issues. Run with `--fix` to auto-repair. Use after every update and when anything seems off.
- **Value Proposition:** Catches misconfiguration before it causes incidents. Auto-fix resolves common issues without manual troubleshooting.
- **Implementation Notes:** `openclaw doctor` for read-only audit. `openclaw doctor --fix` for auto-repair. Run as part of post-update checklist (MON-007).
- **Dependencies:** OpenClaw installed.

---

### [MON-009] Anomaly Detection in Heartbeats
- **Category:** monitoring
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** finance | ops-agent
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 6.4)
- **Description:** During heartbeats, check for unusual message patterns (multiple failed auth, rapid-fire requests), session sizes growing abnormally, unexpected cron job additions, and file permission changes on sensitive directories.
- **Value Proposition:** Catches security incidents and agent misbehaviour in near-real-time. Alerts before damage compounds.
- **Implementation Notes:** Add security checks to HEARTBEAT.md step sequence. Monitor: session message velocity, cron list changes, vault file permissions. Alert on anomalies.
- **Dependencies:** HEARTBEAT.md; security baseline established.

---

### [MON-010] Cost Review & Spend Tracking
- **Category:** monitoring
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Standard Cron Suite), power-user-patterns.md
- **Description:** Scheduled cron (every 4-8 hours) tracking API spend by model, by agent, and by session type. Weekly summary report with week-over-week comparison. Alert on spend anomalies.
- **Value Proposition:** A single runaway sub-agent can burn $50 in an afternoon. Spend monitoring catches this within hours, not at end of month.
- **Implementation Notes:** `openclaw cron add --cron "0 */8 * * *"`. Track token usage per agent. Aggregate into weekly summary. Alert if daily spend exceeds 2x 7-day average.
- **Dependencies:** Provider billing APIs or `/usage tokens` data; channel for alerts.

---

### [MON-011] Log Retention and Archival Policy
- **Category:** monitoring
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** finance | ops-agent
- **Status:** in-playbook
- **Source:** security-hardening-playbook.md (Layer 7.3)
- **Description:** Archive daily memory logs older than 90 days (compress with gzip). Retain session archives for 12 months. Compressed archives retain full audit history while saving disk space.
- **Value Proposition:** Compliance requirement for financial and legal clients. Also prevents disk usage from growing unbounded.
- **Implementation Notes:** Monthly cron: `find memory/archive/ -name "*.md" -mtime +90 -exec gzip {} \;`. Session archival: `find agents/*/sessions/ -name "*.jsonl" -mtime +30 -exec mv {} $ARCHIVE_DIR/ \;`.
- **Dependencies:** Archive directories created; crontab access.

---

### [MON-012] Mission Control Dashboard (abhi1693)
- **Category:** monitoring
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | dev-ops
- **Status:** catalogued
- **Source:** power-user-patterns.md (abhi1693/openclaw-mission-control)
- **Description:** Agent orchestration dashboard from abhi1693 on GitHub. Provides visual monitoring of multi-agent deployments, session states, and agent health.
- **Value Proposition:** Visual overview of a multi-agent deployment. Faster debugging and monitoring than command-line tools alone.
- **Implementation Notes:** Install from abhi1693/openclaw-mission-control. Deploy alongside the gateway. Access via Tailscale (SEC-007) for security.
- **Dependencies:** Node.js; PM2 for process management; Tailscale for secure access.

---

### [MON-013] Image Pruning Cost Bug Check
- **Category:** monitoring
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** content-creator | universal
- **Status:** catalogued
- **Source:** twitter-research-2026-04-05.md (Boris Cherny/Anthropic PR #58038)
- **Description:** Boris Cherny (Anthropic) discovered image pruning was breaking prompt cache → 10-20x cost inflation on image-heavy workflows. PR #58038 fixes it. We may be affected — check any workflows that process images.
- **Value Proposition:** 10-20x cost inflation is massive. A quick check on image-heavy workflows could save significant money.
- **Implementation Notes:** Check if our version includes PR #58038 fix. Audit any image-processing workflows for unexpectedly high token counts. Compare image workflow costs before/after the fix.
- **Dependencies:** OpenClaw version check; image-heavy workflow to audit.

---

### [MON-014] creativecron.ai (Community Cron Recipes)
- **Category:** monitoring
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md (community platforms)
- **Description:** creativecron.ai is a community platform for sharing cron job recipes. Browse and adapt tested cron patterns rather than writing from scratch.
- **Value Proposition:** Reduces cron job setup time. Battle-tested recipes from the community avoid common pitfalls.
- **Implementation Notes:** Browse creativecron.ai for relevant patterns per client industry. Adapt and customise rather than writing from scratch. Vet security of any imported recipe.
- **Dependencies:** Web access; cron system configured.

---

## IDENTITY

---

### [IDN-001] SOUL.md Personality Configuration
- **Category:** identity
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md, universal-openclaw-implementation.md (Phase 2.1)
- **Description:** SOUL.md defines the agent's personality, tone, boundaries, and working relationship rules. Must be under 1KB. Every byte is injected into every message, so it must be tightly written with concrete examples, not abstract rules.
- **Value Proposition:** The single most impactful file for agent quality. A well-written SOUL.md transforms a generic AI into a distinctive, consistent agent persona.
- **Implementation Notes:** Include: anti-sycophancy rule, anti-echo-chamber mandate, data security directives, communication style examples. Use the 12 templates from r/openclaw as starting points.
- **Dependencies:** None — first file written in any deployment.

---

### [IDN-002] USER.md (Human Context File)
- **Category:** identity
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 2.1)
- **Description:** USER.md captures the primary human's name, role, preferences, timezone, and communication style. Ensures the agent knows who it's working for and adapts accordingly.
- **Value Proposition:** Eliminates "who are you?" context loss. The agent always knows the human's name, timezone, and preferences even after session resets.
- **Implementation Notes:** Keep under 500 bytes. Include: name (and how to address them), timezone, communication preference (direct/detailed), any title preferences.
- **Dependencies:** Client intake conversation.

---

### [IDN-003] IDENTITY.md (Agent Name, Creature, Emoji)
- **Category:** identity
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md (Reza Rezvani), universal-openclaw-implementation.md
- **Description:** IDENTITY.md defines the agent's name, creature archetype, vibe, and emoji. Creates a distinctive, memorable personality. Different from SOUL.md (behaviour) — this is the "what am I" file.
- **Value Proposition:** A named agent is stickier. "Ask Wrench" is more memorable than "ask the AI." Clients engage more with personified agents.
- **Implementation Notes:** Keep under 200 bytes. Format: Name, Creature (metaphor), Vibe (2-3 adjectives), Emoji. Choose a name that fits the industry and role.
- **Dependencies:** Client preference for formality level.

---

### [IDN-004] Multiple Persona Profiles
- **Category:** identity
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** personal-assistant | customer-service
- **Status:** catalogued
- **Source:** power-user-patterns.md (Reza Rezvani — Multiple IDENTITY.md personas)
- **Description:** Maintain multiple persona profiles for different contexts: professional, creative, customer-facing. Each with distinct voice, emoji, and behavioral rules. Store in `~/.openclaw/souls/` and switch via `openclaw soul use <name>`.
- **Value Proposition:** An agent that handles both board meetings and casual family chats benefits from context-switching. Different situations call for different personas.
- **Implementation Notes:** Create `souls/` directory with named profiles. Automate switching based on channel (Telegram = casual, Slack = professional) or time of day.
- **Dependencies:** Multiple SOUL.md profiles written; soul-switching command support.

---

### [IDN-005] soul.md Community Repo (aaronjmars)
- **Category:** identity
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md (aaronjmars/soul.md GitHub repo)
- **Description:** Community repository for sharing SOUL.md templates with real opinions, STYLE.md calibration guides, and examples. Source of inspiration for new client deployments.
- **Value Proposition:** Pre-built personality templates accelerate client onboarding. Learn from what works in the community.
- **Implementation Notes:** Review aaronjmars/soul.md repo. Extract useful patterns and adapt per client. Never copy verbatim — each client's agent should feel unique.
- **Dependencies:** GitHub access.

---

### [IDN-006] Agent Naming as Business Strategy
- **Category:** identity
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** customer-service | hospitality | education
- **Status:** catalogued
- **Source:** community-use-cases.md (Nat Eliason "Felix", Daimon Legal agent)
- **Description:** Naming the agent (Felix, Wrench, etc.) creates a memorable identity that staff and clients reference naturally. Businesses adopt the agent as a team member. "Felix made $14,718" — the name makes the result more relatable.
- **Value Proposition:** Stickier client retention. A named agent is harder to replace than "the AI tool." Staff build relationships with named agents.
- **Implementation Notes:** During discovery, collaborate with client on agent name. Consider industry fit (formal for law, friendly for hospitality). Set in IDENTITY.md.
- **Dependencies:** Client buy-in during discovery.

---

### [IDN-007] Business Book Personas (Munger, Ogilvy, Jobs Style)
- **Category:** identity
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | personal-assistant
- **Status:** catalogued
- **Source:** community-use-cases.md (Small software company — 6 agents trained on 150+ business books)
- **Description:** Agents trained on 150+ digitised business books and configured to reason in the style of Munger, Ogilvy, Jobs, Rockefeller, Turing, L.L. Bean. Each agent specialises in a business domain (marketing, sales, finance, legal, accounting, tech, customer service).
- **Value Proposition:** Business wisdom from legendary thinkers applied to daily decisions. Agent that says "Ogilvy would say your headline is too clever by half" is more memorable and credible than generic advice.
- **Implementation Notes:** Digitise key business books into vault/. Configure SOUL.md per agent with reasoning style. Google Workspace Chat/Spaces as channel. 6+ agents on dedicated hardware.
- **Dependencies:** Book content (copyright considerations); dedicated hardware; multi-agent setup.

---

### [IDN-008] TOOLS.md (Tool Usage Reference)
- **Category:** identity
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 2.2), power-user-patterns.md
- **Description:** TOOLS.md provides tool names and one-liner usage notes. Injected every message, so must stay under 1KB. Used to remind the agent about available external tools and how to use them.
- **Value Proposition:** Without TOOLS.md, agents may not know about or correctly use external tools that aren't in the default tool schema.
- **Implementation Notes:** One line per external tool: name, endpoint, and a usage hint. Example: "WordPress — https://leamymaths.ie/wp-admin/ — use browser tool". Keep under 1KB.
- **Dependencies:** Tool inventory from discovery.

---

### [IDN-009] BOOT.md (Startup Routine)
- **Category:** identity
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** ops-agent | personal-assistant
- **Status:** catalogued
- **Source:** power-user-patterns.md (TechNickAI openclaw-config)
- **Description:** BOOT.md defines a startup routine that runs when the agent initialises a new session. Includes context recovery (Protocol D), memory search for recent events, and status checks.
- **Value Proposition:** Consistent agent state on every session start. Prevents the "I forgot everything" problem after session resets.
- **Implementation Notes:** Define startup steps: 1) Check for `.reset` archives (Protocol D), 2) Read today's memory file, 3) Read MEMORY.md, 4) Check heartbeat-state.json for autonomy level, 5) Report ready status.
- **Dependencies:** Memory protocols (MEM-009, MEM-010); heartbeat-state.json.

---

### [IDN-010] HEARTBEAT.md (Periodic Check Pattern)
- **Category:** identity
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** power-user-patterns.md (TechNickAI), universal-openclaw-implementation.md
- **Description:** HEARTBEAT.md defines periodic checks the agent runs every 30 minutes. Step 0: check autonomy level. Subsequent steps: session health, memory status, pending tasks, security checks. Heartbeat Plugin API (`runHeartbeatOnce`) available in v2026.3.28.
- **Value Proposition:** Continuous agent health without manual intervention. The agent self-monitors and self-reports issues.
- **Implementation Notes:** Configure heartbeat interval: 30 minutes. Step sequence: autonomy check → session size → pending actions → security scan → memory checkpoint (if needed). Only alert on issues.
- **Dependencies:** heartbeat-state.json; AGENTS.md autonomy rules.

---

### [IDN-011] Channel Strategy (Per-Channel Agent Binding)
- **Category:** identity
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md (Section 9), community-use-cases.md
- **Description:** Multi-channel architecture where different channels serve different purposes: Telegram for personal assistant DMs, WhatsApp for client-facing, Discord for team ops with channels per agent specialty, Slack for workplace. Per-channel agent bindings and access control.
- **Value Proposition:** Right channel for each audience. Clients WhatsApp, staff use Discord, owner uses Telegram. Each gets appropriate context and persona.
- **Implementation Notes:** Map channels in AGENTS.md routing rules. Restrict MEMORY.md loading in group chats (security — personal context doesn't belong in group channels). Different agents per channel for multi-agent setups.
- **Dependencies:** Multiple channels configured; channel-specific SOUL.md or identity.

---

### [IDN-012] Context-Specific SOUL.md (Customer-Facing vs Internal)
- **Category:** identity
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** customer-service | hospitality
- **Status:** catalogued
- **Source:** power-user-patterns.md (Section 9 creative channel patterns)
- **Description:** Customer-facing agents (WhatsApp) need a different SOUL.md than internal ops agents (Discord/Telegram). Customer-facing: patient, formal, always helpful. Internal: direct, opinionated, flags problems aggressively.
- **Value Proposition:** A single SOUL.md that tries to be both customer-facing and internal-ops ends up mediocre at both. Split personas optimise for each audience.
- **Implementation Notes:** Create separate agent configs: `agents.list["customer-bot"]` with customer SOUL.md, `agents.list["ops"]` with internal SOUL.md. Route channels to appropriate agent.
- **Dependencies:** Multi-agent setup; per-agent SOUL.md.

---

### [IDN-013] Cognitive Calibration (Soul Mod)
- **Category:** identity
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** dev-ops | personal-assistant
- **Status:** catalogued
- **Source:** twitter-research-2026-04-05.md (Toli's Cognitive Calibration)
- **Description:** A SOUL.md modification that makes cheaper models (e.g., Codex) behave more like expensive models (e.g., Opus) through careful personality and reasoning calibration.
- **Value Proposition:** Get Opus-quality reasoning from a Sonnet-priced model through careful prompt engineering. Cost savings without proportional capability loss.
- **Implementation Notes:** Research Toli's cognitive calibration approach. Add reasoning-style directives to SOUL.md: "Think step by step", "Consider edge cases", "Challenge your first instinct." Test on benchmark tasks vs uncalibrated version.
- **Dependencies:** SOUL.md file; test cases for comparison.

---

### [IDN-014] Daimon Legal Identity Pattern (Agent Security Practices)
- **Category:** identity
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** finance | ops-agent
- **Status:** catalogued
- **Source:** community-use-cases.md (Daimon Legal 24/7 law firm deployment)
- **Description:** Agent has its own Gmail account (never uses corporate accounts), explicit human approval for sending emails, structured memory for compounding context, human handoff at sensitive checkpoints, and data sovereignty boundaries.
- **Value Proposition:** Pattern for high-trust deployments in regulated industries. Agent has clear identity separation from the business — its own credentials, its own communication trail.
- **Implementation Notes:** Create dedicated email for the agent (not a corporate alias). Configure approval gates on all outbound communication. Document boundary rules in AGENTS.md. Audit trail for all external actions.
- **Dependencies:** Dedicated agent email account; approval hooks (SEC-015); AGENTS.md boundary rules.

---

### [IDN-015] ClawHub Skills Discovery and Vetting
- **Category:** identity
- **Complexity:** ongoing
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (13,700+ skills), power-user-patterns.md
- **Description:** ClawHub marketplace has 13,700+ skills. CLI integrated: `clawhub search [query]`. ClawNet by Silverfort provides security scanning. However, ~10.8% of broader ecosystem plugins were flagged as malicious pre-ClawHub. Recommended workflow: review source → have OpenClaw analyse it → rebuild custom version.
- **Value Proposition:** Vast library of pre-built capabilities. But must be vetted carefully. The recommended review-analyse-rebuild workflow produces safer, customised skills.
- **Implementation Notes:** `clawhub search [query]` to discover. Review source code. Have agent analyse the skill for security issues. Rebuild a custom version incorporating only what's needed. Never install unvetted skills (SEC-008).
- **Dependencies:** ClawHub access; security review process.

### [UX-019] ClawSuite Dashboard Deployment
- **Category:** ux
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** ops-agent | dev-ops | content-creator | finance
- **Status:** evaluated
- **Source:** github.com/outsourc-e/clawsuite, @outsource_ (Eric), 30K+ clones
- **Description:** Full-stack open-source mission control for OpenClaw. Includes multi-agent orchestration view, live SSE streaming, cost analytics (per-agent spend, daily trends, projected EOM), chat interface, memory browser, ClawHub skills marketplace integration, visual cron manager, exec approval UI, and mobile PWA. Three themes. Auth middleware + rate limiting built in.
- **Value Proposition:** Replaces custom-built Mission Control dashboards. Clone → configure → run. Cuts client dashboard deployment from 4-8 hours custom work to ~1 hour. Professional UI from day one. Best for technical clients and ops-heavy deployments where visual management adds value.
- **Implementation Notes:** Clone repo → npm install → set gateway URL + token → run. Connects to ONE gateway per instance — for multi-gateway setups (multi-tenant), need multiple instances or contribute multi-gateway PR. Not suitable for non-technical clients who just use messaging (adds unnecessary complexity). Electron desktop app + cloud version coming.
- **Dependencies:** ARC-001 (running gateway); gateway auth token.

### [CST-017] Prompt Cache Fix Verification (Anthropic)
- **Category:** cost
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** Boris Cherny (Anthropic), PR #58038, Mario Zechner (@badlogicgames). 93K views, 700 bookmarks.
- **Description:** OpenClaw's image pruning was breaking Anthropic prompt caching — stripping image blocks from already-answered turns caused byte divergence, triggering full cache misses on every subsequent turn. Fix: only prune images older than 3 assistant turns. Any version before this fix means 10-20x cost inflation on Anthropic models.
- **Value Proposition:** Immediate cost savings of up to 90% on Anthropic cached input tokens. Consultancy killer pitch: "Your OpenClaw costs are 10x higher than they should be — here's why." Also fixes latency (cache misses cause prefill waits).
- **Implementation Notes:** Update to OpenClaw ≥v2026.4.2 (fix merged April 4 in PR #58038). After update, verify cache hit rate in Anthropic dashboard. Also check for other cache busters: dynamic timestamps in system prompts, non-deterministic MCP tool ordering. Our setup (v2026.4.1) is affected — update needed.
- **Dependencies:** Anthropic as provider; OpenClaw update.

### [CST-018] Managed Provider Migration Service
- **Category:** cost
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** evaluated
- **Source:** Vox (@Voxyz_ai) Claude→GPT-5.4 migration writeup, Anthropic billing change April 2026
- **Description:** Packaged consultancy service: audit client's current auth setup → configure multi-provider fallback chains → set up profile rotation → test the chain end-to-end. Triggered by Anthropic's <24h billing change that blindsided the community. Most OpenClaw users don't know how to set up fallbacks.
- **Value Proposition:** Immediately sellable service — thousands of users need this RIGHT NOW. We already built this for ourselves (auth.order + auth.cooldowns + cross-provider fallbacks). 1-2 hour engagement per client. Prevents provider lock-in and single-point-of-failure.
- **Implementation Notes:** Follow existing playbook Phase 1.2 (Auth Failover). Add: test provider switchover by temporarily blocking primary, verify fallback activates. Document the full chain for the client. Consider as add-on to every new deployment.
- **Dependencies:** Multiple provider API keys; auth.order configured.

### [CST-019] Cache Buster Audit
- **Category:** cost
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** Boris Cherny, @championswimmer (MCP sorting costing Anthropic "hundreds of millions")
- **Description:** Beyond the image pruning bug, several other patterns silently break Anthropic prompt caching: dynamic timestamps or session IDs in system prompts, non-deterministic MCP tool ordering, workspace files that change between turns. Each cache miss means paying full price for the entire context.
- **Value Proposition:** Even after applying the image fix, other cache busters can inflate costs. A systematic audit catches all of them. Pair with CST-017 for maximum savings.
- **Implementation Notes:** (1) Check system prompt for dynamic content (timestamps, random IDs). (2) Verify MCP tool definitions are sorted deterministically. (3) Check workspace files (MEMORY.md etc.) aren't being rewritten on every turn. (4) Monitor Anthropic cache hit rate after fixes. Consultancy deliverable: "Prompt Cache Audit" as a packaged service.
- **Dependencies:** CST-017 applied first; Anthropic provider.

### [MKT-001] Reviews-as-Pain-Point-Discovery Pipeline
- **Category:** marketing
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** hospitality, education, consultancy
- **Status:** catalogued
- **Source:** Om Patel / Ofek Shaked (@VibeCoderOfek). 348K views, 6.9K bookmarks.
- **Description:** Scrape competitor Google reviews → AI extracts specific pain points → use those pain points to position your own marketing copy against competitor weaknesses. The original tool also generates cold emails, but the real value is the competitive intelligence pattern. Works for any industry where competitors have Google reviews.
- **Value Proposition:** Data-driven competitive positioning. Instead of guessing what customers want, read what they're already complaining about and address it directly. Leamy Maths: find what students hate about other courses. Kilmurry: find what guests complain about at competing hotels. Consultancy: find SMEs complaining about tech/marketing.
- **Implementation Notes:** Google Places API returns ~5 reviews per business (limited). Full review scraping requires browser automation (ToS grey area). Alternative: manual review of top competitors, which is faster for small markets anyway. Could build a lightweight version as an OpenClaw skill.
- **Dependencies:** Google Maps/Places access; browser automation for full scraping.

### [MKT-002] "Built in 2 Weeks" Consultancy Sales Narrative
- **Category:** marketing
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** consultancy
- **Status:** catalogued
- **Source:** Same thread — 16yo dev + Claude Code = full SaaS in 2 weeks.
- **Description:** Use viral "vibe-coded in 2 weeks" stories as consultancy sales framing. Pattern: "A teenager built THIS in 2 weeks with an AI coding agent. Imagine what a managed multi-agent setup does for YOUR business." Then position the demo-to-production gap as where professional services live.
- **Value Proposition:** Instant credibility in sales conversations. Leverages existing viral content as social proof for AI capability, then upsells the reliability/production gap that consultancy fills.
- **Implementation Notes:** Maintain a collection of viral "built with AI" examples for pitch decks. Update monthly. Pair with our own case studies (Kilmurry, Leamy Maths) for the "here's what production-grade looks like" comparison.
- **Dependencies:** None.

### [ARC-022] Priority Map Policy File
- **Category:** architecture
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** Ryan Carson (@ryancarson), ClawChief. 844K views, 1.5K likes. github.com/snarktank/clawchief
- **Description:** Dedicated `priority-map.md` file defining what matters and in what order. Separates prioritization logic from agent instructions (AGENTS.md) and memory (MEMORY.md). Every heartbeat, every decision, every triage references this single source of truth for "what's important right now."
- **Value Proposition:** Eliminates scattered priorities. Makes agent behavior predictable and auditable. Critical for client deployments where the client needs to understand and modify what their agent prioritizes. Also makes handoff between sessions cleaner — new session reads priority map, instantly knows what matters.
- **Implementation Notes:** Create `priority-map.md` at workspace root. Structure: ranked list of priorities with context. Review weekly. Reference from HEARTBEAT.md and AGENTS.md. ClawChief repo has a good template.
- **Dependencies:** None.

### [ARC-023] Auto-Resolver Policy File
- **Category:** architecture
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** Ryan Carson, ClawChief.
- **Description:** Dedicated `auto-resolver.md` defining explicit policies for autonomous vs escalated actions. Replaces vague autonomy tiers with concrete rules: "If email from known contact about scheduling → handle autonomously. If email requesting money → always escalate." Makes the agent's decision boundaries transparent and configurable.
- **Value Proposition:** Removes ambiguity from agent autonomy. Clients can review and modify policies without touching agent code. Reduces risk of unwanted autonomous actions. Essential for trust-building with new clients.
- **Implementation Notes:** Create `auto-resolver.md`. Structure: categorized rules with action (auto/escalate/defer). Start with current implicit rules from AGENTS.md, make them explicit. Update as trust grows.
- **Dependencies:** ARC-022 (priority map informs resolver decisions).

### [ARC-024] Active/Archive Task Separation
- **Category:** architecture
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** Ryan Carson, ClawChief.
- **Description:** Split task management into `tasks.md` (live, canonical) and `tasks-completed.md` (archive). Prevents task files from becoming dumping grounds. Agent works from a clean, short active list; completed items move to archive with timestamps.
- **Value Proposition:** Cleaner task state, faster agent orientation each session. Archive provides accountability trail.
- **Implementation Notes:** Refactor existing `leamymaths-todo.md` into active/archive split. Could generalize for multi-project setups.
- **Dependencies:** None.

### [CST-020] Managed Chief-of-Staff Service Package
- **Category:** cost (consultancy service)
- **Complexity:** complex (1-2 days)
- **Use Case Tags:** consultancy, founders
- **Status:** catalogued
- **Source:** Ryan Carson spending $1000/mo on raw API for ClawChief. Pedro Franceschi (Brex co-founder) also running similar setup.
- **Description:** Packaged "Managed OpenClaw Chief of Staff" consultancy offering. Setup + architecture + ongoing tuning. Target: founders/CEOs who want inbox triage, calendar management, task prep, and proactive follow-ups. Price: $500-1000/mo managed service (competitive vs Ryan's $1000/mo DIY API costs with no support).
- **Value Proposition:** We already have the architecture. ClawChief validates market demand (844K views = founders want this). Our managed service includes setup, priority-map tuning, auto-resolver policies, ongoing maintenance. Client gets a working chief of staff without learning OpenClaw internals.
- **Implementation Notes:** Build from ClawChief template + our existing architecture. Package as consultancy tier. Requires: email integration, calendar access, task management skills. Use ARC-022/023/024 as foundation.
- **Dependencies:** ARC-022, ARC-023, ARC-024. Email/calendar integrations.

### [ARC-025] DESIGN.md — Brand Design System for AI Agents
- **Category:** architecture
- **Complexity:** moderate (1-2 hours per client)
- **Use Case Tags:** universal, consultancy
- **Status:** catalogued
- **Source:** Alvaro Cintas, Google Stitch. 197K views, 5K bookmarks. Repo: github.com/VoltAgent/awesome-design-md. Spec: stitch.withgoogle.com/docs/design-md/overview
- **Description:** Single markdown file capturing a complete design system (colors, typography, components, layout, responsive behavior) that AI coding agents natively understand. Like SOUL.md for UI. 9 sections covering everything from visual atmosphere to agent prompt guides. Works with Claude Code, Cursor, Gemini CLI, Copilot — anything that reads project files.
- **Value Proposition:** Every agent-built page comes out on-brand automatically. Eliminates ad-hoc design choices across builds. Consultancy deliverable: "We'll create a DESIGN.md for your brand" — takes 1 hour, saves dozens on every future build. Pre-built library of 55+ designs (Stripe, Vercel, Linear, etc.) for quick starts.
- **Implementation Notes:** Create per-client DESIGN.md files. Kilmurry: dark + gold #C5A258. Leamy Maths: extract current brand colors/typography from site. For new clients without strong branding, use pre-built templates from awesome-design-md repo. Include in consultancy onboarding package.
- **Dependencies:** None.

### [MKT-003] Synthetic Focus Groups (Simulated Persona Research)
- **Category:** marketing
- **Complexity:** moderate (2-4 hours)
- **Use Case Tags:** education, hospitality, consultancy
- **Status:** catalogued
- **Source:** Brian Roemmele (@brianroemmele, 465K followers) + MiroFish (github.com/666ghj/MiroFish, 24K stars). Swarm agent simulation for prediction/research.
- **Description:** Simulate dozens-to-hundreds of target personas (students, parents, hotel guests) and run marketing messages, pricing strategies, or product ideas through them as a synthetic focus group. Don't need MiroFish's scale — a simple prompt loop with a cheap model (GPT-4o) achieves the same insight. Each persona gets a unique background, preferences, and pain points, then reacts to your proposed messaging.
- **Value Proposition:** Rapid, cheap market research without recruiting real participants. Test 10 headline variants against 100 simulated "Leaving Cert students" in minutes. Test hotel pricing against simulated "couples planning Ryder Cup trips." Won't replace real user testing but great for initial filtering.
- **Implementation Notes:** Build as an OpenClaw skill: input persona template + test material → spawn N simulated responses → aggregate sentiment/preferences. Keep simple — no need for MiroFish infrastructure. GPT-4o-mini at ~$0.01 per 100 personas.
- **Dependencies:** Any cheap LLM API.

### [MEM-001] ByteRover — Portable Hierarchical Memory Layer
- **Category:** memory
- **Complexity:** moderate (2-4 hours to migrate)
- **Use Case Tags:** universal, multi-agent
- **Status:** evaluate-next
- **Source:** Andy Nguyen (@kevinnguyendn). byterover.dev, docs.byterover.dev. Open-sourced 2026-04-06.
- **Description:** Persistent, portable memory system replacing flat markdown + vector search with a hierarchical knowledge tree. Local-first, provider-agnostic, shared across all OpenClaw agents. 92.2% retrieval accuracy on LoCoMo benchmark. Tiered retrieval: fuzzy text → LLM-driven deep search. Can import existing MEMORY.md and memory/ files via CLI (`brv curate -f`).
- **Value Proposition:** Solves our biggest memory gap: cross-agent sharing. Currently our 5 agents (main, sitemgr, marketing, scout, content) have isolated memory. ByteRover would let Scout's research be instantly available to Marketing. Also provides portability across tools (OpenClaw → Claude Code → Cursor) and providers (critical during Anthropic → GPT migration). Client deployments get better memory out of the box.
- **Implementation Notes:** Migration path: `brv curate -f ~/MEMORY.md` + `brv curate --folder ~/memory/`. Let it mature 2-4 weeks before adopting — just open-sourced, 3K followers, could be abandoned. Our current system (autoDream + daily files + QMD search) works fine, just manual. Evaluate after GPT migration is stable. Key question: does the hierarchical tree actually outperform our flat markdown + memory_search in practice?
- **Dependencies:** Node.js, any LLM API key. Optional cloud sync.

### [MEM-002] Cross-Agent Selective Memory Sharing
- **Category:** memory
- **Complexity:** moderate (2-4 hours)
- **Use Case Tags:** multi-agent
- **Status:** catalogued — deprioritised
- **Source:** ByteRover feature + our own gap analysis.
- **Description:** Selective (not default) memory sharing between agents in a multi-agent setup. Current agent isolation is a feature: each agent stays focused on its domain without context bloat from irrelevant cross-agent data. The orchestrator (main) already handles routing information between agents when needed.
- **Value Proposition:** Limited. Default shared memory causes context bloat — Scout's research polluting Sitemgr's context, etc. Current pattern (orchestrator passes relevant findings explicitly) is actually cleaner. Only worth revisiting if a specific use case demands it.
- **Implementation Notes:** Don't implement by default. Current orchestrator-mediated sharing works. If needed for a specific workflow, use a narrow shared file (e.g. `shared/handoff.md`) rather than full memory merging.
- **Dependencies:** Multi-agent setup.

### [IDN-019] Cognitive Calibration Soul Mod
- **Category:** identity
- **Complexity:** quick-win (< 30 min)
- **Use Case Tags:** universal
- **Status:** implement-now
- **Source:** Toli (@tolibear_). 45K views, 431 bookmarks. Builds AX (Agent Experience infrastructure).
- **Description:** A model-agnostic SOUL.md block that encodes Opus-style reasoning behaviours into any model. Key rules: operate from steady confidence not eagerness; simple questions get simple answers; on consequential tasks, check alternatives and failure modes before shipping; surface unstated assumptions; name real trade-offs; if the answer came too fast on something important, test it. Designed by having Opus and GPT-5.4 co-engineer the transfer of reasoning style.
- **Value Proposition:** Directly addresses model migration quality gap. When moving Opus → GPT-5.4 (our immediate plan), this block preserves the thoughtful reasoning style without paying Opus prices. Also improves cheaper models (Sonnet, Gemini) on client deployments — free quality upgrade.
- **Implementation Notes:** Add to SOUL.md as a ## Cognitive Calibration section. Apply to all agent SOUL.md files including client deployments. Test on GPT-5.4 before and after to validate improvement. The block is already battle-tested by Toli across multiple agents.
- **Dependencies:** None.

### [IDN-018] Model-Specific SOUL.md Tuning
- **Category:** identity
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** Vox (@Voxyz_ai) GPT-5.4 migration notes — "needs Senior Engineer framing to reduce verbosity"
- **Description:** Different models respond differently to the same SOUL.md. When switching a client's primary model, SOUL.md may need adjustment. GPT-5.4 specifically benefits from authority framing ("You are a senior engineer") to curb verbosity. Claude responds better to personality-driven prompts. Gemini needs more explicit tool-use instructions.
- **Value Proposition:** Same SOUL.md on a different model can produce noticeably worse behaviour. 15-minute tuning pass during any model migration prevents client disappointment. Cataloguing model-specific quirks saves time on future migrations.
- **Implementation Notes:** Maintain a reference doc of per-model SOUL.md tweaks. When migrating: swap model → test 5-10 representative prompts → adjust SOUL.md tone/framing → re-test. Pairs with IDN-016 (regression test suite).
- **Dependencies:** IDN-016 recommended; knowledge of target model's quirks.

### [UX-020] Cost Analytics Dashboard (Visual)
- **Category:** ux
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** ClawSuite cost analytics feature; also achievable via custom dashboard
- **Description:** Visual per-agent cost tracking with daily trends, MTD totals, and projected end-of-month spend. Shows which agents are expensive and why. Can be delivered via ClawSuite (UX-019) or built as a standalone panel in existing Mission Control.
- **Value Proposition:** Makes costs tangible and visible. Essential for client ROI conversations — "your agent saved X this month while costing Y." Also catches runaway cost spikes (e.g., our Opus bulk-membership incident at €15).
- **Implementation Notes:** ClawSuite includes this natively. For standalone: pull from OpenClaw usage logs, aggregate per agent per day, render in existing Mission Control. Pair with CST cost-routing entries for maximum savings visibility.
- **Dependencies:** Usage tracking enabled; either ClawSuite (UX-019) or custom dashboard.

### [MON-015] Harbor Agent Benchmarking Framework
- **Category:** monitoring
- **Complexity:** major (4+ hours)
- **Use Case Tags:** dev-ops | ops-agent | universal
- **Status:** catalogued
- **Source:** github.com/harbor-framework/harbor, used by AutoAgent (ThirdLayer, YC W25)
- **Description:** Universal agent benchmarking framework that can evaluate Claude Code, Codex CLI, OpenHands, and other agents against standardised tasks. Score-based with trace logging. Docker-isolated. Used by AutoAgent to achieve #1 on SpreadsheetBench and TerminalBench.
- **Value Proposition:** Lets us *prove* agent quality with numbers, not vibes. Consultancy differentiator: before/after benchmarking when tuning client agents. Pairs with IDN-016 (regression testing) to provide quantitative evidence that changes improved performance. Also useful for comparing model choices (e.g., Opus vs Sonnet for a specific workflow).
- **Implementation Notes:** Docker required. Define benchmark tasks relevant to the client's domain. Run baseline, make changes, re-run, compare scores. Not a quick win — needs custom task definitions per use case. Best for mature deployments where proving ROI matters (enterprise clients, agencies).
- **Dependencies:** Docker; domain-specific benchmark tasks defined; IDN-016 recommended.

### [IDN-016] Eval-Gated Agent Tuning (Regression Test Suite)
- **Category:** identity
- **Complexity:** moderate (1-4 hours) initial setup, then ongoing
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** NeoSigma auto-harness (github.com/neosigmaai/auto-harness), adapted from coding agent self-improvement loop to OpenClaw context
- **Description:** Maintain a small regression test suite (5-10 representative prompts/scenarios) for each agent. Before changing SOUL.md/AGENTS.md, replay the test suite to verify the agent still handles known-good scenarios correctly. Inspired by NeoSigma's eval-gated improvement loop for coding agents — adapted here for conversational agents where the "harness" is SOUL.md + AGENTS.md + skills.
- **Value Proposition:** Prevents the whack-a-mole problem where fixing one agent behaviour breaks another. Turns agent tuning from guesswork into a measurable process. For clients: "monthly agent tuning review" as a recurring consultancy deliverable.
- **Implementation Notes:** Create `tests/agent-scenarios.md` with 5-10 prompts and expected behaviour. Run monthly via isolated cron session — replay each prompt, compare output against expected. Flag regressions. Best suited for mature deployments (30+ days) with enough .learnings data to mine. Can also do periodic failure clustering: review .learnings/corrections.md and .learnings/ERRORS.md monthly, cluster by root cause, batch-update AGENTS.md.
- **Dependencies:** .learnings/ directory populated; agent running 30+ days; isolated cron session.

### [IDN-017] Failure Clustering & Batch Tuning
- **Category:** identity
- **Complexity:** moderate (1-4 hours) per review cycle
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** NeoSigma auto-harness pattern (failure mining → root cause clustering → batched harness changes), adapted for OpenClaw
- **Description:** Instead of reactively updating AGENTS.md after each mistake, accumulate errors in .learnings/ for 30 days, then cluster failures by root cause and apply batched, tested fixes. NeoSigma's key insight: individual reactive fixes cause regression; batched, evaluated changes are more stable.
- **Value Proposition:** Higher quality agent improvements. Consultancy angle: "monthly agent optimisation report" showing failure patterns, changes made, and before/after metrics. Turns ongoing support into a structured, valuable deliverable.
- **Implementation Notes:** Monthly review cycle: (1) Read .learnings/corrections.md + ERRORS.md, (2) Cluster by category (tool misuse, tone issues, factual errors, workflow gaps), (3) Draft AGENTS.md/SOUL.md changes addressing top 3 clusters, (4) Run regression suite (IDN-016) before and after, (5) Log changes and results. Can be delegated to advisor/cheap model for initial clustering.
- **Dependencies:** IDN-016 (regression test suite); .learnings/ directory; 30+ days of operational data.

---

## ARCHITECTURE

---

### [ARC-001] systemd Gateway Service (Not tmux/screen/nohup)
- **Category:** architecture
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 1.2 systemd section)
- **Description:** Run the OpenClaw gateway as a systemd service, not tmux/screen/nohup. systemd provides auto-restart on crash, boot persistence, proper logging via journalctl, and a clean reproducible environment. tmux holds processes and env vars in memory only — lost on kill/reboot.
- **Value Proposition:** Both Kilmurry and Leamy had systemd migration failures on 30 March 2026 because they were running in tmux. tmux is not a process manager.
- **Implementation Notes:** Create `/etc/systemd/system/openclaw-gateway.service`. EnvironmentFile for secrets. ALWAYS run `openclaw gateway --help` to verify correct ExecStart command. Test manually before enabling. See playbook for full template.
- **Dependencies:** Linux server; systemd; secrets in .env file (SEC-016).

---

### [ARC-002] Dedicated VPS Per Client (Data Isolation)
- **Category:** architecture
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 0.2)
- **Description:** Each client gets a dedicated Linode/Hetzner VPS. Data isolation is non-negotiable — no shared infrastructure between clients. Minimum 4GB RAM (8GB recommended if browser automation needed).
- **Value Proposition:** Client data isolation prevents cross-contamination. If one server is compromised, other clients are unaffected. Clean billing per client.
- **Implementation Notes:** Linode/Hetzner. 4GB minimum, 8GB with browser. Region closest to client geography. Our SSH key + optionally client's SSH key.
- **Dependencies:** Hosting account; client agreement on hosting costs.

---

### [ARC-003] Layered Playbook Architecture (Universal → Sector → Custom)
- **Category:** architecture
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Playbook Structure)
- **Description:** Three-layer architecture: Universal Foundation (every client gets this), Sector Module (industry patterns — hotels.md, education.md), Business-Specific Customisation (unique workflows, integrations, skills). Sector modules stack on top of the universal foundation.
- **Value Proposition:** Standardises delivery quality while allowing customisation. Every client gets the proven foundation; sector expertise adds value; custom work is genuinely unique.
- **Implementation Notes:** Apply Phase 1-4 (universal), Phase 5 (sector), Phase 6 (custom) sequentially. Never skip the universal foundation.
- **Dependencies:** Playbook files for each sector; universal implementation checklist.

---

### [ARC-004] Auth Profile Rotation + Cooldowns
- **Category:** architecture
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 1.2 Auth Failover)
- **Description:** Multiple auth profiles per provider (e.g., two Anthropic API keys). `auth.order` specifies which profile to try first. `auth.cooldowns` controls how many profile rotations to attempt before falling to a different model. Introduced in v2026.4.1.
- **Value Proposition:** On 2 Apr 2026, the agent hit 429 rate limits and couldn't fall to the backup Anthropic key because auth.order wasn't configured. Having multiple keys is useless without rotation config.
- **Implementation Notes:** `openclaw config set auth.order.anthropic '["primary", "backup"]'`. Set `rateLimitedProfileRotations: 2`, `overloadedProfileRotations: 2`, `overloadedBackoffMs: 2000`. Full failover chain in playbook.
- **Dependencies:** v2026.4.1+; multiple API keys per provider.

---

### [ARC-005] SearXNG Self-Hosted Search
- **Category:** architecture
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** implemented-ours
- **Source:** universal-openclaw-implementation.md (Phase 4.2)
- **Description:** SearXNG is the recommended search backend as of v2026.4.1+. Self-hosted, bundled as a plugin, zero rate limits. Replaces Brave Search which has rate limiting (we hit 429s during production use on 2 Apr 2026).
- **Value Proposition:** Zero rate limits on search. Self-hosted = no third-party dependency. No API key needed. Eliminates the Brave 429 problem.
- **Implementation Notes:** Enable plugin: `openclaw config set plugins.entries.searxng.enabled true`. Set baseUrl to `http://localhost:8888`. Disable Brave. Verify: `curl 'http://localhost:8888/search?q=test&format=json'`.
- **Dependencies:** v2026.4.1+; localhost:8888 available.

---

### [ARC-006] Multi-Agent Team Architecture
- **Category:** architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | dev-ops | hospitality
- **Status:** in-playbook
- **Source:** power-user-patterns.md (Section 3), community-use-cases.md, multi-agent-coordination-playbook.md
- **Description:** Orchestrator → specialist agents pattern. Separate workspaces per agent, different SOUL.md per agent, channel bindings (agent A handles Telegram DMs, agent B handles Discord). Shared memory layer but isolated sessions. maxSpawnDepth defaults to 1, max 2.
- **Value Proposition:** Specialisation produces better results than one generalist agent. Each agent optimised for its role with the right model, right context, right persona.
- **Implementation Notes:** Start single-agent. Expand to multi-agent only when volume exceeds one agent's capacity or specialisation is needed. Use the growth path: Single Agent → Multi-Agent → Department-Aligned Team → Autonomous Operations.
- **Dependencies:** Proven single-agent deployment; clear role separation; sufficient API budget.

---

### [ARC-007] CEO/COO/Worker Model (Orchestration Hierarchy)
- **Category:** architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | dev-ops
- **Status:** catalogued
- **Source:** power-user-patterns.md (OnlyTerp CEO/COO/Worker Model)
- **Description:** Lean orchestrator (~5KB context) receives questions, runs memory_search (45ms, local, $0), loads only relevant context (~200 tokens), then delegates heavy work to sub-agents. The orchestrator coordinates; sub-agents execute.
- **Value Proposition:** Minimal context per orchestrator message = fastest, cheapest responses. Sub-agents carry the workload. Clean separation of coordination and execution.
- **Implementation Notes:** Orchestrator: Opus with lean SOUL/AGENTS/MEMORY. Sub-agents: Sonnet/Haiku with task-specific context. Memory search on every turn. Sub-agents for file editing, research, content generation.
- **Dependencies:** Multi-agent setup (ARC-006); QMD memory (MEM-004); model tiering (CST-004).

---

### [ARC-008] STATE.yaml Autonomous Project Management
- **Category:** architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** dev-ops | ops-agent
- **Status:** catalogued
- **Source:** power-user-patterns.md
- **Description:** Sub-agents work in parallel without orchestrator overhead using a shared STATE.yaml file for coordination. Each agent reads state, picks up unassigned work, updates state on completion.
- **Value Proposition:** Removes the orchestrator bottleneck for parallel workstreams. Agents self-organise based on shared state.
- **Implementation Notes:** Create STATE.yaml with task assignments, statuses, and dependencies. Agents poll state file for new work. File-based coordination — no message passing overhead.
- **Dependencies:** Multi-agent setup (ARC-006); shared workspace access.

---

### [ARC-009] Podman Rootless Container Deployment
- **Category:** architecture
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** dev-ops | universal
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (v2026.3.28)
- **Description:** Rootless Podman container deployment simplified in v2026.3.28 with `~/.local/bin` launch helper. Provides container isolation without Docker's daemon requirement or root privileges.
- **Value Proposition:** Container isolation without root. Each client deployment in its own container provides stronger isolation than shared-server deployments.
- **Implementation Notes:** Follow v2026.3.28 Podman simplification guide. Rootless user container setup. Configure with `~/.local/bin` launch helper.
- **Dependencies:** v2026.3.28+; Podman installed.

---

### [ARC-010] Sequential Filesystem Handoff (Multi-Agent Coordination)
- **Category:** architecture
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** ops-agent | hospitality | content-creator
- **Status:** implemented-ours
- **Source:** multi-agent-coordination-playbook.md
- **Description:** Two or more agents run sequentially. Each writes output to a shared `intel-drops/` folder. The next agent reads previous output and builds on it. Filesystem is the coordination layer — no message queues or webhooks. POC: Scout (Grok, 40s) → Main (Sonnet, 118s) = ~3 min total, ~$0.053/day.
- **Value Proposition:** Simple, auditable multi-agent coordination. Every intermediate artifact is a file you can inspect. Total daily cost ~$0.05 vs ~$0.15 running everything on Opus.
- **Implementation Notes:** Create `intel-drops/` folder. Cron Agent A at T-10 min, Agent B at T. Graceful degradation: Agent B handles missing handoff files. Timeout on A < gap between A and B.
- **Dependencies:** Multi-agent setup; cron system; shared filesystem or symlinks.

---

### [ARC-011] Fan-Out Parallel Agent Pattern
- **Category:** architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | hospitality | research-agent
- **Status:** catalogued
- **Source:** multi-agent-coordination-playbook.md (Variations — Fan-Out)
- **Description:** Multiple agents run simultaneously, each covering different sources. A final merge agent reads all outputs and synthesises. Pattern: Agent A → twitter.md, Agent B → reddit.md, Agent C → news.md → Merge Agent → final report.
- **Value Proposition:** Parallel data gathering from multiple sources. Total time = slowest agent + merge time, not sum of all agents.
- **Implementation Notes:** Careful timing required. All fan-out agents must complete before merge agent runs. Use conservative gaps. Each agent writes to a named file in intel-drops/.
- **Dependencies:** Multi-agent setup (ARC-006); sequential handoff (ARC-010) as baseline; cron scheduling.

---

### [ARC-012] Review Loop Pattern (Draft → Critique → Revise)
- **Category:** architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** content-creator | customer-service | education
- **Status:** catalogued
- **Source:** multi-agent-coordination-playbook.md (Variations — Review Loop)
- **Description:** Agent A (creative) produces a draft → Agent B (critical) reviews and critiques → Agent A reads review and produces a final version. Requires 3 cron slots but produces higher quality output than single-pass generation.
- **Value Proposition:** Catches errors, inconsistencies, and quality issues through adversarial review. Particularly valuable for customer-facing content.
- **Implementation Notes:** 3 cron jobs with appropriate gaps. Creative agent uses Sonnet; critical agent uses Opus or different provider for genuine perspective diversity. Review file format must be structured for easy parsing.
- **Dependencies:** Multi-agent setup; 3 cron slots; two distinct models for genuine diversity.

---

### [ARC-013] Moltworker — OpenClaw on Cloudflare Workers
- **Category:** architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** dev-ops | universal
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (competitors section)
- **Description:** Moltworker runs OpenClaw on Cloudflare Workers — serverless, ~$35/mo, zero local server exposure. No VPS management, no system administration.
- **Value Proposition:** Eliminates server management entirely. For clients who don't want to think about VPS, security hardening, or system administration. Fixed cost of ~$35/month.
- **Implementation Notes:** Evaluate for non-technical clients who just want an agent running without infrastructure concerns. Trade-off: less customisation, no browser automation, no local model support.
- **Dependencies:** Cloudflare account; Moltworker installation.

---

### [ARC-014] GoGogot — Ultra-Light Self-Hosted Alternative
- **Category:** architecture
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** ecosystem-state-march2026.md (competitors — managed alternatives)
- **Description:** GoGogot is a free/OSS alternative — 15MB, one Docker command, lightest self-hosted option. For clients who need maximum simplicity with minimum overhead.
- **Value Proposition:** When OpenClaw's full feature set is overkill. A simple chatbot with no multi-agent, no skills, no complex memory — just a channel-connected LLM.
- **Implementation Notes:** Evaluate for clients who only need a simple FAQ bot or basic assistant. If they need memory, multi-agent, or complex automation, stick with OpenClaw.
- **Dependencies:** Docker; minimal server (1GB RAM sufficient).

---

### [ARC-015] Mission Control (Next.js Dashboard)
- **Category:** architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** ops-agent | hospitality
- **Status:** in-playbook
- **Source:** universal-openclaw-implementation.md (Phase 4.4)
- **Description:** Next.js dashboard deployed via PM2 for client-facing monitoring. Client-specific pages. Accessible on localhost or behind Tailscale auth. Provides a visual overview of agent operations.
- **Value Proposition:** Non-technical clients need a visual dashboard, not command-line tools. Shows agent health, recent actions, and key metrics.
- **Implementation Notes:** Deploy Next.js app. PM2 for process management with boot persistence. Secure behind Tailscale (SEC-007/SEC-017). Rebuild after config changes.
- **Dependencies:** Node.js; PM2; Tailscale for access control.

---

### [ARC-016] Self-Healing Home Server Pattern
- **Category:** architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** dev-ops | personal-assistant
- **Status:** catalogued
- **Source:** community-use-cases.md (awesome-openclaw-usecases)
- **Description:** Always-on infrastructure agent with SSH access, automated cron jobs, and self-healing capabilities across the home network. Detects service failures and auto-remediates.
- **Value Proposition:** Home server that fixes itself. No 3am wake-ups for service restarts. Agent monitors, diagnoses, and resolves common failures autonomously.
- **Implementation Notes:** Grant agent SSH access to home network devices. Configure health checks for key services. Define auto-remediation playbooks (restart service, clear disk, reboot device). Human alert for anything outside playbook.
- **Dependencies:** SSH infrastructure; service health endpoints; remediation playbooks.

---

### [ARC-017] Self-Hosted Git (Gitea alongside OpenClaw)
- **Category:** architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** dev-ops
- **Status:** catalogued
- **Source:** power-user-patterns.md (Section 12 — Common Mistakes)
- **Description:** Host Gitea alongside OpenClaw for self-hosted git. Eliminates dependency on GitHub — one user's GitHub account suspension caused loss of access to all repos.
- **Value Proposition:** Complete data sovereignty. No dependency on third-party git hosting. Eliminates single point of failure.
- **Implementation Notes:** Install Gitea on the same VPS or adjacent server. Lightweight (Go binary, runs on minimal resources). Migrate critical repos from GitHub to Gitea.
- **Dependencies:** VPS resources; domain/subdomain for Gitea; backup strategy.

---

### [ARC-018] Managed Hosting Options for Non-Technical Clients
- **Category:** architecture
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** power-user-patterns.md (Section 12), ecosystem-state-march2026.md
- **Description:** For clients unwilling to manage VPS: ClawHosters (Hetzner, €19/mo), EasyClaw.co (one-click Telegram), ButterClaw (privacy-first), Hostinger Docker Catalog (random port + auto-auth). Trade-off: less control for less complexity.
- **Value Proposition:** Opens OpenClaw to non-technical clients who can't manage a VPS. Expands the addressable market.
- **Implementation Notes:** Evaluate per client. We still provide configuration, identity, memory, and automation layers on top of managed hosting. Revenue model: managed hosting + our configuration/customisation fee.
- **Dependencies:** Client budget; managed hosting provider account.

---

### [ARC-019] OpenClaw as Consultancy Offering (Meta-Architecture)
- **Category:** architecture
- **Complexity:** ongoing
- **Use Case Tags:** universal
- **Status:** in-playbook
- **Source:** easy-wins-by-industry.md (pricing tiers), community-use-cases.md (consulting ecosystem)
- **Description:** Our consultancy model: Starter (€500 setup + €99/mo), Professional (€1,500 setup + €199/mo), Enterprise (€3,000 setup + €349/mo). Vertical specialisation recommended — "OpenClaw for hotels" beats "OpenClaw for everyone."
- **Value Proposition:** Proven market with 10+ dedicated OpenClaw consultancies launched in Feb-March 2026. "Too complex for Lindy, too busy for DIY" is our target segment.
- **Implementation Notes:** Discovery → pick archetype → pull essential catalogue items → add recommended items → customise. See INDEX.md for the workflow.
- **Dependencies:** This catalogue; playbooks; sector modules.

---

### [ARC-020] NeoSigma Auto-Harness (Self-Improving Agent Loop)
- **Category:** architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** dev-ops | research-agent
- **Status:** catalogued
- **Source:** twitter-research-2026-04-05.md
- **Description:** Self-improving agent loop that achieved 0.56 → 0.78 on the Tau3 benchmark. Agent iteratively refines its own capabilities through automated testing and improvement cycles.
- **Value Proposition:** Agents that improve themselves over time without manual tuning. Interesting for long-running research or development agents.
- **Implementation Notes:** Research NeoSigma auto-harness approach. Evaluate for agents that need to improve on specific benchmarks or tasks over time. Not actionable now — monitor.
- **Dependencies:** Research-stage; not production-ready.

---

### [ARC-021] AutoAgent (ThirdLayer, YC W25) — Autonomous Harness Engineering
- **Category:** architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** dev-ops
- **Status:** catalogued
- **Source:** twitter-research-2026-04-05.md
- **Description:** ThirdLayer (YC W25) autonomous harness engineering — #1 on multiple agent benchmarks. Self-tuning agent framework that optimises agent configuration automatically.
- **Value Proposition:** Could automate some of what we do manually (agent tuning, prompt optimisation). Worth monitoring for when it matures.
- **Implementation Notes:** Monitor ThirdLayer/AutoAgent. Evaluate when stable. If it can reliably auto-tune agent configurations, it could accelerate our deployment pipeline.
- **Dependencies:** Research-stage; YC W25 company — may productise soon.
---

## NEW ENTRIES — April 14, 2026 Bookmark Research Batch

---

### [MEM-023] Include Session Transcripts in QMD Search Paths
- **Category:** memory
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** @BenjaminBadejo (Apr 11, 182K views)
- **Description:** Add session transcript paths to QMD's `paths[]` config alongside `memory/` and `vault/`. Every past conversation becomes semantically searchable, not just what the agent manually wrote to memory files.
- **Value Proposition:** Dramatically increases recall depth. Agent can find context from conversations it never explicitly logged.
- **Implementation Notes:** Add to `memory.qmd.paths[]` in openclaw.json: `{"name": "sessions", "path": "~/.openclaw/agents/main/sessions", "pattern": "*.jsonl"}`. Run QMD re-index after. Slight latency increase (5-8s per response) is acceptable trade-off.
- **Action for us:** Implement on main agent. High priority.

---

### [MEM-024] Durable Agent Rule — Codify Before Moving On
- **Category:** memory / automation
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** @garrytan / YC CEO (Apr 9, 246K views)
- **Description:** Add to AGENTS.md: "You are not allowed to do one-off work. If I ask you to do something that will need to happen again: (1) do it manually first, (2) show output and ask for approval, (3) if approved, codify into a SKILL.md file, (4) if it should run automatically, add to cron."
- **Value Proposition:** Prevents knowledge loss. Tasks that recur get systematised automatically rather than relying on the human to remember to ask again.
- **Implementation Notes:** Paste rule directly into AGENTS.md. Works best paired with a `/skills` directory in workspace.
- **Action for us:** Already partially in our workflow. Formalise the rule in AGENTS.md.

---

### [MEM-025] Skill Drift Detection
- **Category:** memory / identity
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** universal
- **Status:** catalogued
- **Source:** @MatthewBerman (Apr 10, 8.8K views)
- **Description:** As AGENTS.md, SOUL.md, and skills accumulate edits over time, instructions start contradicting each other silently. Tool at journeykits.ai/browse/kits/matt-clawd/skill-drift-detector detects and resolves these conflicts.
- **Value Proposition:** Prevents agent behaviour degrading gradually as workspace files grow. "Silent killer post-Claude ban."
- **Action for us:** Run drift check quarterly or after major AGENTS.md rewrites. Add to playbook.

---

### [ARC-028] Open Harness = Own Your Memory
- **Category:** architecture
- **Complexity:** ongoing
- **Use Case Tags:** universal, consultancy-pitch
- **Status:** catalogued
- **Source:** @hwchase17 / LangChain founder (Apr 11, 1.8M views, 10K bookmarks)
- **Description:** Agent harnesses won't be absorbed by models. The real moat is memory. Closed harnesses (Anthropic Managed Agents, OpenAI APIs) = yield control of your agent's memory to a third party. Open harnesses (OpenClaw, Letta) = you own your memory, your data, your agent's accumulated intelligence.
- **Value Proposition:** This is the core consultancy pitch. Every OpenClaw client we deploy owns their data permanently. They can switch models, switch providers, export everything. No lock-in.
- **Key Quote:** "If your agent's memory lives behind someone else's API, you don't have a product."
- **Action for us:** Use this framing in all consultancy pitch materials. Add to sales deck.

---

### [ARC-029] Pluggable Harness Architecture + Strict Mode
- **Category:** architecture
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** GPT users, power users
- **Status:** catalogued
- **Source:** @steipete / OpenClaw contributor (Apr 12, 358K views)
- **Description:** Two config options for GPT laziness: (1) `agents.defaults.embeddedPi.executionContract = 'strict-agentic'` — forces agent to keep working instead of stopping at "here's a plan". (2) Native Codex harness via `plugins.entries.codex.enabled = true` + `agents.defaults.model = 'codex/gpt-5.4'` for longer-horizon task completion. Harnesses are now pluggable plugins.
- **Action for us:** If GPT-5.4 goes lazy on long tasks, apply strict-agentic mode. Test before rolling out to clients.

---

### [MEM-026] Git-Like Version Control for Agent Memory (ByteRover)
- **Category:** memory
- **Complexity:** moderate (1-4 hours)
- **Use Case Tags:** multi-agent, team deployments
- **Status:** catalogued
- **Source:** @kevinnguyendn / ByteRover creator (Apr 8, 10.8K views)
- **Description:** ByteRover adds 15 git-like operations to shared agent context trees: staging, commits, rollbacks, merging, branching. Prevents "last writer wins" overwrites when multiple agents or humans update the same knowledge base. Install: `curl -fsSL https://byterover.dev/install | sh`. GitHub: byterover.dev.
- **Value Proposition:** Essential for multi-agent setups or client deployments where multiple people use the same agent. Currently our agents have isolated memory (by design) but shared knowledge management is a future need.
- **Action for us:** Low priority now (isolation is a feature), but evaluate for consultancy clients with team deployments.

---

### [AUT-038] /last30days Skill — AI-Led Research Engine
- **Category:** automation
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** research, competitive analysis, content
- **Status:** catalogued
- **Source:** @mvanhorn (Apr 9, 308K views)
- **Description:** OpenClaw skill that runs AI-agent-led research. Pre-research brain resolves X handles, subreddits, YouTube channels, TikTok hashtags for a topic before running the actual search. Reddit, X, YouTube content free with no API keys. Single-pass X-vs-Y comparisons in 5 mins. GitHub: mvanhorn/last30days-skill.
- **Value Proposition:** Replaces or supercharges Scout agent for competitive research. Particularly useful for Leamy Maths competitor tracking and consultancy client market research.
- **Action for us:** Install as a skill on Scout agent. Test with a Leamy Maths competitor query.

---

### [CST-024] Permanent Memory for Claude Code (95% Token Reduction)
- **Category:** cost
- **Complexity:** quick-win (< 1 hour)
- **Use Case Tags:** Claude Code users
- **Status:** catalogued
- **Source:** @RoundtableSpace (Apr 12, 553K views, 46K GitHub stars)
- **Description:** Open-source tool (likely claude-mem) that gives Claude Code permanent memory across sessions. Claims 95% less token consumption per session, never hits context limits, picks up exactly where left off. One command install, free.
- **Value Proposition:** Massive cost reduction for Jack's Claude Code usage on Kilmurry Mission Control. If the 95% claim holds even partially it's transformative.
- **Action for us:** Find the exact repo (search GitHub for "claude-mem" or "claude code permanent memory" ~46K stars), install on Kilmurry for Jack. High priority.

---

### [MEM-027] Vertical vs Horizontal Memory Architecture
- **Category:** memory / architecture
- **Complexity:** major (4+ hours)
- **Use Case Tags:** multi-agent, advanced
- **Status:** catalogued
- **Source:** @Voxyz_ai (Apr 14)
- **Description:** Two distinct memory failure modes: Vertical (within-agent forgetting) solved by Dreaming/auto-consolidation. Horizontal (cross-agent silos) solved by a shared knowledge layer like GBrain integrated with Gmail/Calendar data. Without horizontal memory, agents in a multi-agent setup cannot benefit from each other's learning.
- **Action for us:** Vertical is handled. Horizontal is a known gap (Jonny chose isolation intentionally). GBrain is the leading candidate if we ever want to bridge this. Document trade-off for consultancy clients.
