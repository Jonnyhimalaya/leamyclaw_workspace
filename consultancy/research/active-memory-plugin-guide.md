# Active Memory Plugin — Research Notes (2026-04-14)

## What It Is
New optional plugin in OpenClaw v2026.4.10 (#64298). Introduces a dedicated memory sub-agent that runs **before** each main reply, automatically searching and injecting relevant context from:
- MEMORY.md and memory/*.md files
- Past conversation details
- User preferences and decisions

## Why It Matters for Us
- **Multi-agent context loss** is the #1 community complaint (GitHub issues #50263, #62442, #45868)
- Our 6-agent setup uses isolated workspaces (Jonny's decision) — Active Memory improves recall **within** each agent's own sessions without breaking isolation
- Particularly valuable for the Orchestrator (main) which has the longest, most complex sessions

## How to Enable
After upgrading to v2026.4.10:
1. Add Active Memory plugin to agent config in `openclaw.json`
2. Configure which memory paths to index
3. Set the sub-agent model (use a cheap/fast model — this runs on every message)

## Cost Considerations
- Adds one extra LLM call per message (the memory sub-agent query)
- Use a lightweight model (e.g., GPT-4o-mini, Gemini Flash) for the memory sub-agent to keep costs down
- Don't enable on agents with very high message volume unless the recall improvement justifies cost

## Consultancy Application
- This is a strong selling point: "Your AI assistant remembers everything about your business"
- For client deployments: enable by default with a budget-friendly memory model
- Document in onboarding playbook: what gets remembered, privacy implications, how to clear memory

## Related: Context Passing Between Agents
Active Memory solves intra-agent recall. For inter-agent context:
- GitHub issue #50263 requests persona file injection via `sessions_spawn`
- Current workaround: pass context explicitly in the `task` parameter
- Our approach: keep isolation, but make each agent excellent at remembering its own context
