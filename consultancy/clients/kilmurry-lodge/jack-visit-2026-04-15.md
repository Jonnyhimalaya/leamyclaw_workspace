# Jack Visit — April 15, 2026
_Prep for Jonny's in-person visit to Kilmurry Lodge_

## Priority 1: Kill the 980-message session
Jack needs to send `/new` to KilmurryBot today (or when you arrive).
That session has been running since April 5 — every message is sending 5MB of context overhead at Opus pricing.
If he hasn't done it yet, have him do it first thing.

## Priority 2: everything-claude-code setup
**Repo:** https://github.com/affaan-m/everything-claude-code (155K stars, Anthropic hackathon winner)

What it is: A complete performance optimisation system for Claude Code — skills, memory system, instincts, security scanning, research-first development. Works across Claude Code, Codex, Cursor, and others.

**Install on Kilmurry server:**
```bash
ssh clawuser@172.239.98.61
export PATH="$HOME/.npm-global/bin:$PATH"
cd ~/mission-control
npx ecc-universal install
```

Or manually clone and read:
```bash
git clone https://github.com/affaan-m/everything-claude-code.git /tmp/ecc
cat /tmp/ecc/README.md
```

Key components to implement for Jack:
- **Memory optimisation** — cross-session recall for Claude Code (the 95% token reduction claim)
- **Skills system** — codified reusable tasks (aligns with the Durable Agent Rule we just added)
- **Instincts** — behavioural rules that prevent common failure modes
- **Security scanning** — flags risky operations before execution

**Time estimate:** 30-45 mins to walk through and install the core bits.

## Priority 3: Review the Claude Code + ACP workflow
Jack now has:
- Claude Code v2.1.104 installed and authenticated (Claude Max team subscription)
- ACP harness enabled in openclaw.json
- AGENTS.md rule: all coding goes via Claude Code, not inline

Make sure he understands the workflow:
1. Tell KilmurryBot what to build
2. Bot spawns Claude Code via ACP → builds it
3. Bot reviews and reports back
4. Bot's Opus tokens only used for thinking/directing, not file writing

Show him how to invoke it: "Use Claude Code to add a new Forecasting section to the Revenue page"

## Priority 4: OpenClaw upgrade confirmation
Kilmurry is now on v2026.4.12 (upgraded remotely yesterday).
Gateway was restarted. Active Memory is live.
Should be noticeably sharper — mention it to Jack so he notices the improvement.

## Server details (for reference)
- IP: 172.239.98.61
- User: clawuser / Castletroy1995! (also sudo password)
- MC: http://172.239.98.61:3333 (Jack), http://172.239.98.61:3334 (Kate)
- OpenClaw: v2026.4.12 ✅
- Claude Code: v2.1.104, authenticated ✅
