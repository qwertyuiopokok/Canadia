
# Module: news_events.py
# Collecte de cas réels à partir d'événements d'actualité

def extract_events(article: dict) -> list:
	"""
	Extrait des événements organisationnels
	(fusion, embauche, expansion, pivot).
	"""
	events = []

	text = article["content"].lower()

	if "acquisition" in text or "fusion" in text:
		events.append("merger_acquisition")

	if "hiring" in text or "new employees" in text:
		events.append("hiring_phase")

	if "reorganization" in text:
		events.append("restructuring")

	return events
