from app.storage.evolution_store import upsert_gap

def create_gap_now(theme: str, question: str, province: str=None):
    key = f"realtime:{theme}:{province or 'CAN'}"

    from app.core.live_stats import update_live_stats, LIVE_STATS
    from app.core.anomaly import detect_anomaly
    from app.core.realtime_gap import create_gap_now


    upsert_gap(
        key=key,
        theme=theme,
        province=province or "CAN"
    )

from app.core.question import analyze
from app.core.retrieve import retrieve_internal
from app.core.coverage import evaluate

from collections import defaultdict
from datetime import datetime

# stats en mémoire (rapide)
LIVE_STATS = defaultdict(lambda: {
    "count": 0,
    "full": 0,
    "partial": 0,
    "none": 0,
    "last_seen": None
})

WINDOW_MINUTES = 30  # fenêtre glissante

def update_live_stats(question, analysis, coverage):
    theme = analysis.get("theme", "autre")
    key = theme
    stat = LIVE_STATS[key]


    if total < 5:
        return False  # trop tôt

    coverage_ratio = full / total if total else 0

    # règle simple mais efficace
    if total >= 10 and coverage_ratio < 0.4:
        return True

    return False

def maybe_create_gap(question, analysis, coverage):
    # TODO: Immediately create a gap if needed
    pass

def ask(question: str):
    """
    Pipeline complet pour traiter une question et générer une réponse.
    Args:
        question (str): Question utilisateur.
    Returns:
        dict: Réponse, confiance, usage web, sources.
    """
    analysis = analyze(question)

    internal = retrieve_internal(analysis["domain"])
    coverage = evaluate(internal)

    # Logging and live stats/anomaly/gap
    log_question(question, analysis, coverage)
    update_live_stats(question, analysis, coverage)
    detect_anomaly(question, analysis, coverage)
    maybe_create_gap(question, analysis, coverage)

    external = []
    if coverage != "full":
        external = search_web(question)

    merged = merge(internal, external)

    answer = generate(question, merged)
    confidence = compute_confidence(merged)


    return {
        "answer": answer,
        "confidence": confidence,
        "used_web": coverage != "full",
        "sources": list({c["source"] for c in merged})
    }

# --- FIN DE LA LISTE DE DICTIONNAIRES ---

