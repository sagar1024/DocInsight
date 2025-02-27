from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.summarization import process_document

router = APIRouter(prefix="/summarize")

@router.post("/")
async def summarize(
    file: UploadFile = File(...),
    summary_length: int = Form(100),
    focus_sections: str = Form(""),
    language: str = Form("English")
):
    """
    Endpoint to summarize and analyze an uploaded document.
    Extracts text and images, performs OCR, and generates a summary.
    """
    try:
        # Process the uploaded file
        result = await process_document(
            file.file, summary_length, focus_sections, language
        )
        return {
            "summary": result["summary"],
            "image_count": result["images"],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error summarizing document: {str(e)}")
