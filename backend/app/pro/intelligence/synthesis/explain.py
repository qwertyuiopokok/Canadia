
def explain_similarity(user_context: dict, similar_cases: list):
# Module: explain.py
# Génération de réponses explicables à partir des cas

from app.pro.intelligence.trajectory_engine.patterns import extract_common_patterns

def explain_similarity(user_context: dict, similar_cases: list):
	return {
		"summary": (
			"Sur la base de trajectoires publiques d'entreprises "
			"présentant des profils similaires, "
			"voici des patterns observés."
		),
		"patterns": extract_common_patterns(similar_cases),
		"disclaimer": (
			"Ces informations sont issues de données publiques "
			"et d'analyses comparatives. "
			"Elles ne constituent pas un conseil financier ou stratégique."
		)
	}

def synthesize_answer(question: str, context: dict, similar_cases: list) -> str:
	if not similar_cases:
		return (
			"Aucun cas public strictement similaire n’a été identifié. "
			"La réponse suivante repose sur des principes organisationnels généraux."
		)

	patterns = extract_common_patterns(similar_cases)

	response = (
		"Sur la base de trajectoires publiques d’organisations similaires, "
		"voici des patterns observés :\n\n"
	)

	for p, count in patterns[:5]:
		response += f"- {p} (observé dans {count} cas similaires)\n"

	response += (
		"\nCes éléments servent à éclairer la réflexion, "
		"sans constituer une recommandation prescriptive."
	)

	return response
