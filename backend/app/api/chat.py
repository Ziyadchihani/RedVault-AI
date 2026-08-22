from fastapi import APIRouter
from pydantic import BaseModel

from app.rag.retriever import retrieve_documents
from app.llm.gemini_service import ask_gemini

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):
    # Retrieve relevant chunks
    documents = retrieve_documents(request.question)

    # Ask Gemini
    answer = ask_gemini(request.question, documents)

    return {
        "question": request.question,
        "answer": answer,
        "sources": documents
    }