"""
Gestion de l'évolution : logs de questions, détection de gaps, propositions de sources.
"""
from datetime import datetime
from app.storage.database import get_connection

def init_evolution_tables():
    conn = get_connection()
    cur = conn.cursor()

    # Questions et résultats
    cur.execute("""
    CREATE TABLE IF NOT EXISTS question_log (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      question TEXT NOT NULL,
      province TEXT,
      region TEXT,
      coverage TEXT,          -- none | partial | full
      used_web INTEGER,       -- 0/1
      created_at TEXT
    )
    """)

    # "Gaps" détectés (manques de contenu)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS gaps (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      key TEXT UNIQUE,        -- ex: logement:QC:regie_loyer
      theme TEXT,
      province TEXT,
      region TEXT,
      example_question TEXT,
      count INTEGER DEFAULT 1,
      status TEXT DEFAULT 'open',  -- open | proposed | approved | done
      priority INTEGER DEFAULT 50,
      updated_at TEXT
    )
    """)

    # Propositions de sources/connecteurs
    cur.execute("""
    CREATE TABLE IF NOT EXISTS source_proposals (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      gap_id INTEGER,
      source_name TEXT,
      source_url TEXT,
      method TEXT,            -- rss | api | web
      notes TEXT,
      status TEXT DEFAULT 'proposed', -- proposed | approved | rejected
      created_at TEXT
    )
    """)

    conn.commit()
    conn.close()

def log_question(question: str, coverage: str, used_web: bool, province: str=None, region: str=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
      INSERT INTO question_log (question, province, region, coverage, used_web, created_at)
      VALUES (?, ?, ?, ?, ?, ?)
    """, (question, province, region, coverage, int(used_web), datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()

def upsert_gap(key: str, theme: str, province: str, region: str, example_question: str, priority: int = 50):
    conn = get_connection()
    cur = conn.cursor()

    now = datetime.utcnow().isoformat()
    cur.execute("SELECT id, count FROM gaps WHERE key = ?", (key,))
    row = cur.fetchone()

    if row:
        gap_id, count = row
        cur.execute("""
          UPDATE gaps SET count=?, updated_at=?, priority=MIN(priority, ?)
          WHERE id=?
        """, (count + 1, now, priority, gap_id))
    else:
        cur.execute("""
          INSERT INTO gaps (key, theme, province, region, example_question, count, status, priority, updated_at)
          VALUES (?, ?, ?, ?, ?, 1, 'open', ?, ?)
        """, (key, theme, province, region, example_question, priority, now))

    conn.commit()
    conn.close()
