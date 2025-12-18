
from langchain_community.vectorstores import FAISS
from app.index.embeddings import get_embeddings

INDEX_PATH = "backend/app/index_data"
INDEX_NAME = "canadia_faiss"

def get_retriever(k=3):
	embeddings = get_embeddings()
	db = FAISS.load_local(
		INDEX_PATH,
		embeddings,
		index_name=INDEX_NAME,
		allow_dangerous_deserialization=True
	)
	return db.as_retriever(search_kwargs={"k": k})
