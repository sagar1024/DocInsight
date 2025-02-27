# from fastapi import APIRouter, HTTPException
# from pydantic import BaseModel
# from app.services.chatbot import get_chatbot_response

# router = APIRouter()

# class ChatRequest(BaseModel):
#     prompt: str

# @router.post("/chatbot")
# async def chat_with_bot(request: ChatRequest):
#     try:
#         response = get_chatbot_response(request.prompt)
#         return {"response": response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error processing chatbot query: {str(e)}")

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.chatbot import get_chatbot_response

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str
    document_summary: str = ""

@router.post("/chatbot")
async def chat_with_bot(request: ChatRequest):
    try:
        response = get_chatbot_response(request.prompt, request.document_summary)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chatbot query: {str(e)}")
