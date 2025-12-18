try:
	from ..storage.evolution_store import insert_source_proposal
	from .llm_suggest_sources import llm_suggest_sources
except (ImportError, ValueError):
	from app.storage.evolution_store import insert_source_proposal
	from app.core.llm_suggest_sources import llm_suggest_sources

def auto_propose_sources_for_gap(gap: dict):
	proposals = recommend_sources(gap)

	for p in proposals:
		insert_source_proposal(gap["id"], p)
# Génère automatiquement des sources pertinentes selon le thème et la localisation du gap
def recommend_sources(gap: dict) -> list:
	"""
	Génère automatiquement des sources pertinentes
	selon le thème et la localisation du gap.
	"""
	theme = gap.get("theme")
	province = gap.get("province", "CAN")

	sources = []

	# --- Sources fédérales (toujours pertinentes)
	sources.append({
		"source_name": "Gouvernement du Canada",
		"source_url": "https://www.canada.ca",
		"method": "rss",
		"notes": f"Source fédérale pertinente pour {theme}"
	})

	# --- Sources provinciales
	if province == "QC":
		sources.append({
			"source_name": "Gouvernement du Québec",
			"source_url": "https://www.quebec.ca",
			"method": "rss",
			"notes": f"Source provinciale Québec — {theme}"
		})

	if province == "ON":
		sources.append({
			"source_name": "Government of Ontario",
			"source_url": "https://www.ontario.ca",
			"method": "rss",
			"notes": f"Ontario official source — {theme}"
		})

	# --- Données ouvertes (très forte valeur)
	sources.append({
		"source_name": "Données ouvertes Canada",
		"source_url": "https://open.canada.ca",
		"method": "api",
		"notes": "Données ouvertes officielles"
	})

	# --- Filtrage par thème (exemples)
	if theme == "logement":
		sources.append({
			"source_name": "SCHL (Société canadienne d'hypothèques et de logement)",
			"source_url": "https://www.cmhc-schl.gc.ca",
			"method": "rss",
			"notes": "Autorité fédérale sur le logement"
		})

	# --- Suggestions LLM (toujours à la fin)
	sources.extend(llm_suggest_sources(theme, province))

	return sources[:5]  # limite volontaire
# Module pour recommander des sources en fonction des gaps ou besoins détectés
