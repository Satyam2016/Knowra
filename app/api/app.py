from fastapi import FastAPI
from app.vectorstore.faiss_store import load_faiss
from app.vectorstore.bm25_store import BM25Store
from app.ingestion.embeddings import embedder
from app.retrieval.hybrid_retriever import hybrid_search
from app.retrieval.reranker import rerank
from app.agents.planner_agent import plan_query
from app.agents.answer_agent import build_prompt

app = FastAPI()

faiss_index, metadata = load_faiss()
bm25_store = BM25Store(list(metadata.values()))

@app.post("/chat")
def chat(query: str):
    plan = plan_query(query)

    chunks = hybrid_search(
        query,
        embedder,
        faiss_index,
        bm25_store,
        metadata,
        top_k=20
    )

    final_chunks = rerank(query, chunks)
    prompt = build_prompt(query, final_chunks)

    return {
        "prompt": prompt,
        "sources": final_chunks
    }