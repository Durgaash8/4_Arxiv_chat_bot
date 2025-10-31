from sentence_transformers import SentenceTransformer
import json 
from tqdm import tqdm
import faiss
import numpy as np
from pathlib import Path
import pickle

MODEL_NAME = "all-mpnet-base-v2"

def chunk_text(text, max_length=300):
    # naive splitter by sentences
    import re
    sents = re.split(r'(?<=[.!?]) +', text)
    chunks, cur = [], []
    cur_len = 0
    for s in sents:
        tok = len(s.split())
        if cur_len + tok > max_length:
            chunks.append(" ".join(cur))
            cur = [s]
            cur_len = tok
        else:
            cur.append(s)
            cur_len += tok
    if cur:
        chunks.append(" ".join(cur))
    return chunks

def build_index(input_json="data/quantum_subset.json", index_path="data/faiss.index", meta_path="data/meta.pkl"):
    model = SentenceTransformer(MODEL_NAME)
    with open(input_json,"r",encoding="utf8") as f:
        docs = json.load(f)
    all_embs = []
    metas = []
    for doc in tqdm(docs):
        doc_id = doc["id"]
        title = doc["title"]
        abstract = doc.get("abstract","")
        text = title + ". " + abstract
        chunks = chunk_text(text)
        for i, chunk in enumerate(chunks):
            emb = model.encode(chunk)
            all_embs.append(emb)
            metas.append({
                "doc_id": doc_id, "title": title, "chunk_idx": i, "text": chunk
            })
    X = np.vstack(all_embs).astype("float32")
    d = X.shape[1]
    index = faiss.IndexFlatIP(d)  # inner product (use normalized vectors) or IndexFlatL2
    faiss.normalize_L2(X)
    index.add(X)
    faiss.write_index(index, index_path)
    with open(meta_path, "wb") as f:
        pickle.dump(metas, f)
    print("Index and meta saved.")

if __name__ == "__main__":
    build_index()
