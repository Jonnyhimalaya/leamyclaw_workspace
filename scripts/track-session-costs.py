#!/usr/bin/env python3
"""Track OpenClaw session costs to a JSON ledger file.
Run periodically (cron/heartbeat) to capture session snapshots.
Each entry records a point-in-time snapshot of active sessions."""

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

LEDGER_PATH = os.path.expanduser('~/.openclaw/workspace/session-costs.json')
GATEWAY_URL = 'http://127.0.0.1:18789'

def get_token():
    config_path = os.path.expanduser('~/.openclaw/openclaw.json')
    with open(config_path) as f:
        raw = f.read()
    # Simple extraction - find token value
    import re
    m = re.search(r'token["\s:]+["\']([a-f0-9]+)["\']', raw)
    return m.group(1) if m else None

def get_sessions(token):
    req = urllib.request.Request(
        f'{GATEWAY_URL}/tools/invoke',
        data=json.dumps({'tool': 'sessions_list', 'args': {'limit': 50}}).encode(),
        headers={
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
        }
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read())

    result = data.get('result', {})
    # Parse gateway response format
    if 'content' in result:
        for c in result['content']:
            if c.get('type') == 'text':
                parsed = json.loads(c['text'])
                return parsed if isinstance(parsed, list) else parsed.get('sessions', [])
    if 'details' in result:
        d = result['details']
        return d if isinstance(d, list) else d.get('sessions', [])
    return []

def load_ledger():
    if os.path.exists(LEDGER_PATH):
        with open(LEDGER_PATH) as f:
            return json.load(f)
    return {'snapshots': [], 'sessions': {}}

def save_ledger(ledger):
    with open(LEDGER_PATH, 'w') as f:
        json.dump(ledger, f, indent=2)

def main():
    token = get_token()
    if not token:
        print('ERROR: Could not find gateway token')
        sys.exit(1)

    sessions = get_sessions(token)
    ledger = load_ledger()
    now = datetime.now(timezone.utc).isoformat()
    today = now[:10]

    # Update per-session historical data
    for s in sessions:
        key = s.get('key', 'unknown')
        tokens = s.get('totalTokens', 0)
        cost = s.get('estimatedCostUsd', 0)
        model = s.get('model', 'unknown')
        channel = s.get('lastChannel', s.get('channel', 'unknown'))
        status = s.get('status', 'unknown')
        session_id = s.get('sessionId', '')

        if key not in ledger['sessions']:
            ledger['sessions'][key] = {
                'firstSeen': now,
                'model': model,
                'channel': channel,
                'sessionId': session_id,
                'history': [],
            }

        entry = ledger['sessions'][key]
        entry['lastSeen'] = now
        entry['lastStatus'] = status
        entry['currentTokens'] = tokens
        entry['currentCost'] = cost
        entry['model'] = model
        entry['channel'] = channel

        # Only append history if tokens changed since last entry
        history = entry['history']
        if not history or history[-1]['tokens'] != tokens:
            history.append({
                'timestamp': now,
                'tokens': tokens,
                'cost': round(cost, 6),
            })

    # Daily snapshot (aggregate)
    total_tokens = sum(s.get('totalTokens', 0) for s in sessions)
    total_cost = sum(s.get('estimatedCostUsd', 0) for s in sessions)
    active_count = sum(1 for s in sessions if s.get('status') == 'running')

    # Check if we already have a snapshot for today
    existing_today = [i for i, snap in enumerate(ledger['snapshots']) if snap['date'] == today]
    snapshot = {
        'date': today,
        'timestamp': now,
        'totalSessions': len(sessions),
        'activeSessions': active_count,
        'totalTokens': total_tokens,
        'totalCost': round(total_cost, 6),
        'sessionBreakdown': {
            s.get('key', '?'): {
                'tokens': s.get('totalTokens', 0),
                'cost': round(s.get('estimatedCostUsd', 0), 6),
                'model': s.get('model', '?'),
                'channel': s.get('lastChannel', '?'),
            }
            for s in sessions
        }
    }

    if existing_today:
        # Update today's snapshot (keep the latest)
        ledger['snapshots'][existing_today[-1]] = snapshot
    else:
        ledger['snapshots'].append(snapshot)

    save_ledger(ledger)

    # Print summary
    print(f'OK|sessions={len(sessions)},tokens={total_tokens},cost=${total_cost:.2f},tracked={len(ledger["sessions"])}')

if __name__ == '__main__':
    main()
