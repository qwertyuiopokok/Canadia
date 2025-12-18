"""
API source fetcher (open data, etc.)
"""
import requests

def fetch_api(endpoint: str, params: dict = None) -> list:
	response = requests.get(endpoint, params=params, timeout=10)
	response.raise_for_status()
	data = response.json()
	return data.get("results", data)
