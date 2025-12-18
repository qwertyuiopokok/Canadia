"""
Deduplication utilities
"""
import hashlib

def normalize_text(text: str) -> str:
	return " ".join(text.lower().strip().split())

def compute_fingerprint(title: str, url: str, source_id: str) -> str:
	base = f"{normalize_text(title)}|{url}|{source_id}"
	return hashlib.sha256(base.encode("utf-8")).hexdigest()
