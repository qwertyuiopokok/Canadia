def propose_sources_for_gap(gap):
	"""
	Génère automatiquement des propositions de sources
	(à valider par un humain).
	"""
	base_sources = [
		{
			"name": "Gouvernement du Canada",
			"url": "https://www.canada.ca",
			"method": "rss"
		},
		{
			"name": "Gouvernement provincial",
			"url": f"https://www.{gap['province'].lower()}.ca",
			"method": "rss"
		},
		{
			"name": "Données ouvertes",
			"url": "https://open.canada.ca",
			"method": "api"
		}
	]

	return base_sources[:PROPOSED_SOURCES_PER_GAP]
# seuils configurables
MIN_QUESTIONS_PER_DAY = 20
COVERAGE_THRESHOLD = 0.5
PROPOSED_SOURCES_PER_GAP = 3


from datetime import datetime, timedelta
from collections import defaultdict
from app.storage.database import get_connection
from app.storage.evolution_store import upsert_gap

def analyze_daily_gaps():
	"""
	Analyse les questions des dernières 24h
	et détecte les thèmes sous-couverts.
	"""
	conn = get_connection()
	cur = conn.cursor()

	since = (datetime.utcnow() - timedelta(days=1)).isoformat()

	cur.execute("""
		SELECT question, coverage, province, region
		FROM question_log
		WHERE created_at >= ?
	""", (since,))
	rows = cur.fetchall()
	conn.close()

	stats = defaultdict(lambda: {"total": 0, "covered": 0, "example": None})

	for q, coverage, province, region in rows:
		key = (province or "CAN", region or "ALL")

		stats[key]["total"] += 1
		if coverage == "full":
			stats[key]["covered"] += 1

		if not stats[key]["example"]:
			stats[key]["example"] = q

	for (province, region), data in stats.items():
		total = data["total"]
		covered = data["covered"]
		coverage_ratio = covered / total if total else 0

		if (
			total >= MIN_QUESTIONS_PER_DAY
			and coverage_ratio < COVERAGE_THRESHOLD
		):
			gap_key = f"auto:{province}:{region}"

			upsert_gap(
				key=gap_key,
				theme="auto-detected",
				province=province,
				region=region,
				example_question=data["example"],
				priority=10  # très haute priorité
			)
# Logique de décision pour l'évolution du système
