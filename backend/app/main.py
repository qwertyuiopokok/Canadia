from fastapi import Body


# --- IMPORTS ---
from fastapi import FastAPI, Request, Response, status, Body
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, constr as pyd_constr, Field
from typing import Any, List, Optional, Union, Literal
from enum import Enum
from uuid import UUID
import threading
import time
import requests

import logging
import psutil
import yagmail

# --- SURVEILLANCE MEMOIRE EN TACHE DE FOND ---
MEMORY_ALERT_THRESHOLD = 80.0  # pourcentage
MEMORY_CHECK_INTERVAL = 10  # secondes

# --- CONFIG EMAIL ---
MEMORY_ALERT_EMAIL = "fourniermorinetienne@gmail.com"  # Adresse d'alerte
YAGMAIL_USER = "fourniermorinetienne@gmail.com"        # Identifiant d'envoi
YAGMAIL_PASS = "VOTRE_MOT_DE_PASSE"             # À personnaliser

def memory_monitor_loop():
    process = psutil.Process()
    while True:
        mem_percent = process.memory_percent()
        if mem_percent > MEMORY_ALERT_THRESHOLD:
            logging.warning(f"ALERTE MEMOIRE: Utilisation mémoire élevée: {mem_percent:.2f}%")
            try:
                yag = yagmail.SMTP(YAGMAIL_USER, YAGMAIL_PASS)
                yag.send(
                    to=MEMORY_ALERT_EMAIL,
                    subject="Alerte mémoire Canadia",
                    contents=f"Utilisation mémoire élevée détectée: {mem_percent:.2f}% sur le backend."
                )
            except Exception as e:
                logging.error(f"Erreur lors de l'envoi de l'alerte email: {e}")
        time.sleep(MEMORY_CHECK_INTERVAL)

# Lancer la surveillance mémoire en tâche de fond au démarrage
threading.Thread(target=memory_monitor_loop, daemon=True).start()

# Pour la surveillance mémoire

# --- APP & MIDDLEWARE ---
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://localhost", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    response: Response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
    response.headers["Referrer-Policy"] = "same-origin"
    response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none';"
    return response

# --- MODELES ---
class AskReq(BaseModel):
    question: pyd_constr(strip_whitespace=True, min_length=1, max_length=500)

# (Autres modèles Pydantic ici, voir plus bas)

# --- ROUTES PRINCIPALES ---
@app.post("/ask", status_code=status.HTTP_200_OK)
def ask(req: AskReq):
    return {"message": f"Question reçue: {req.question}"}

@app.post("/citizen/ask", status_code=status.HTTP_200_OK)
def citizen_ask(req: AskReq = Body(...)):
    return ask(req)

# --- ROUTES HTML ---
templates = Jinja2Templates(directory="backend/app/templates")
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
@app.get("/charte", response_class=HTMLResponse)
def charte(request: Request):
    return templates.TemplateResponse("charte.html", {"request": request})
@app.get("/signals/html", response_class=HTMLResponse)
def signals_html(request: Request):
    return templates.TemplateResponse("signals.html", {"request": request, "signals": []})
@app.get("/success", response_class=HTMLResponse)
def success_example(request: Request):
    return templates.TemplateResponse("success.html", {"request": request, "message": "Opération réussie !", "data": {"foo": "bar"}})
@app.get("/error", response_class=HTMLResponse)
def error_example(request: Request):
    return templates.TemplateResponse("error.html", {"request": request, "message": "Une erreur est survenue.", "details": "Détail technique ici."})

# --- INCLUSION DES ROUTEURS ---
from backend.app.api.ask import router as ask_router
from backend.app.api.content import router as content_router
from backend.app.api.alerts import router as alerts_router
from backend.app.api.pro import router as pro_router
from backend.app.api.student import router as student_router
from backend.app.api.feedback import router as feedback_router
from backend.app.api.ask_web import router as ask_web_router
from backend.app.api.status import router as status_router
from backend.app.api.ask_anything import router as ask_anything_router
from backend.app.api.ask_anything_pro import router as ask_anything_pro_router

# --- ROUTE DE SURVEILLANCE MEMOIRE ---
@app.get("/monitor/memory", response_class=JSONResponse)
def monitor_memory():
    process = psutil.Process()
    mem_info = process.memory_info()
    return {
        "rss": mem_info.rss,  # Resident Set Size
        "vms": mem_info.vms,  # Virtual Memory Size
        "percent": process.memory_percent(),
    }


app.include_router(ask_router)
app.include_router(content_router)
app.include_router(alerts_router)
app.include_router(pro_router)
app.include_router(student_router, prefix="/student")
app.include_router(feedback_router)
app.include_router(ask_web_router)
app.include_router(status_router)
app.include_router(ask_anything_router)
app.include_router(ask_anything_pro_router)
# app.include_router(ask_rag_router)

# --- AUTRES MODELES (à placer dans un fichier models.py idéalement) ---
# (Province, Region, Geographie, Document, etc.)


# SCHEDULER désactivé pour stabilité (threading et scheduler_loop retirés)

# Jinja2 templates setup
templates = Jinja2Templates(directory="backend/app/templates")

# --- Import du routeur ask pour suggestions ---
from backend.app.api.ask import router as ask_router
from backend.app.api.content import router as content_router
from backend.app.api.alerts import router as alerts_router
from backend.app.api.pro import router as pro_router
from backend.app.api.student import router as student_router

app.include_router(ask_router)
app.include_router(content_router)
app.include_router(alerts_router)
app.include_router(pro_router)
app.include_router(student_router, prefix="/student")
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
from backend.app.pipeline import run_ingestion

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
from backend.app.api.feedback import router as feedback_router
app.include_router(feedback_router)

# --- Ajout du routeur ask_web ---
from backend.app.api.ask_web import router as ask_web_router
app.include_router(ask_web_router)


# --- Ajout du routeur status ---
from backend.app.api.status import router as status_router
app.include_router(status_router)

from backend.app.api.ask_anything import router as ask_anything_router
app.include_router(ask_anything_router)

from backend.app.api.ask_anything_pro import router as ask_anything_pro_router
app.include_router(ask_anything_pro_router)

from backend.app.api.ask_rag import router as ask_rag_router
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

