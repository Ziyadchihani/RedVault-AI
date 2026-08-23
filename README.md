# RedVault AI

RedVault AI is a Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions about their content.

Instead of sending the entire document directly to an AI model, RedVault AI first processes the document, divides it into smaller chunks, converts those chunks into numerical embeddings, and stores them in a vector database. When the user asks a question, the system retrieves the most relevant chunks and sends them together with the question to Gemini, which generates a natural-language answer based on the retrieved information.

## Project Architecture

The project consists of two main parts:

- Frontend: React + Vite
- Backend: Python + FastAPI

The backend contains the complete RAG pipeline:

PDF → Text Extraction → Chunking → Embeddings → ChromaDB → Retrieval → Gemini → Answer

## How It Works

### 1. PDF Upload

The user selects a PDF from the React interface.

The frontend sends the PDF to the FastAPI backend through:

`POST /upload`

### 2. Text Extraction

The backend extracts the text from the uploaded PDF.

### 3. Chunking

The extracted text is divided into smaller chunks.

This makes the document easier to search and allows the system to retrieve only the relevant information.

### 4. Embeddings

Each text chunk is converted into a numerical vector using a sentence-transformer embedding model.

In our project, each embedding contains 384 dimensions.

### 5. ChromaDB

The chunks and their embeddings are stored in ChromaDB.

ChromaDB is used as the vector database for semantic search.

### 6. Question Retrieval

When the user asks a question, the question is converted into an embedding.

The system searches ChromaDB and retrieves the most relevant document chunks.

### 7. Gemini

The retrieved chunks and the user's question are sent to Gemini.

Gemini generates a natural-language answer using the retrieved document information.

### 8. Response

The answer is returned through FastAPI and displayed in the React frontend.

## Technologies Used

### Frontend

- React
- Vite
- Axios
- JavaScript
- CSS / Tailwind CSS

### Backend

- Python
- FastAPI
- Uvicorn

### RAG

- Sentence Transformers
- Embeddings
- ChromaDB
- Semantic Search

### LLM

- Google Gemini API

### Document Processing

- PDF text extraction
- Text chunking

## Project Structure

```text
RAG/
│
├── backend/
│   │
│   ├── app/
│   │   ├── api/
│   │   │   ├── chat.py
│   │   │   └── upload.py
│   │   │
│   │   ├── llm/
│   │   │   └── gemini_service.py
│   │   │
│   │   ├── rag/
│   │   │   ├── chunking.py
│   │   │   ├── embeddings.py
│   │   │   ├── pipeline.py
│   │   │   ├── retriever.py
│   │   │   └── vector_store.py
│   │   │
│   │   ├── services/
│   │   │   ├── document_service.py
│   │   │   └── upload_service.py
│   │   │
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── .gitignore
├── README.md
