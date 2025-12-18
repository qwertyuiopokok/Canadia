
# Module: normalize.py
# Structure commune pour la normalisation des cas

def normalize_case(raw: dict) -> dict:
	return {
		"company_profile": {
			"sector": raw.get("sector"),
			"size_range": raw.get("size_range"),
			"region": raw.get("region")
		},
		"trajectory": raw.get("events", []),
		"context": raw.get("context"),
		"outcomes": raw.get("outcomes"),
		"time_horizon": raw.get("years")
	}
