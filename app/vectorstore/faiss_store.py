import faiss
import json

def build_faiss_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatIP(dim)
    faiss.normalize_L2(vectors)
    index.add(vectors)
    return index

def save_faiss(index, metadata, path="data"):
    faiss.write_index(index, f"{path}/faiss.index")
    with open(f"{path}/metadata.json", "w") as f:
        json.dump(metadata, f)

def load_faiss(path="data"):
    index = faiss.read_index(f"{path}/faiss.index")
    with open(f"{path}/metadata.json") as f:
        metadata = json.load(f)
    return index, metadata