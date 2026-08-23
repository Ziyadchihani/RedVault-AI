from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router

app = FastAPI(title="RedVault AI")

# Naming allowed origins clearly for local development and production
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://redvault-ai.vercel.app", 
]

# Allow React frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {"message": "RedVault AI API is running"}