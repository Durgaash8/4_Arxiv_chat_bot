# src/faiss_indexer.py
import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer
MODEL_NAME = "all-mpnet-base-v2"

class Retriever:
    def __init__(self, index_path="data/faiss.index", meta_path="data/meta.pkl"):
        self.index = faiss.read_index(index_path)
        with open(meta_path,"rb") as f:
            self.meta = pickle.load(f)
        self.model = SentenceTransformer(MODEL_NAME)

    def query(self, text, top_k=5):
        q_emb = self.model.encode(text).astype("float32")
        faiss.normalize_L2(q_emb.reshape(1,-1))
        D, I = self.index.search(q_emb.reshape(1,-1), top_k)
        results = []
        for score, idx in zip(D[0], I[0]):
            m = self.meta[idx]
            results.append({"score": float(score), **m})
        return results

