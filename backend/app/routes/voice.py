import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import speech_recognition as sr
from gtts import gTTS

router = APIRouter()

# Directory to save generated audio files
AUDIO_SAVE_PATH = "generated_audio"
os.makedirs(AUDIO_SAVE_PATH, exist_ok=True)

BASE_URL = "http://localhost:8000"  # Update if deployed

@router.post("/voice/command")
async def process_voice_command(audio: UploadFile = File(...)):
    """
    Process a voice command from an uploaded audio file using Speech-to-Text (STT).
    """
    recognizer = sr.Recognizer()
    
    try:
        # Generate a unique filename for the uploaded audio
        audio_filename = f"{uuid.uuid4()}.wav"
        audio_path = os.path.join(AUDIO_SAVE_PATH, audio_filename)

        # Save the uploaded audio file
        with open(audio_path, "wb") as buffer:
            buffer.write(audio.file.read())

        # Load audio for recognition
        with sr.AudioFile(audio_path) as source:
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.record(source)

        # Perform Speech-to-Text using Google Web Speech API
        text_command = recognizer.recognize_google(audio_data)

        # Cleanup: Remove the temporary audio file
        os.remove(audio_path)

        return {"transcribed_text": text_command}

    except sr.UnknownValueError:
        raise HTTPException(status_code=400, detail="Could not understand the audio.")
    except sr.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Speech recognition service error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in voice processing: {str(e)}")

class TTSRequest(BaseModel):
    text: str

# @router.post("/voice/narrate")
# async def narrate_text(request: TTSRequest):
#     """
#     Convert text into speech using Text-to-Speech (TTS) and return the generated audio URL.
#     """
#     try:
#         # Generate a unique filename for the output speech
#         audio_filename = f"{uuid.uuid4()}.mp3"
#         audio_filepath = os.path.join(AUDIO_SAVE_PATH, audio_filename)

#         # Convert text to speech
#         tts = gTTS(text=request.text, lang="en")
#         tts.save(audio_filepath)

#         # Return a URL instead of a local file path
#         return {"audio": f"{BASE_URL}/generated_audio/{audio_filename}"}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error in TTS processing: {str(e)}")

@router.post("/voice/narrate")
async def narrate_text(request: TTSRequest):
    """
    Convert text into speech using Text-to-Speech (TTS) and return the generated audio URL.
    """
    try:
        # Generate a unique filename for the output speech
        audio_filename = f"{uuid.uuid4()}.mp3"
        audio_filepath = os.path.join(AUDIO_SAVE_PATH, audio_filename)

        # Convert text to speech
        tts = gTTS(text=request.text, lang="en")
        tts.save(audio_filepath)

        # Return the direct download URL
        return {"audio": f"{BASE_URL}/generated_audio/{audio_filename}"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error in TTS processing: {str(e)}")
