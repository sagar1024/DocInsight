from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.summarization import process_document

router = APIRouter(prefix="/summarize")

@router.post("/")
async def summarize(file: UploadFile = File(...)):
    """
    Endpoint to summarize and analyze an uploaded document.
    Extracts text and images, performs OCR, and generates a summary.
    """
    try:
        # Process the uploaded file
        result = await process_document(file.file)  # Use the file stream directly
        return {
            "summary": result["summary"],
            "image_count": result["images"],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error summarizing document: {str(e)}")
