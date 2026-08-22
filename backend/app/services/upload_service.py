from pathlib import Path
import shutil

from fastapi import HTTPException, UploadFile

from app.rag.pipeline import process_document

# Folder where uploaded files will be stored
UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {".pdf", ".docx"}


def save_uploaded_file(file: UploadFile) -> str:
    """
    Validate the uploaded file and save it to the uploads folder.
    """

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed."
        )

    file_path = UPLOAD_FOLDER / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if extension == ".pdf":
        result = process_document(file_path)

        print("\n========== RAG PIPELINE ==========")
        print(f"Chunks created: {result['chunks']}")
        print(f"Embedding shape: {result['embedding_shape']}")
        print(f"Vectors in DB: {result['documents_in_db']}")
        print("==================================\n")

    return file.filename