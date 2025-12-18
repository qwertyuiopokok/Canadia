"""
Boucle autonome d'apprentissage et d'amélioration continue.
"""

from .self_questions import generate_self_questions
from .trusted_sources import is_source_trusted
from ..core.web import search_web
from ..storage.evolution_store import upsert_gap

def run_learning_loop():
    # Placeholder: à compléter avec logique d'apprentissage
    pass

def autonomous_learning_cycle():
    questions = generate_self_questions()
    for q in questions:
        web_results = search_web(q)
        trusted_results = [
            r for r in web_results
            if is_source_trusted(r.get("url", ""))
        ]
        if not trusted_results:
            # rien de fiable → gap
            upsert_gap(
                key=f"self:{q}",
                theme="auto",
                province=None,
                region=None,
                example_question=q,
                priority=20
            )
        else:
            # on ne stocke PAS le contenu
            # on signale juste qu'une source fiable existe
            upsert_gap(
                key=f"source_found:{q}",
                theme="auto",
                province=None,
                region=None,
                example_question=q,
                priority=50
            )
