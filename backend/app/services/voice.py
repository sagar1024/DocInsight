# import pyttsx3
# import speech_recognition as sr
# from io import BytesIO

# def text_to_speech(text: str):
#     """
#     Convert text to speech and return the audio file path or binary data.
#     """
#     engine = pyttsx3.init()
#     engine.save_to_file(text, "summary_audio.mp3")
#     engine.runAndWait()
#     return "summary_audio.mp3"

# def speech_to_text():
#     """
#     Convert speech to text using speech recognition.
#     """
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#     try:
#         text = recognizer.recognize_google(audio)
#         return text
#     except sr.UnknownValueError:
#         return "Sorry, I could not understand the audio."
#     except sr.RequestError:
#         return "Error processing speech request."

import pyttsx3
import speech_recognition as sr
import whisper
from io import BytesIO
from gtts import gTTS
import tempfile
import os

# Load Whisper model (can be 'tiny', 'base', 'small', 'medium', 'large')
model = whisper.load_model("base")

def text_to_speech(text: str, return_bytes=False):
    """
    Convert text to speech and return the audio file path or binary data.
    
    :param text: Input text to convert to speech.
    :param return_bytes: If True, return binary audio data instead of a file path.
    :return: File path (if return_bytes=False) or binary audio data (if return_bytes=True).
    """
    try:
        # Generate speech using gTTS
        tts = gTTS(text=text, lang="en")
        
        # Save to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_file.name)

        if return_bytes:
            with open(temp_file.name, "rb") as audio_file:
                audio_bytes = audio_file.read()
            os.remove(temp_file.name)  # Delete temp file after use
            return audio_bytes
        return temp_file.name

    except Exception as e:
        print(f"[Error] Text-to-Speech failed: {e}")
        return None

def speech_to_text(audio_path: str = None):
    """
    Convert speech to text using Whisper or SpeechRecognition.
    
    :param audio_path: If provided, uses Whisper STT for transcription.
                       If None, records from microphone using SpeechRecognition.
    :return: Transcribed text or an error message.
    """
    try:
        if audio_path:
            # Use Whisper model for accurate transcription
            result = model.transcribe(audio_path)
            return result["text"]

        else:
            # Record audio from microphone and transcribe using Google STT
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
                audio = recognizer.listen(source)

            return recognizer.recognize_google(audio)

    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Error processing speech request."
    except Exception as e:
        print(f"[Error] Speech-to-Text failed: {e}")
        return "Error in speech processing."

# if __name__ == "__main__":
#     # Quick testing (uncomment below to test)
#     # print(speech_to_text("test_audio.wav"))
#     # print(text_to_speech("Hello, this is a test!", return_bytes=False))
#     pass
