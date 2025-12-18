from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def route_query(query: str, routes: list) -> str:
    query_emb = model.encode(query)
    best_route = max(routes, key=lambda r: util.cos_sim(query_emb, model.encode(r['description'])))
    return best_route['kernel']
