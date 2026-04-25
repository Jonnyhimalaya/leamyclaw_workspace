echo "logged"

## Don't eavesdrop on client agent conversations (2026-04-22)
Jonny corrected me for reading Jack's session JSONL files to check for replies to a report I'd sent.
Rule: do not read other agents' session transcripts unless explicitly asked. Health/status checks (systemctl, ports, disk) are fine. Session contents are private — same boundary as client-to-client.
Acceptable: "is the service running?" / "did the delivery succeed?" (check send-side log only).
Not acceptable: "what did Jack say back?" / reading inbound messages to other agents.

## NO GUESSING — verify first (2026-04-25)
Jonny's words: "twice recently you have guessed and been wrong. No more guessing. That doesn't help anyone. Place a hard rule that you no longer guess, you always verify first."

Both incidents this week:
1. Told Jonny his setup used a separate Anthropic API key, when in reality his `anthropic:claw` profile is `sk-ant-oat01-...` — an OAuth bearer, identical shape to Aidan's. I'd never actually checked his auth-profiles.json before claiming the difference.
2. Earlier context bleed between Aidan and Dano deployments — inferred client-specific commands instead of looking up each client's record fresh.

The pattern: confident technical claims based on inference / pattern-matching / what "usually" applies, instead of verification.

New rule (also pinned to AGENTS.md Core Rules):
- Before any technical claim about config, billing, system state, API behaviour, or what's installed: VERIFY by reading the actual file, running the actual command, or checking the actual log.
- If verification isn't possible right now, say so explicitly. Don't fill the gap with confident inference.
- Pattern-matching across clients counts as guessing.
- Memory of "how it usually works" counts as guessing unless I just verified it for the current target.

Why this matters operationally: in a consultancy, every wrong technical claim erodes trust faster than any correct one builds it. A hedged "I haven't checked yet" is always better than a confident wrong answer.
