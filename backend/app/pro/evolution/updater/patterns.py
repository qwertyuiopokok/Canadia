def update_patterns(cases: list):
	patterns = {}

	for c in cases:
		for step in c["trajectory"]:
			patterns[step] = patterns.get(step, 0) + 1

	return patterns
def build_trajectory(events: list, context: dict) -> dict:
	return {
		"company_profile": {
			"sector": context.get("sector"),
			"region": context.get("region"),
			"size_range": context.get("size_range")
		},
		"trajectory": events,
		"confidence": "public_observed"
	}
# Module: patterns.py
# Mise à jour des patterns observés à partir de nouveaux signaux
