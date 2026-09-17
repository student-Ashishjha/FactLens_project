import os
from fastapi import APIRouter, UploadFile, File
from app.core.document_loader import extract_text_from_pdf

router = APIRouter()

UPLOAD_DIR = "uploaded_docs"


@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    
    extracted_text = extract_text_from_pdf(file_path)
    
    return {
        "filename": file.filename,
        "characters_extracted": len(extracted_text),
        "preview": extracted_text[:300]
    }