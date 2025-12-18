"""
Génération de réponse à partir du contexte fusionné, via LLM (Ollama).
"""
from langchain_community.llms import Ollama

llm = Ollama(model="tinyllama")

def generate(question: str, contents: list) -> str:
    """
    Génère une réponse à partir de la question et du contexte fourni.
    Args:
        question (str): La question utilisateur.
        contents (list): Liste de dicts avec 'text' et 'source'.
    Returns:
        str: Réponse générée par le LLM.
    """
    context = "\n".join(
        f"- {c['text']} (source: {c['source']})"
        for c in contents
    )

    prompt = f"""
Tu es Canadia, une IA citoyenne canadienne.

Réponds UNIQUEMENT avec les informations ci-dessous.
Si l'information est incomplète, dis-le clairement.

Informations :
{context}

Question :
{question}

Réponse :
"""

    return llm(prompt)
