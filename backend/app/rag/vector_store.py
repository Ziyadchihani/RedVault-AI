import uuid
import chromadb

BASE_DIR = Path("/tmp") if os.name != "nt" else Path(".")
CHROMA_PATH = BASE_DIR / "chroma_db"

client = chromadb.PersistentClient(path=str(CHROMA_PATH))

collection = client.get_or_create_collection(
    name="documents"
)


def store_embeddings(chunks, embeddings):
    ids = [str(uuid.uuid4()) for _ in chunks]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
    )


def count_documents():
    return collection.count()