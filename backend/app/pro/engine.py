from langchain_community.llms import Ollama
from app.pro.prompts.universal_pro_prompt import UNIVERSAL_PRO_PROMPT

llm = Ollama(model="mistral")

def ask_pro(question: str, context: dict):
    prompt = UNIVERSAL_PRO_PROMPT.format(
        sector=context["sector"],
        job=context["job"],
        capabilities=", ".join(context["capabilities"]),
        focus=", ".join(context["focus"]),
        context=context,
        question=question
    )
    answer = llm(prompt)
    return {
        "answer": answer,
        "disclaimer": (
            "Canadia Pro fournit une aide à la structuration "
            "et à l’optimisation opérationnelle. "
            "Aucun conseil financier, légal ou technique certifié."
        )
    }
