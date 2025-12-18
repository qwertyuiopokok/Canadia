# Placeholder upsert_gap for compatibility
def upsert_gap(gap_id: str, data: dict):
	"""
	Insert or update a gap entry in the evolution store.
	"""
	# Implement actual persistence logic here
	print(f"Upsert gap: {gap_id} -> {data}")
from .database import get_connection

def insert_source_proposal(gap_id: int, proposal: dict):
	conn = get_connection()
	cur = conn.cursor()

	cur.execute("""
	INSERT INTO source_proposals (
		gap_id,
		source_name,
		source_url,
		method,
		notes,
		status,
		created_at
	)
	VALUES (?, ?, ?, ?, ?, 'proposed', datetime('now'))
	""", (
		gap_id,
		proposal["source_name"],
		proposal["source_url"],
		proposal["method"],
		proposal.get("notes", "")
	))

	conn.commit()
	conn.close()
# Stockage des gaps et propositions pour l'évolution
