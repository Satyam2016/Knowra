from rank_bm25 import BM25Okapi

class BM25Store:
    def __init__(self, chunks):
        self.texts = [c["text"] for c in chunks]
        self.tokenized = [t.lower().split() for t in self.texts]
        self.bm25 = BM25Okapi(self.tokenized)

    def search(self, query, top_k=10):
        tokens = query.lower().split()
        scores = self.bm25.get_scores(tokens)
        ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
        return ranked[:top_k]