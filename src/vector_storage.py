import faiss
import numpy as np
from langchain.embeddings import OpenAIEmbeddings  # You can replace with another embedding model

# Initialize OpenAI embedding
embedder = OpenAIEmbeddings()

class FAISSStorage:
    def __init__(self, dim=1536):
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []

    def add_documents(self, texts):
        """Adds text chunks to FAISS index."""
        vectors = np.array([embedder.embed_query(text) for text in texts]).astype("float32")
        self.index.add(vectors)
        self.documents.extend(texts)

    def search(self, query, k=5):
        """Retrieves the most relevant documents for a query."""
        query_vector = np.array([embedder.embed_query(query)]).astype("float32")
        _, indices = self.index.search(query_vector, k)
        return [self.documents[i] for i in indices[0]]

# Test
if __name__ == "__main__":
    storage = FAISSStorage()
    docs = ["This is document 1", "Relevant text about AI", "Some data about deep learning"]
    storage.add_documents(docs)
    
    results = storage.search("AI")
    print("Search Results:", results)
