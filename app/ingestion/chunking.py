def chunk_text(pages, chunk_size=500, overlap=100):
    chunks = []

    for page in pages:
        paragraphs = page["text"].split("\n\n")
        buffer = ""

        for para in paragraphs:
            if len(buffer) + len(para) <= chunk_size:
                buffer += " " + para
            else:
                chunks.append({
                    "text": buffer.strip(),
                    "page": page["page"]
                })
                buffer = buffer[-overlap:] + " " + para

        if buffer.strip():
            chunks.append({
                "text": buffer.strip(),
                "page": page["page"]
            })

    return chunks