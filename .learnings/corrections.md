echo "logged"

## Don't eavesdrop on client agent conversations (2026-04-22)
Jonny corrected me for reading Jack's session JSONL files to check for replies to a report I'd sent.
Rule: do not read other agents' session transcripts unless explicitly asked. Health/status checks (systemctl, ports, disk) are fine. Session contents are private — same boundary as client-to-client.
Acceptable: "is the service running?" / "did the delivery succeed?" (check send-side log only).
Not acceptable: "what did Jack say back?" / reading inbound messages to other agents.
