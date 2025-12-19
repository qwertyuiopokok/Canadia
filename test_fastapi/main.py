from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Autoriser le frontend local
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/status")
def status():
    return {"status": "OK", "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

@app.get("/ask_web")
def ask_web(question: str):
    # Ici tu peux brancher ta logique Wikipedia ou autre
    return {
        "source": "Wikipedia",
        "title": question,
        "snippet": f"Résumé de {question}..."
    }
