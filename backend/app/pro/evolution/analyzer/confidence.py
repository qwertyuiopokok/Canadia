def confidence_score(case: dict) -> float:
	score = 0.5

	if case.get("confidence") == "public_observed":
		score += 0.3

	if case.get("sources"):
		score += 0.2

	return min(score, 1.0)
# Module: confidence.py
# Extraction et calcul de la confiance des signaux
