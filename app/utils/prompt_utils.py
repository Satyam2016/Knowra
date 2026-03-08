def build_grounded_prompt(query, chunks):
    """
    Builds a hallucination-resistant prompt
    with explicit grounding and citations.
    """

    context = "\n\n".join(
        f"(Page {c['page']}) {c['text']}"
        for c in chunks
    )

    return f"""
You are a document-based assistant.
Answer the question using ONLY the context provided.
If the answer is not present, say you don't know.
Always cite page numbers.

Context:
{context}

Question:
{query}

Answer:
"""