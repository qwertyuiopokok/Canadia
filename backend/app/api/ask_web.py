from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.core.bing import bing_web_search

router = APIRouter()

@router.get("/ask_web")
def ask_web(question: str = Query(..., description="Question à poser")):
    result = bing_web_search(question)
    if "results" in result:
        # For compatibility with frontend, return only the first result
        first = result["results"][0] if result["results"] else None
        if first:
            return JSONResponse(first)
        else:
            return JSONResponse({"error": "Aucun résultat trouvé."}, status_code=404)
    else:
        return JSONResponse({"error": result.get("error", "Erreur inconnue")}, status_code=500)
