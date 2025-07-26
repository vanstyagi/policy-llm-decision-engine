from pathlib import Path
import json
from sentence_transformers import SentenceTransformer, util

chunks_dir = Path(__file__).resolve().parent.parent / "outputs" / "chunks"
model = SentenceTransformer("all-MiniLM-L6-v2")  # 50 MB, downloads once

def embed_chunks():
    """Return {filename: embedding} for every chunk."""
    embeddings = {}
    for txt_file in sorted(chunks_dir.glob("*.txt")):
        text = txt_file.read_text(encoding="utf-8")
        embeddings[txt_file.name] = model.encode(text, convert_to_tensor=True)
    return embeddings

def top_chunks(query, chunk_embs, k=3):
    query_emb = model.encode(query, convert_to_tensor=True)
    scores = []
    for fname, emb in chunk_embs.items():
        score = float(util.cos_sim(query_emb, emb)[0][0])
        scores.append((score, fname))
    scores.sort(reverse=True)
    return scores[:k]

if __name__ == "__main__":
    chunk_embs = embed_chunks()
    query = "knee surgery waiting period"
    best = top_chunks(query, chunk_embs)
    print(json.dumps(best, indent=2))