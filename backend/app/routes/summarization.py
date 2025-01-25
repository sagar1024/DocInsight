# from fastapi import APIRouter, UploadFile, File, HTTPException
# from app.services.summarization import summarize_document

# router = APIRouter()

# @router.post("/summarize")
# async def summarize(file: UploadFile = File(...)):
#     """
#     Endpoint to summarize an uploaded document.
#     """
#     try:
#         # Read the uploaded file
#         content = await file.read()
#         # Call the summarization service
#         summary = summarize_document(content, file.filename)
#         return {"summary": summary}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error summarizing document: {str(e)}")

from fastapi import APIRouter, File, UploadFile
from app.services.summarization import process_document

router = APIRouter()

@router.post("/analyze/")
async def analyze_document(file: UploadFile = File(...)):
    result = await process_document(file.file)
    return {
        "summary": result["summary"],
        "image_count": result["images"],
    }
