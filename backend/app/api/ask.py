from fastapi import APIRouter
from app.api.rss_scraper import fetch_rss_articles

router = APIRouter()

@router.get("/suggestions")
def get_suggestions():
    """Retourne une liste de suggestions d’actualités du jour (titres)."""
    articles = fetch_rss_articles()
    # On retourne uniquement les titres et liens pour l’autocomplétion
    return [{"title": a["title"], "link": a["link"]} for a in articles if a.get("title") and a.get("link")]
from typing import Any, Dict
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.core.ask import ask as core_ask

# Initialisation des templates (doit être partagé avec main.py)
templates = Jinja2Templates(directory="backend/app/templates")

def analyse_question(question: str) -> dict:
    q = question.lower()

    themes = []
    if any(w in q for w in ["logement", "loyer", "habitation"]):
        themes.append("logement")

    geo = "canada"
    if "québec" in q or "qc" in q:
        geo = "QC"
    if "montréal" in q:
        geo = "MTL"

    return {
        "themes": themes,
        "geo": geo,
        "raw": question
    }

def search_content(contents: list, analysis: dict) -> list:
    results = []
    for c in contents:
        if any(t in c.get("themes", []) for t in analysis["themes"]):
            results.append(c)

    return results

def recherche_contenu(analysis: dict) -> dict:
    # Exemple de contenus enrichis
    contents = [
        {"id": 1, "themes": ["logement"], "geo": "QC", "text": "Aide au logement au Québec (programme provincial)."},
        {"id": 2, "themes": ["santé"], "geo": "CANADA", "text": "Assurance maladie au Canada (programme fédéral)."},
        {"id": 3, "themes": ["logement"], "geo": "CANADA", "text": "Programmes fédéraux de logement (CMHC)."},
        {"id": 4, "themes": ["logement"], "geo": "QC", "text": "Allocation-logement pour familles à faible revenu au Québec."}
    ]
    results = search_content(contents, analysis)
    return {"resultats": [r["text"] for r in results]}

def evaluate_coverage(results: list) -> str:
    if not results:
        return "none"

    if len(results) == 1:
        return "partial"

    if len(results) >= 2:
        return "full"

    return "unknown"

def evaluer_couverture(contenu: dict) -> dict:
    coverage = evaluate_coverage(contenu["resultats"])
    return {"couverture": coverage, "nb_resultats": len(contenu["resultats"])}

def generer_reponse(question: str, contenu: dict, evaluation: dict, analyse: dict) -> str:
    sources = "https://www.rdl.gouv.qc.ca, https://www.cmhc-schl.gc.ca"
    answer = contenu["resultats"][0] if contenu["resultats"] else "Aucune donnée disponible."
    couverture = evaluation.get("couverture")
    if couverture == "none":
        return TRANSPARENCY
    elif couverture == "partial":
        return PARTIAL.format(answer=answer)
    elif couverture == "full":
        return FACTUAL.format(answer=answer, sources=sources)
    else:
        return ORIENTATION.format(sources=sources)

# Endpoint principal
from fastapi import APIRouter
router = APIRouter()

@router.get("/ask", response_class=HTMLResponse)
def ask_endpoint(request: Request, question: str, niveau: int = 1):
    result = core_ask(question, niveau)
    return templates.TemplateResponse(
        "success.html",
        {"request": request, "message": result["answer"], "data": result, "niveau": niveau}
    )
