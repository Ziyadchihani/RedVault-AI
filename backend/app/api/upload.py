from fastapi import APIRouter, UploadFile, File
from app.services.upload_service import save_uploaded_file

router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    filename = save_uploaded_file(file)

    return {
        "status": "success",
        "filename": filename
    }