MAX_AGENT = 300

def ask(question: str):
	global rag
	if rag is None:
		rag = get_rag_engine()

	result = rag({"query": question})
	docs = result.get("source_documents", [])

	coverage = evaluate_coverage(docs)

	if coverage == "none":
		return {
			"answer": T.TRANSPARENCY,
			"ai_used": False
		}

	sources = list({d.metadata.get("source") for d in docs})

	return {
		"answer": T.FACTUAL.format(
			answer=result["result"],
			sources=", ".join(sources)
		),
		"ai_used": True
	}

from app.index.retriever import get_retriever

def get_rag_engine():
	llm = Ollama(model="tinyllama")
	retriever = get_retriever(k=3)
	return RetrievalQA.from_chain_type(
		llm=llm,
		retriever=retriever,
		return_source_documents=True
	)

import os
from typing import Dict, List
from threading import Lock

# Imports lourds désactivés pour diagnostic crash
# from langchain_community.embeddings import HuggingFaceEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain_community.llms import Ollama
# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate

# Prompt citoyen
prompt = PromptTemplate(
	input_variables=["context", "question"],
	template="""
Tu es une IA citoyenne destinée aux Canadiens et aux Québécois.

Tu aides à comprendre l’information publique, en favorisant les sources
du Québec et du Canada lorsque pertinent.

Tu restes neutre, factuelle et accessible.

Contexte :
{context}

Question :
{question}

Réponds clairement.
"""
)


qa = None
_init_lock = Lock()

def init():
	global qa
	if qa is not None:
		return

	with _init_lock:
		if qa is not None:
			return

		base_dir = os.path.abspath(
		    os.path.join(os.path.dirname(__file__), "../../..")
		)

		embeddings = HuggingFaceEmbeddings(
		    model_name="sentence-transformers/all-MiniLM-L6-v2"
		)

		# ✅ Vérifie le BON fichier FAISS
		faiss_index_path = os.path.join(base_dir, "quebec_faiss.index")
		if not os.path.exists(faiss_index_path):
		    raise RuntimeError(
		        "Index FAISS introuvable. Lance d'abord le script d'ingestion."
		    )

		db = FAISS.load_local(
		    folder_path=base_dir,
		    embeddings=embeddings,
		    index_name="quebec_faiss",
		    allow_dangerous_deserialization=True
		)

		llm = Ollama(model="tinyllama")

		qa = RetrievalQA.from_chain_type(
		    llm=llm,
		    retriever=db.as_retriever(search_kwargs={"k": 3}),
		    chain_type_kwargs={"prompt": prompt},
		    return_source_documents=True
		)

def ask(question: str) -> Dict:
	return {
		"answer": "Le système fonctionne. Question reçue : " + question,
		"sources": ["test"]
	}
from app.core.coverage import evaluate_coverage
from app.core import response_templates as T

rag = None

def ask(question: str):
	global rag
	if rag is None:
		rag = get_rag_engine()

	result = rag({"query": question})
	docs = result.get("source_documents", [])

	coverage = evaluate_coverage(docs)

	if coverage == "none":
		return {
			"answer": T.TRANSPARENCY,
			"ai_used": False
		}

	sources = list({d.metadata.get("source") for d in docs})

	return {
		"answer": T.FACTUAL.format(
			answer=result["result"],
			sources=", ".join(sources)
		),
		"ai_used": True
	}
from app.index.retriever import get_retriever

# def get_rag_engine():
#     llm = Ollama(model="tinyllama")
#     retriever = get_retriever(k=3)
#     return RetrievalQA.from_chain_type(
#         llm=llm,
#         retriever=retriever,
#         return_source_documents=True
#     )


import os
from typing import Dict, List
from threading import Lock

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Prompt citoyen désactivé pour diagnostic crash



qa = None
_init_lock = Lock()

# def init():
#     global qa
#     if qa is not None:
#         return
#
#     with _init_lock:
#         if qa is not None:
#             return
#
#         base_dir = os.path.abspath(
#             os.path.join(os.path.dirname(__file__), "../../..")
#         )
#
#         embeddings = HuggingFaceEmbeddings(
#             model_name="sentence-transformers/all-MiniLM-L6-v2"
#         )
#
#         # ✅ Vérifie le BON fichier FAISS
#         faiss_index_path = os.path.join(base_dir, "quebec_faiss.index")
#         if not os.path.exists(faiss_index_path):
#             raise RuntimeError(
#                 "Index FAISS introuvable. Lance d'abord le script d'ingestion."
#             )
#
#         db = FAISS.load_local(
#             folder_path=base_dir,
#             embeddings=embeddings,
#             index_name="quebec_faiss",
#             allow_dangerous_deserialization=True
#         )
#
#         llm = Ollama(model="tinyllama")
#
#         qa = RetrievalQA.from_chain_type(
#             llm=llm,
#             retriever=db.as_retriever(search_kwargs={"k": 3}),
#             chain_type_kwargs={"prompt": prompt},
#             return_source_documents=True
#         )

def ask(question: str) -> Dict:
	return {
		"answer": "Le système fonctionne. Question reçue : " + question,
		"sources": ["test"]
	}

