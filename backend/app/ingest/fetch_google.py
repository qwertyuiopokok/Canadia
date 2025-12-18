"""
Google Custom Search API fetcher for web results.
Requires API key and Custom Search Engine (CSE) ID.
"""
import os
import requests
from typing import List, Dict

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "YOUR_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID", "YOUR_CSE_ID")

SEARCH_URL = "https://www.googleapis.com/customsearch/v1"

def fetch_google_search(query: str, num_results: int = 5) -> List[Dict]:
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": query,
        "num": num_results
    }
    resp = requests.get(SEARCH_URL, params=params)
    resp.raise_for_status()
    data = resp.json()
    results = []
    for item in data.get("items", []):
        results.append({
            "title": item.get("title"),
            "link": item.get("link"),
            "summary": item.get("snippet"),
            "source": "google_search"
        })
    return results

if __name__ == "__main__":
    for r in fetch_google_search("gouvernement logement Québec"):
        print(r)
