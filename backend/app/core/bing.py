
# Version sans clé API : DuckDuckGo scraping (simple)
import requests
from bs4 import BeautifulSoup

def bing_web_search(question: str, count: int = 3, market: str = "fr-CA"):
    try:
        url = f"https://html.duckduckgo.com/html/?q={question}"
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        results = []
        for a in soup.select("a.result__a")[:count]:
            title = a.get_text()
            link = a.get("href")
            snippet_tag = a.find_parent("div", class_="result__body").find("a", class_="result__snippet")
            snippet = snippet_tag.get_text() if snippet_tag else ""
            results.append({
                "source": link,
                "title": title,
                "snippet": snippet
            })
        if results:
            return {"results": results}
        else:
            return {"error": "Aucun résultat trouvé."}
    except Exception as e:
        return {"error": str(e)}
