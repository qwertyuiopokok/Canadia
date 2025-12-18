def add_case(case: dict):
	CASE_INDEX.append(case)

# Module: index.py
# Indexation et accès à la base de cas

CASE_INDEX = []  # Placeholder: should be populated with normalized cases

def find_similar_cases(context: dict, limit: int = 5):
	results = []

	for case in CASE_INDEX:
		score = 0

		if case["company_profile"]["sector"] == context.get("sector"):
			score += 0.4

		if case["company_profile"]["size_range"] == context.get("company_size"):
			score += 0.3

		overlap = set(case["trajectory"]) & set(context.get("trajectory", []))
		score += 0.3 * len(overlap)

		if score > 0.4:
			results.append((score, case))

	results.sort(key=lambda x: x[0], reverse=True)
	return [c for _, c in results[:limit]]
