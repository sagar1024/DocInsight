import requests
import streamlit as st
import json

BASE_URL = "http://127.0.0.1:8000"  # Backend's URL (hosted remotely)

def register_user(username, email, password):
    """
    Register a new user with the backend API.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json={"username": username, "email": email, "password": password},
        )
        response_data = response.json()  #Parse JSON response
        print("Register API Response:", response_data)  #Debugging
        if response.status_code == 200 or response.status_code == 201:
            return {"success": True, "message": response_data.get("message", "Registration successful!")}
        return {"success": False, "error": response_data.get("detail", "Registration failed.")}

    except requests.exceptions.RequestException as e:
        print(f"Register API Error: {e}")
        return {"success": False, "error": str(e)}

def authenticate_user(email, password):
    """
    Sends login credentials to the backend authentication API.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={"email": email, "password": password}
        )

        response_data = response.json()  #Parse the JSON response
        print("Login API Response:", response_data)  #Debugging

        if response.status_code == 200 and "access_token" in response_data:
            return {
                "success": True,
                "token": response_data["access_token"],
                "user": response_data.get("user", {}),
            }
        
        return {"success": False, "error": "Invalid credentials. Please try again."}

    except requests.RequestException as e:
        print(f"Error authenticating user: {e}")
        return {"success": False, "error": str(e)}

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

def send_voice_command(audio_bytes):
    """Send recorded voice data to the backend for STT processing."""
    try:
        response = requests.post(
            f"{BASE_URL}/voice/command",
            files={"audio": ("audio.wav", audio_bytes, "audio/wav")}
        )
        return response.json() if response.status_code == 200 else None
    except requests.exceptions.RequestException as e:
        print(f"Voice Command API Error: {e}")
        return None

def send_text_to_speech(text):
    """Send text to the backend for TTS processing."""
    try:
        response = requests.post(f"{BASE_URL}/voice/narrate", json={"text": text})
        return response.json().get("audio") if response.status_code == 200 else None
    except requests.exceptions.RequestException as e:
        print(f"TTS API Error: {e}")
        return None
    
# def fetch_preferences(user_id):
#     """
#     Fetch user preferences from the backend API.
#     """
#     try:
#         response = requests.get(f"{BASE_URL}/preferences/{user_id}")
#         if response.status_code == 200:
#             return response.json()
#         return None
#     except requests.exceptions.RequestException as e:
#         print(f"Preferences API Error: {e}")
#         return None

# def update_preferences(user_id, preferences):
#     """
#     Update user preferences in the backend API.
#     """
#     try:
#         response = requests.put(
#             f"{BASE_URL}/preferences/{user_id}",
#             json=preferences,
#         )
#         return response.status_code == 200
#     except requests.exceptions.RequestException as e:
#         print(f"Update Preferences API Error: {e}")
#         return False

def fetch_preferences(user_id):
    """
    Fetch user preferences from the backend API.
    Always returns a dictionary.
    """
    try:
        response = requests.get(f"{BASE_URL}/preferences/{user_id}")
        if response.status_code == 200:
            prefs = response.json()
            if isinstance(prefs, str):
                try:
                    prefs = json.loads(prefs)
                except json.JSONDecodeError:
                    prefs = {}
            return prefs
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
    