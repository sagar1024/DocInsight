# from app.utils.voice_utils import text_to_speech_conversion, interpret_voice_command

# def text_to_speech(text: str) -> bytes:
#     """
#     Convert text to speech using a voice API.
    
#     Args:
#         text (str): The text to convert.
    
#     Returns:
#         bytes: The audio file content.
#     """
#     try:
#         audio_data = text_to_speech_conversion(text)
#         return audio_data
#     except Exception as e:
#         raise ValueError(f"Failed to convert text to speech: {str(e)}")

# def process_voice_command(command: str) -> str:
#     """
#     Process voice commands and return the appropriate response.
#     Args:
#         command (str): The voice command to process.
#     Returns:
#         str: The interpreted command response.
#     """
#     try:
#         response = interpret_voice_command(command)
#         return response
#     except Exception as e:
#         raise ValueError(f"Failed to process voice command: {str(e)}")

import pyttsx3
import speech_recognition as sr
from io import BytesIO

def text_to_speech(text: str):
    """
    Convert text to speech and return the audio file path or binary data.
    """
    engine = pyttsx3.init()
    engine.save_to_file(text, "summary_audio.mp3")
    engine.runAndWait()
    return "summary_audio.mp3"

def speech_to_text():
    """
    Convert speech to text using speech recognition.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Error processing speech request."
    