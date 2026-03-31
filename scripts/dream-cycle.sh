#!/bin/bash
# dream-cycle.sh — Nightly memory consolidation
# Finds daily logs older than 7 days, spawns a Sonnet sub-agent to distil them
# into MEMORY.md, then archives the processed files.

WORKSPACE="/home/jonny/.openclaw/workspace"
MEMORY_DIR="$WORKSPACE/memory"
ARCHIVE_DIR="$MEMORY_DIR/archive"
MEMORY_FILE="$WORKSPACE/MEMORY.md"
CUTOFF_DAYS=7

mkdir -p "$ARCHIVE_DIR"

# Find daily logs older than N days (exclude archive dir)
OLD_LOGS=$(find "$MEMORY_DIR" -maxdepth 1 -name "20*.md" -mtime +$CUTOFF_DAYS | sort)

if [ -z "$OLD_LOGS" ]; then
  echo "Dream Cycle: no logs older than $CUTOFF_DAYS days. Nothing to do."
  exit 0
fi

echo "Dream Cycle: found logs to consolidate:"
echo "$OLD_LOGS"

# Build the content to summarise
CONTENT=""
for f in $OLD_LOGS; do
  FILENAME=$(basename "$f")
  CONTENT="$CONTENT\n\n---\n## From: $FILENAME\n$(cat "$f")"
done

# Current MEMORY.md content
CURRENT_MEMORY=$(cat "$MEMORY_FILE")

# Spawn Sonnet sub-agent to consolidate
openclaw run \
  --agent marketing \
  --model anthropic/claude-sonnet-4-6 \
  --print \
  --input "You are doing a nightly Dream Cycle memory consolidation for Jonny's AI assistant workspace.

Here are old daily log files to process:
$CONTENT

Here is the current MEMORY.md:
$CURRENT_MEMORY

Your task:
1. Read through the daily logs carefully
2. Extract anything worth preserving long-term: key decisions, lessons learned, important facts, project milestones, user preferences
3. Skip raw task logs, heartbeat entries, and server health checks — those don't need to survive long-term
4. Output ONLY new content to append to MEMORY.md — formatted as markdown sections
5. If there is nothing worth preserving, output exactly: NOTHING_TO_ADD

Do not repeat anything already in MEMORY.md. Be concise and distilled." 2>/dev/null

# Note: The actual append to MEMORY.md and archiving is handled by the cron wrapper
# since openclaw run output needs to be captured. See cron-dream-cycle.sh for the full flow.

echo "Dream Cycle: consolidation complete."
echo "Files to archive: $OLD_LOGS"

# Archive the processed logs
for f in $OLD_LOGS; do
  mv "$f" "$ARCHIVE_DIR/"
  echo "Archived: $(basename $f)"
done
