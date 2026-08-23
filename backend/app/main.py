from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.upload import router as upload_router
from app.api.chat import router as chat_router

app = FastAPI(title="RedVault AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # السماح للجميع مؤقتاً للتأكد
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(chat_router)


@app.get("/")
def root():
    return {"message": "RedVault AI API is running"}