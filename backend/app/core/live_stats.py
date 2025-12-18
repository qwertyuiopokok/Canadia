from collections import defaultdict
from datetime import datetime

LIVE_STATS = defaultdict(lambda: {
    "count": 0,
    "full": 0,
    "partial": 0,
    "none": 0,
    "last_seen": None
})

WINDOW_MINUTES = 30  # fenêtre glissante

def update_live_stats(theme: str, coverage: str):
    key = theme
    stat = LIVE_STATS[key]
    stat["count"] += 1
    stat[coverage] += 1
    stat["last_seen"] = datetime.utcnow()
