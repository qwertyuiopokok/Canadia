def init_db():
	conn = get_connection()
	cur = conn.cursor()

	# Table principale
	cur.execute("""
	CREATE TABLE IF NOT EXISTS contents (
		fingerprint TEXT PRIMARY KEY,
		title TEXT,
		content TEXT,
		url TEXT,
		source_id TEXT,
		source_name TEXT,
		source_type TEXT,
		themes TEXT,
		geography TEXT,
		last_updated TEXT,
		status TEXT
	)
	""")

	# Historique des mises à jour
	cur.execute("""
	CREATE TABLE IF NOT EXISTS content_history (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		fingerprint TEXT,
		previous_content TEXT,
		updated_at TEXT
	)
	""")

	conn.commit()
	conn.close()
"""
SQLite database connection utilities
"""
import sqlite3
from pathlib import Path

DB_PATH = Path("backend/app/storage/canadia.db")

def get_connection():
	DB_PATH.parent.mkdir(parents=True, exist_ok=True)
	return sqlite3.connect(DB_PATH)
