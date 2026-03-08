from app.retrieval.hybrid_retriever import hybrid_search

def retrieval_agent(query, plan, resources):
    """
    Executes retrieval based on the query plan.

    resources = {
        "vector": callable,
        "bm25": callable,
        "hybrid": callable
    }
    """

    mode = plan["mode"]
    top_k = plan["top_k"]

    if mode == "semantic":
        return resources["vector"](query, top_k)

    if mode == "keyword":
        return resources["bm25"](query, top_k)

    return resources["hybrid"](query, top_k)