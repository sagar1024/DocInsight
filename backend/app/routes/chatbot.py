from fastapi import APIRouter, HTTPException
from app.services.chatbot import get_chatbot_response

router = APIRouter()

@router.post("/chat")
async def chat_with_bot(query: str):
    """
    Endpoint to interact with the chatbot.
    """
    try:
        # Get the chatbot's response to the query
        response = get_chatbot_response(query)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chatbot query: {str(e)}")

