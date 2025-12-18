
import sqlite3
from datetime import datetime
from app.storage.database import get_connection

def init_feedback_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fingerprint TEXT,
        value INTEGER, -- 1 = like, -1 = dislike
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_feedback(fingerprint: str, value: int):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO feedback (fingerprint, value, created_at)
    VALUES (?, ?, ?)
    """, (fingerprint, value, datetime.utcnow().isoformat()))

    conn.commit()
    conn.close()


def get_feedback_score_by_fingerprint(fp: str) -> int:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT COALESCE(SUM(value), 0)
    FROM feedback
    WHERE fingerprint = ?
    """, (fp,))

    score = cur.fetchone()[0]
    conn.close()
    return score
