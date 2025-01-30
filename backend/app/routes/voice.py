from fastapi import APIRouter, HTTPException
from app.services.voice import text_to_speech, process_voice_command

router = APIRouter()

@router.post("/voice/narrate")
async def narrate_text(text: str):
    """
    Endpoint to convert text to speech for summary narration.
    """
    try:
        # Generate audio from text
        audio_data = text_to_speech(text)
        return {"audio": audio_data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating narration: {str(e)}")

@router.post("/voice/command")
async def handle_voice_command(command: str):
    """
    Endpoint to process voice commands.
    """
    try:
        # Process the voice command
        response = process_voice_command(command)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing voice command: {str(e)}")
