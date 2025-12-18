"""
FAISS index creation and update utilities
"""
import os
from langchain_community.vectorstores import FAISS
from app.index.embeddings import get_embeddings
from app.storage.content_store import all_contents

INDEX_PATH = "backend/app/index_data"
INDEX_NAME = "canadia_faiss"

def build_or_update_index():
	contents = all_contents()
	if not contents:
		print("Aucun contenu à indexer.")
		return
	texts = [c["content"] for c in contents]
	metadatas = [{"source": c["source"]["id"], "title": c["title"], "url": c["url"]} for c in contents]
	embeddings = get_embeddings()
	db = FAISS.from_texts(texts, embeddings, metadatas=metadatas)
	db.save_local(INDEX_PATH, index_name=INDEX_NAME)
	print(f"Index FAISS sauvegardé dans {INDEX_PATH} ({INDEX_NAME})")
