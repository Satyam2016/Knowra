def recall_at_k(relevant, retrieved, k):
    return len(set(relevant) & set(retrieved[:k])) / len(relevant)

def mrr(retrieved, relevant):
    for i, r in enumerate(retrieved):
        if r in relevant:
            return 1 / (i + 1)
    return 0