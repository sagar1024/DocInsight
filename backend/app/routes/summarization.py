# from fastapi import APIRouter, UploadFile, File, HTTPException, Form, Query
# from typing import Optional
# from tempfile import NamedTemporaryFile

# from ..services import summarization

# router = APIRouter(prefix="/summarize", tags=["Summarization"])

# @router.post("/")
# async def summarize_document(
#     file: UploadFile = File(...), 
#     summary_length: Optional[str] = Query("medium", enum=["short", "medium", "long"]),
#     language: Optional[str] = Query("en", description="Language of the summary")
# ):
#     """
#     Endpoint to summarize an uploaded document.
#     """
#     length_mapping = {
#         "short": (50, 100),
#         "medium": (100, 200),
#         "long": (200, 300),
#     }
#     min_length, max_length = length_mapping[summary_length]

#     try:
#         # Save the uploaded file temporarily
#         with NamedTemporaryFile(delete=False) as temp_file:
#             temp_file.write(await file.read())
#             temp_file_path = temp_file.name
        
#         # Extract text from file
#         text = summarization.extract_text_from_file(temp_file_path)
        
#         # Summarize the extracted text
#         summary = summarization.summarize_text(text, max_length=max_length, min_length=min_length, language=language)
#         return {"summary": summary}
    
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.summarization import summarize_document

router = APIRouter()

@router.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    """
    Endpoint to summarize an uploaded document.
    """
    try:
        # Read the uploaded file
        content = await file.read()
        # Call the summarization service
        summary = summarize_document(content, file.filename)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error summarizing document: {str(e)}")
