"""
Central content storage abstraction
"""

import json
from .database import get_connection

def get_by_fingerprint(fp: str):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute(
		"SELECT * FROM contents WHERE fingerprint = ?",
		(fp,)
	)
	row = cur.fetchone()
	conn.close()

	if not row:
		return None

	return {
		"fingerprint": row[0],
		"title": row[1],
		"content": row[2],
		"url": row[3],
		"source": {
			"id": row[4],
			"name": row[5],
			"type": row[6]
		},
		"themes": json.loads(row[7]),
		"geography": json.loads(row[8]),
		"last_updated": row[9],
		"status": row[10]
	}

def save(content: dict):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
	INSERT OR REPLACE INTO contents
	VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
	""", (
		content["fingerprint"],
		content["title"],
		content["content"],
		content.get("url"),
		content["source"]["id"],
		content["source"]["name"],
		content["source"]["type"],
		json.dumps(content.get("themes", [])),
		json.dumps(content.get("geography", {})),
		content.get("last_updated"),
		content.get("status")
	))

	conn.commit()
	conn.close()

def save_history(fp: str, previous_content: str, updated_at: str):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
	INSERT INTO content_history (fingerprint, previous_content, updated_at)
	VALUES (?, ?, ?)
	""", (fp, previous_content, updated_at))

	conn.commit()
	conn.close()

def all_contents():
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("SELECT fingerprint FROM contents")
	fps = [row[0] for row in cur.fetchall()]
	conn.close()

	return [get_by_fingerprint(fp) for fp in fps]
