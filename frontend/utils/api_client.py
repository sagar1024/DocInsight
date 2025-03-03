import requests
import streamlit as st

BASE_URL = "http://127.0.0.1:8000"  # Backend's URL (hosted remotely)

def register_user(email, password, username):
    """
    Register a new user with the backend API.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json={"username": username, "email": email, "password": password},
        )
        if response.status_code == 201:
            return response.json()  # Registration successful
        return {"error": "Registration failed"}
    except requests.exceptions.RequestException as e:
        print(f"Register API Error: {e}")
        return None

def login_user(username, password):
    """
    Authenticate user with the backend API.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={"username": username, "password": password},
        )
        if response.status_code == 200:
            return response.json()  # User details
        return None
    except requests.exceptions.RequestException as e:
        print(f"Login API Error: {e}")
        return None

def authenticate_user(email, password):
    """Sends login credentials to the backend authentication API."""
    url = f"{BASE_URL}/auth/login"
    payload = {"email": email, "password": password}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error authenticating user: {e}")
        return {"error": str(e)}

def summarize_document(document, summary_length=100, focus_sections="", language="English"):
    """
    Send a document for summarization to the backend API.
    """
    try:
        files = {"file": document}
        data = {
            "summary_length": summary_length,
            "focus_sections": focus_sections,
            "language": language,
        }

        response = requests.post(f"{BASE_URL}/summarize", files=files, data=data)

        if response.status_code == 200:
            #return response.json() #Returns the summary data
            summary_data = response.json()
            #Store summary in session state
            st.session_state["document_summary"] = summary_data.get("summary", "")
            return summary_data
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Summarization API Error: {e}")
        return None

def query_chatbot(prompt, document_summary=""):
    """
    Send a prompt and document summary to the chatbot API and get the response.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/chatbot", 
            json={"prompt": prompt, "document_summary": document_summary}
        )
        if response.status_code == 200:
            return response.json().get("response", "No response received.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Chatbot API Error: {e}")
        return None

def voice_command():
    """
    Capture user voice, send to backend for STT & chatbot response, return TTS.
    """
    try:
        response = requests.post(f"{BASE_URL}/voice/command")
        if response.status_code == 200:
            return response.json()
        return {"error": "Voice command processing failed"}
    except requests.exceptions.RequestException as e:
        print(f"Voice Command API Error: {e}")
        return {"error": str(e)}

def narrate_text(text):
    """
    Send text to the backend TTS API and receive the generated audio file path.
    """
    try:
        response = requests.post(f"{BASE_URL}/voice/narrate", json={"text": text})
        if response.status_code == 200:
            return response.json().get("audio", None)
        return {"error": "TTS failed"}
    except requests.exceptions.RequestException as e:
        print(f"TTS API Error: {e}")
        return {"error": str(e)}
    
def fetch_preferences(user_id):
    """
    Fetch user preferences from the backend API.
    """
    try:
        response = requests.get(f"{BASE_URL}/preferences/{user_id}")
        if response.status_code == 200:
            return response.json()
        return None
    except requests.exceptions.RequestException as e:
        print(f"Preferences API Error: {e}")
        return None

def update_preferences(user_id, preferences):
    """
    Update user preferences in the backend API.
    """
    try:
        response = requests.put(
            f"{BASE_URL}/preferences/{user_id}",
            json=preferences,
        )
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Update Preferences API Error: {e}")
        return False
    