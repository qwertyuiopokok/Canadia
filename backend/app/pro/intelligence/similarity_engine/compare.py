
# Module: compare.py
# Matching intelligent entre cas

def compute_similarity(case_a: dict, case_b: dict) -> float:
	score = 0

	if case_a["company_profile"]["sector"] == case_b["company_profile"]["sector"]:
		score += 0.4

	if case_a["company_profile"]["size_range"] == case_b["company_profile"]["size_range"]:
		score += 0.3

	overlap = set(case_a["trajectory"]) & set(case_b["trajectory"])
	score += 0.3 * len(overlap)

	return round(score, 2)
