
from typing import Any, Dict, Optional

# from langchain_community.llms import Ollama
from app.pro.prompts.universal_pro_prompt import UNIVERSAL_PRO_PROMPT
# llm = Ollama(model="mistral")

def ask_pro(question: str, company_context: Optional[Dict[str, Any]] = None, context: Optional[Dict[str, Any]] = None):
    ctx = company_context or context or {}
    prompt = UNIVERSAL_PRO_PROMPT.format(
        sector=ctx.get("sector", ""),
        job=ctx.get("job", ""),
        capabilities=", ".join(ctx.get("capabilities", []) or []),
        focus=", ".join(ctx.get("focus", []) or []),
        context=ctx,
        question=question
    )
    # answer = llm(prompt)
    answer = "[Ollama désactivé pour test minimal]"
    return {
        "answer": answer,
        "disclaimer": (
            "Canadia Pro fournit une aide à la structuration "
            "et à l’optimisation opérationnelle. "
            "Aucun conseil financier, légal ou technique certifié."
        )
    }
