from app.rag.embeddings import model
from app.rag.vector_store import collection


def retrieve_documents(query: str, n_results: int = 5):
    """
    Retrieve the most relevant document chunks from ChromaDB.
    """

    # Convert the question into an embedding
    query_embedding = model.encode([query])

    # Search the vector database
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=n_results
    )

    return results["documents"][0]