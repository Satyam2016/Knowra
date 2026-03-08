import faiss

def hybrid_search(query, embedder, faiss_index, bm25_store, metadata, alpha=0.6, top_k=20):
    q_vec = embedder.encode([query])
    faiss.normalize_L2(q_vec)

    v_scores, v_indices = faiss_index.search(q_vec, top_k)
    vector_results = {int(i): float(s) for i, s in zip(v_indices[0], v_scores[0])}

    bm25_indices = bm25_store.search(query, top_k)
    bm25_results = {idx: 1 / (rank + 1) for rank, idx in enumerate(bm25_indices)}

    combined = {}
    for idx in set(vector_results) | set(bm25_results):
        combined[idx] = alpha * vector_results.get(idx, 0) + (1 - alpha) * bm25_results.get(idx, 0)

    ranked = sorted(combined.items(), key=lambda x: x[1], reverse=True)

    return [{
        "text": metadata[str(idx)]["text"],
        "page": metadata[str(idx)]["page"],
        "score": score
    } for idx, score in ranked[:top_k]]