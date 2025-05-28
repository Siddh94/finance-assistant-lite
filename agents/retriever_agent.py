from data_ingestion.embeddings import model, load_vector_index
import numpy as np

def retrieve_top_k(query: str, k: int = 3):
    try:
        index, docs = load_vector_index()
        query_vec = model.encode([query])
        D, I = index.search(np.array(query_vec), k)

        if len(I) == 0 or len(I[0]) == 0:
            return ["No relevant documents found."]

        results = []
        for i in I[0]:
            if i < len(docs):
                results.append(docs[i])
        return results

    except Exception as e:
        return [f"Retriever error: {str(e)}"]
