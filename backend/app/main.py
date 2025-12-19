import os
import logging
def check_faiss_llm():
    try:
        from backend.app.rag import engine
        base_dir = os.path.dirname(os.path.abspath(engine.__file__))
        faiss_index_path = os.path.join(base_dir, "quebec_faiss.index")
        if not os.path.exists(faiss_index_path):
            logging.warning(f"[Canadia] Index FAISS absent: {faiss_index_path}")
        from langchain_community.llms import Ollama
        _ = Ollama(model="tinyllama")
    except Exception as e:
        logging.warning(f"[Canadia] Problème LLM/FAISS: {e}")

check_faiss_llm()
# --- Load environment variables from .env ---
from dotenv import load_dotenv
load_dotenv()

# --- Database initialization ---
from .storage.database import init_db
from fastapi import FastAPI, Response
app = FastAPI()

# --- Middleware CORS ---
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure DB tables exist at startup
@app.on_event("startup")
def startup_event():
    init_db()
# --- Daily job scheduler for gap analysis ---
from app.scheduler.daily_jobs import run_daily_jobs
import threading
import time
from app.pipeline import run_ingestion
from app.storage.content_store import all_contents
from datetime import datetime

# Ajout de l'endpoint après la création de l'objet app
@app.post("/admin/ingest")
def ingest_now():
    """
    Lance manuellement le pipeline d’actualités.
    À protéger plus tard (clé admin).
    """
    results = run_ingestion()
    return {
        "status": "ok",
        "items_processed": len(results)
    }

@app.get("/suggestions")
def suggestions():
    # Récupère les contenus du jour (ou les plus récents)
    contents = all_contents()
    # Tri par date décroissante, puis sélection des 10 plus récents
    items = sorted(
        [c for c in contents if c.get("status") == "new" or c.get("status") == "updated"],
        key=lambda x: x.get("last_updated", ""),
        reverse=True
    )[:10]
    # Format minimal pour l’UI
    return [
        {
            "title": c["title"],
            "link": c.get("url", "#")
        } for c in items
    ]
# --- Import du routeur ask pour suggestions ---
from app.api.ask import router as ask_router
from app.api.content import router as content_router
from app.api.alerts import router as alerts_router
from app.api.pro import router as pro_router
from app.api.student import router as student_router
# --- Modèles avancés pour filtrage, pagination, tri ---
from typing import Any, List, Optional
from enum import Enum
from pydantic import BaseModel, Field


class Operator(str, Enum):
    eq = "eq"
    ne = "ne"
    lt = "lt"
    lte = "lte"
    gt = "gt"
    gte = "gte"
    contains = "contains"
    in_ = "in"


class FilterCondition(BaseModel):
    field: str = Field(..., example="status")
    operator: Operator = Field(..., example="eq")
    value: Any = Field(..., example="active")


class Pagination(BaseModel):
    page: int = Field(1, ge=1)
    page_size: int = Field(20, ge=1, le=100)


class SortOrder(str, Enum):
    asc = "asc"
    desc = "desc"


class Sort(BaseModel):
    field: str
    order: SortOrder = SortOrder.asc


class FilterPayload(BaseModel):
    filters: List[FilterCondition]
    pagination: Optional[Pagination] = None
    sort: Optional[List[Sort]] = None


from fastapi import FastAPI, Request
import requests
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel, Field
from typing import List, Literal, Optional, Union
from uuid import UUID


# Sous-modèles imbriqués
class Source(BaseModel):
    nom: str
    url: str
    type: Literal["gouvernement", "media", "organisme", "citoyen"]


# Nouveau modèle Province
class Province(BaseModel):
    code: str
    nom: str

# Nouveau modèle Region
class Region(BaseModel):
    code: str
    nom: str
    province: str

class Geographie(BaseModel):
    niveau: Literal["canada", "province", "region"]
    provinces: Optional[List[Province]] = None
    regions: Optional[List[Region]] = None

class Document(BaseModel):
    id: Union[UUID, str]
    titre: str
    resume: Optional[str] = None
    contenu: str
    source: Source
    date_publication: str
    themes: List[str]
    geographie: Geographie
    statut: Literal["actif", "archive"]









import threading
from app.pipeline import run_ingestion

def start_scheduler_background(interval_minutes=30):
    def scheduler_loop():
        while True:
            run_ingestion()
            time.sleep(interval_minutes * 60)
    thread = threading.Thread(target=scheduler_loop, daemon=True)
    thread.start()


# Démarre le scheduler d'ingestion en tâche de fond au lancement de l'API
start_scheduler_background(interval_minutes=30)

# Jinja2 templates setup
templates = Jinja2Templates(directory="backend/app/templates")





# Inclusion des routeurs
app.include_router(ask_router)
app.include_router(content_router)
app.include_router(alerts_router)
app.include_router(pro_router)
app.include_router(student_router, prefix="/student")
from app.api.feedback import router as feedback_router
app.include_router(feedback_router)

# --- Ajout du routeur ask_web ---
from app.api.ask_web import router as ask_web_router
app.include_router(ask_web_router)


# --- Ajout du routeur status ---
from app.api.status import router as status_router
app.include_router(status_router)

from app.api.ask_anything import router as ask_anything_router
app.include_router(ask_anything_router)

from app.api.ask_anything_pro import router as ask_anything_pro_router
app.include_router(ask_anything_pro_router)

from app.api.ask_rag import router as ask_rag_router
app.include_router(ask_rag_router)


@app.post("/document")
def create_document(doc: Document):
    return doc


@app.post("/document-to-signal")
@app.post("/document-to-signal-and-save")




# Page d'accueil avec moteur de recherche
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route to render charte.html
@app.get("/charte", response_class=HTMLResponse)
def charte(request: Request):
    return templates.TemplateResponse("charte.html", {"request": request})

# Route to render all signals as HTML
@app.get("/signals/html", response_class=HTMLResponse)
def signals_html(request: Request):
    return templates.TemplateResponse("signals.html", {"request": request, "signals": []})

# Example: success template usage
@app.get("/success", response_class=HTMLResponse)
def success_example(request: Request):
    return templates.TemplateResponse("success.html", {"request": request, "message": "Opération réussie !", "data": {"foo": "bar"}})

# Example: error template usage
@app.get("/error", response_class=HTMLResponse)
def error_example(request: Request):
    return templates.TemplateResponse("error.html", {"request": request, "message": "Une erreur est survenue.", "details": "Détail technique ici."})

