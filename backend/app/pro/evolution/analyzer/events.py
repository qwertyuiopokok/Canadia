def extract_structuring_events(text: str) -> list:
	events = []

	text = text.lower()

	if "acquisition" in text or "fusion" in text:
		events.append("merger_acquisition")

	if "reorganization" in text or "restructuring" in text:
		events.append("restructuring")

	if "hired" in text or "new employees" in text:
		events.append("hiring_phase")

	if "expansion" in text:
		events.append("expansion")

	return events
# Module: events.py
# Extraction de signaux d'événements
