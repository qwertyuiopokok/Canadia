"""
Recherche web contrôlée via DuckDuckGo API.
"""
import requests

def search_web(query: str) -> list:
    """
    Effectue une recherche web via DuckDuckGo et retourne les 3 premiers résultats.
    Args:
        query (str): Requête de recherche.
    Returns:
        list: Résultats formatés (content, source, confidence).
    """
    response = requests.get(
        "https://api.duckduckgo.com/",
        params={"q": query, "format": "json"},
        timeout=10
    )

    data = response.json()
    results = []

    for item in data.get("RelatedTopics", [])[:3]:
        if "Text" in item:
            results.append({
                "content": item["Text"],
                "source": "Web public",
                "confidence": "medium"
            })

    return results
