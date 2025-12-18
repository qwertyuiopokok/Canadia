import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

SYSTEM_PROMPT = """
Tu es Canadia, un assistant expert en compréhension, structuration et aide à la décision.
Tu réponds TOUJOURS en JSON strict avec ces clés exactes :
{
  "title": "Titre court et impactant",
  "summary": "Résumé clair en 3-5 phrases",
  "key_points": ["point 1", "point 2", ...],
  "analysis": "Analyse approfondie et nuancée",
  "actions_or_reflections": ["action ou question de réflexion 1", ...],
  "sources": ["source 1", ...] ou [],
  "limits": "Limites de l'analyse",
  "disclaimer": "Note si nécessaire"
}

Adapte le ton :
- citizen : simple, concret, quotidien
- student : pédagogique, analogies
- pro : professionnel, stratégique

Tu prends en compte l'historique de conversation.
"""

@app.post("/{mode}/ask")
async def ask(mode: str, body: dict):
    messages = body.get("messages", [])
    context = body.get("context", "general")

    mode_instructions = {
        "citizen": "Langage simple et concret",
        "student": "Pédagogique avec analogies",
        "pro": "Professionnel et orienté résultats"
    }

    system_msg = {
        "role": "system",
        "content": SYSTEM_PROMPT + f"\nMode: {mode_instructions.get(mode, 'general')}. Contexte: {context}"
    }

    full_messages = [system_msg] + messages

    try:
        response = client.chat.completions.create(
            model="grok-4",
            messages=full_messages,
            temperature=0.7,
            response_format={"type": "json_object"}
        )
        content = response.choices[0].message.content
        return json.loads(content)
    except Exception as e:
        return {
            "analysis": "Erreur de format JSON ou d'appel API",
            "error": str(e),
            "raw": locals().get("content", "")
        }
