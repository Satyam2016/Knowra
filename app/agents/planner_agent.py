def plan_query(query):
    q = query.lower()

    if any(k in q for k in ["define", "what is", "explain"]):
        return {"mode": "semantic", "top_k": 5}

    if any(k in q for k in ["exact", "term", "section", "page"]):
        return {"mode": "keyword", "top_k": 10}

    return {"mode": "hybrid", "top_k": 8}