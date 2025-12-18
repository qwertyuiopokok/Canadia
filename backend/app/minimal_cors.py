from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.app.rag.engine import ask

from backend.app.api.feedback import router as feedback_router
from backend.app.api.chat import router as chat_router
from backend.app.api.content import router as content_router


app = FastAPI(
    title="Citoyen.QC",
    description="Plateforme citoyenne canadienne",
    version="0.1.0"
)

# CORS (simple pour le dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------- Modèles -----------

class AskRequest(BaseModel):
    question: str

# ----------- Routes -----------

@app.get("/")
def root():
    return {"message": "Citoyen.QC fonctionne"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask_endpoint(payload: AskRequest):
    return ask(payload.question)


# Route chat (si utilisée)
app.include_router(chat_router)

# Feedback 👍 / 👎
app.include_router(feedback_router)

# Content API
app.include_router(content_router)
