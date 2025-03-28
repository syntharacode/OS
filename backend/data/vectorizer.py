# Import sentence-transformers for generating semantic embeddings
from sentence_transformers import SentenceTransformer

# Import NumPy for vector operations
import numpy as np

# Load a pre-trained embedding model for similarity or retrieval tasks
# MiniLM is efficient and provides good performance for small-scale setups
_model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate an embedding vector from a given input string
def embed_text(text: str) -> np.ndarray:
    return _model.encode(text, convert_to_numpy=True)

# Compute cosine similarity between two embedding vectors
def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    dot = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    return dot / (norm1 * norm2 + 1e-10)  # Add epsilon to avoid division by zero

# Given a query and a list of texts, return the top-k most similar entries
def most_similar(query: str, corpus: list[str], top_k: int = 5) -> list[tuple[str, float]]:
    query_vec = embed_text(query)
    scored = [(text, cosine_similarity(query_vec, embed_text(text))) for text in corpus]
    return sorted(scored, key=lambda x: x[1], reverse=True)[:top_k]
