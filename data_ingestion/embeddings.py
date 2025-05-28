from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

model = SentenceTransformer("all-MiniLM-L6-v2")
INDEX_FILE = "vector_store.index"
DOCS_FILE = "documents.pkl"

def embed_texts(texts):
    return model.encode(texts)

def save_vector_index(texts):
    vectors = embed_texts(texts)
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(np.array(vectors))
    with open(DOCS_FILE, "wb") as f:
        pickle.dump(texts, f)
    faiss.write_index(index, INDEX_FILE)

def load_vector_index():
    index = faiss.read_index(INDEX_FILE)
    with open(DOCS_FILE, "rb") as f:
        docs = pickle.load(f)
    return index, docs