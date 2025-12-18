"""
Web page fetcher (controlled scraping)
"""
import requests
from bs4 import BeautifulSoup

def fetch_web_page(url: str) -> dict:
	html = requests.get(url, timeout=10).text
	soup = BeautifulSoup(html, "html.parser")
	return {
		"title": soup.title.string if soup.title else "",
		"content": " ".join(p.get_text() for p in soup.find_all("p")),
		"url": url
	}
