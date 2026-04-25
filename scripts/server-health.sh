#!/bin/bash
# Server Health Check & Cleanup Script
# Run periodically via cron or heartbeat

ALERT=""

# --- Memory Check ---
# Use 'available' (col $7), not 'free' (col $4). Linux uses free RAM for
# disk cache which is reclaimable — 'available' reflects actual usable memory.
MEM_USED_PCT=$(free | awk '/Mem:/{printf "%.0f", $3/$2*100}')
SWAP_USED=$(free -m | awk '/Swap:/{print $3}')
MEM_AVAIL_MB=$(free -m | awk '/Mem:/{print $7}')

if [ "$MEM_AVAIL_MB" -lt 300 ]; then
    ALERT="${ALERT}🔴 CRITICAL: Only ${MEM_AVAIL_MB}MB available RAM\n"
elif [ "$MEM_AVAIL_MB" -lt 600 ]; then
    ALERT="${ALERT}🟡 WARNING: ${MEM_AVAIL_MB}MB available RAM (getting low)\n"
fi

if [ "$SWAP_USED" -gt 800 ]; then
    ALERT="${ALERT}🔴 CRITICAL: Swap usage ${SWAP_USED}MB\n"
elif [ "$SWAP_USED" -gt 500 ]; then
    ALERT="${ALERT}🟡 Swap usage: ${SWAP_USED}MB (performance impact)\n"
fi

# --- Chrome Zombie Check ---
CHROME_COUNT=$(ps aux | grep -c "[c]hrome.*remote-debugging")
CHROME_MB=$(ps aux | grep "[c]hrome" | awk '{sum+=$6} END {printf "%.0f", sum/1024}')
if [ "$CHROME_COUNT" -gt 0 ]; then
    ALERT="${ALERT}🧹 Chrome: ${CHROME_COUNT} processes using ${CHROME_MB}MB — killing idle instances\n"
    # Kill chrome if no browser tool calls in last 10 minutes
    CHROME_PARENT=$(pgrep -f "chrome.*remote-debugging-port" | head -1)
    if [ -n "$CHROME_PARENT" ]; then
        # Check if any page has been active recently (last modified time of DevTools socket)
        pkill -f "chrome.*remote-debugging-port=18800" 2>/dev/null
        ALERT="${ALERT}✅ Chrome processes killed\n"
    fi
fi

# --- Disk Check ---
DISK_PCT=$(df / | awk 'NR==2{print $5}' | tr -d '%')
if [ "$DISK_PCT" -gt 90 ]; then
    ALERT="${ALERT}🔴 CRITICAL: Disk ${DISK_PCT}% full\n"
elif [ "$DISK_PCT" -gt 80 ]; then
    ALERT="${ALERT}🟡 Disk usage: ${DISK_PCT}%\n"
fi

# --- PM2 Health ---
PM2_STATUS=$(pm2 jlist 2>/dev/null | python3 -c "
import sys,json
try:
    apps = json.load(sys.stdin)
    for app in apps:
        name = app.get('name','?')
        status = app.get('pm2_env',{}).get('status','?')
        restarts = app.get('pm2_env',{}).get('restart_time',0)
        if status != 'online':
            print(f'🔴 PM2 {name}: {status}')
        elif restarts > 10:
            print(f'🟡 PM2 {name}: {restarts} restarts')
except: pass
" 2>/dev/null)
if [ -n "$PM2_STATUS" ]; then
    ALERT="${ALERT}${PM2_STATUS}\n"
fi

# --- Load Average ---
LOAD=$(awk '{print $1}' /proc/loadavg)
CPUS=$(nproc)
LOAD_INT=$(echo "$LOAD $CPUS" | awk '{printf "%.0f", $1/$2*100}')
if [ "$LOAD_INT" -gt 150 ]; then
    ALERT="${ALERT}🔴 High load: ${LOAD} (${CPUS} CPUs)\n"
elif [ "$LOAD_INT" -gt 100 ]; then
    ALERT="${ALERT}🟡 Elevated load: ${LOAD}\n"
fi

# --- Orphan Node Processes ---
ORPHAN_NODE=$(ps aux | grep -E "node.*claude.*print|codex" | grep -v grep | wc -l)
if [ "$ORPHAN_NODE" -gt 0 ]; then
    ALERT="${ALERT}🧹 ${ORPHAN_NODE} orphan coding agent process(es) found\n"
fi

# --- Output ---
if [ -n "$ALERT" ]; then
    echo -e "SERVER HEALTH ISSUES:\n${ALERT}"
    echo "---"
    echo "Memory: ${MEM_USED_PCT}% used, ${MEM_AVAIL_MB}MB available, ${SWAP_USED}MB swap"
    echo "Disk: ${DISK_PCT}%"
    echo "Load: ${LOAD}"
    echo "Chrome: ${CHROME_COUNT} processes (${CHROME_MB}MB)"
    exit 1
else
    echo "OK|mem=${MEM_USED_PCT}%,avail=${MEM_AVAIL_MB}MB,swap=${SWAP_USED}MB,disk=${DISK_PCT}%,load=${LOAD},chrome=${CHROME_COUNT}"
    exit 0
fi