CONTENT_STORE = [
    {"titre": "Procédure pour bénéficier de l'aide alimentaire", "contenu": "Remplissez le formulaire fourni par l'école en début d'année.", "themes": ["éducation", "procédure"], "source": "École locale"},
    # Emploi
    {"titre": "Aide à la recherche d'emploi", "contenu": "Emploi-Québec propose des ateliers et du coaching pour les chercheurs d'emploi.", "themes": ["emploi", "aide"], "source": "Emploi-Québec"},
    {"titre": "Contact Emploi-Québec", "contenu": "Appelez le 1-877-767-8773 ou visitez le site emploiquebec.gouv.qc.ca.", "themes": ["emploi", "contact"], "source": "Emploi-Québec"},
    {"titre": "Procédure pour s'inscrire à Emploi-Québec", "contenu": "Créez un compte en ligne et remplissez votre profil de chercheur d'emploi.", "themes": ["emploi", "procédure"], "source": "Emploi-Québec"},
    {"titre": "Programme de subvention salariale", "contenu": "Des subventions sont offertes aux employeurs pour l'embauche de certains candidats.", "themes": ["emploi", "aide"], "source": "Emploi-Québec"},
    {"titre": "Contact subvention salariale", "contenu": "Contactez votre centre local d'emploi pour plus d'informations.", "themes": ["emploi", "contact"], "source": "Emploi-Québec"},
    {"titre": "Procédure pour demander une subvention salariale", "contenu": "Remplissez le formulaire de demande disponible sur le site d'Emploi-Québec.", "themes": ["emploi", "procédure"], "source": "Emploi-Québec"},
    # Famille
    {"titre": "Aide pour les familles monoparentales", "contenu": "Des allocations et des services de soutien sont disponibles.", "themes": ["famille", "aide"], "source": "Gouvernement du Québec"},
    {"titre": "Contact allocations familiales", "contenu": "Appelez Revenu Québec au 1-800-267-6299.", "themes": ["famille", "contact"], "source": "Revenu Québec"},
    {"titre": "Procédure pour demander l'allocation familiale", "contenu": "Faites la demande en ligne sur le site de Revenu Québec.", "themes": ["famille", "procédure"], "source": "Revenu Québec"},
    {"titre": "Programme de soutien aux proches aidants", "contenu": "Des ressources et du répit sont offerts aux proches aidants.", "themes": ["famille", "aide"], "source": "Gouvernement du Québec"},
    {"titre": "Contact soutien proches aidants", "contenu": "Contactez l'Appui au 1-855-852-7784.", "themes": ["famille", "contact"], "source": "L'Appui"},
    {"titre": "Procédure pour obtenir du répit", "contenu": "Contactez un organisme local et planifiez une évaluation des besoins.", "themes": ["famille", "procédure"], "source": "L'Appui"},
    # Immigration
    {"titre": "Aide à l'intégration des nouveaux arrivants", "contenu": "Des services d'accueil et d'orientation sont offerts gratuitement.", "themes": ["immigration", "aide"], "source": "Gouvernement du Québec"},
    {"titre": "Contact services d'intégration", "contenu": "Appelez le 1-877-672-3460 pour joindre le ministère de l'Immigration.", "themes": ["immigration", "contact"], "source": "MIFI"},
    {"titre": "Procédure pour obtenir un certificat de sélection", "contenu": "Remplissez le formulaire en ligne et payez les frais requis.", "themes": ["immigration", "procédure"], "source": "MIFI"},
    {"titre": "Programme de francisation", "contenu": "Des cours de français gratuits sont offerts aux nouveaux arrivants.", "themes": ["immigration", "aide"], "source": "MIFI"},
    {"titre": "Contact francisation", "contenu": "Inscrivez-vous sur le site du ministère ou appelez le 1-877-672-3460.", "themes": ["immigration", "contact"], "source": "MIFI"},
    {"titre": "Procédure d'inscription à la francisation", "contenu": "Créez un compte en ligne et choisissez votre établissement.", "themes": ["immigration", "procédure"], "source": "MIFI"},
    # Transport
    {"titre": "Aide pour le transport adapté", "contenu": "Les personnes à mobilité réduite peuvent bénéficier d'un service de transport adapté.", "themes": ["transport", "aide"], "source": "STM"},
    {"titre": "Contact transport adapté", "contenu": "Appelez la STM au 514-280-8211, option 4.", "themes": ["transport", "contact"], "source": "STM"},
    {"titre": "Procédure pour s'inscrire au transport adapté", "contenu": "Remplissez le formulaire sur le site de la STM et joignez un certificat médical.", "themes": ["transport", "procédure"], "source": "STM"},
    {"titre": "Programme de covoiturage", "contenu": "Des plateformes de covoiturage facilitent les déplacements entre régions.", "themes": ["transport", "aide"], "source": "AMT"},
    {"titre": "Contact covoiturage", "contenu": "Consultez le site de l'AMT ou appelez au 514-287-8726.", "themes": ["transport", "contact"], "source": "AMT"},
    {"titre": "Procédure pour s'inscrire au covoiturage", "contenu": "Créez un compte sur la plateforme de covoiturage de votre région.", "themes": ["transport", "procédure"], "source": "AMT"}
]

def ask(question: str, niveau: int = 1):
    analysis = analyse_question(question)
    results = search_content(CONTENT_STORE, analysis)
    coverage = evaluate_coverage(results)

    qtype = analysis.get("type", "information")
    sources = results[0]["source"] if results else "https://www.rdl.gouv.qc.ca, https://www.cmhc-schl.gc.ca"
    answer = results[0]["contenu"] if results else "Aucune donnée disponible."

    # Niveau 1 : Réponse complète (factuelle)
    if niveau == 1:
        template = T.FACTUAL
    # Niveau 2 : Réponse partielle (contextualisée)
    elif niveau == 2:
        template = T.PARTIAL
    # Niveau 3 : Réponse explicative (cadre + limites)
    elif niveau == 3:
        template = T.EXPLANATORY
    # Niveau 4 : Réponse d’orientation (où chercher)
    elif niveau == 4:
        template = T.ORIENTATION
    # Niveau 5 : Réponse de transparence (ce qui manque)
    elif niveau == 5:
        template = T.TRANSPARENCY
    else:
        template = T.FACTUAL

    ia_autorisee = coverage != "none"

    return {
        "answer": template.format(answer=answer, sources=sources),
        "type": qtype,
        "niveau": niveau,
        "ia_autorisee": ia_autorisee
    }
