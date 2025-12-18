
# Module: patterns.py
# Analyse de parcours et détection de patterns

def extract_common_patterns(cases: list) -> dict:
	patterns = {}

	for c in cases:
		for step in c["trajectory"]:
			patterns[step] = patterns.get(step, 0) + 1

	return sorted(
		patterns.items(),
		key=lambda x: x[1],
		reverse=True
	)
