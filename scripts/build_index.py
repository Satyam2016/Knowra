import os
from app.ingestion.ingest import extract_pages
from app.ingestion.chunking import chunk_text
from app.ingestion.embeddings import embed_texts
from app.vectorstore.faiss_store import build_faiss_index, save_faiss
from app.vectorstore.bm25_store import BM25Store

PDF_DIR = "data/pdfs"

all_chunks = []
for file in os.listdir(PDF_DIR):
    if file.endswith(".pdf"):
        pages = extract_pages(os.path.join(PDF_DIR, file))
        chunks = chunk_text(pages)
        all_chunks.extend(chunks)

texts = [c["text"] for c in all_chunks]
vectors = embed_texts(texts)

index = build_faiss_index(vectors)

metadata = {
    str(i): {"text": c["text"], "page": c["page"]}
    for i, c in enumerate(all_chunks)
}

save_faiss(index, metadata)
BM25Store(all_chunks)

print("Index built successfully")