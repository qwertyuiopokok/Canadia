ALLOWED_EVENTS = {
	"merger_acquisition",
	"restructuring",
	"hiring_phase",
	"expansion",
	"process_change"
}

def validate_case(case: dict) -> bool:
	for e in case["trajectory"]:
		if e not in ALLOWED_EVENTS:
			return False
	return True
# Module: rules.py
# Règles de filtrage et validation des signaux
