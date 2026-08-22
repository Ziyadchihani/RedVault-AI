from app.services.document_service import extract_text_from_pdf
from app.rag.chunking import split_text
from app.rag.embeddings import create_embeddings
from app.rag.vector_store import store_embeddings, count_documents


def process_document(file_path):
    # 1. Extract text
    text = extract_text_from_pdf(file_path)

    # 2. Split into chunks
    chunks = split_text(text)

    # 3. Generate embeddings
    embeddings = create_embeddings(chunks)

    # 4. Store in ChromaDB
    store_embeddings(chunks, embeddings)

    return {
        "chunks": len(chunks),
        "embedding_shape": embeddings.shape,
        "documents_in_db": count_documents()
    }