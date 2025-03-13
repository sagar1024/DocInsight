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
    