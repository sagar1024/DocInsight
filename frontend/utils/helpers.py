import streamlit as st
from playsound import playsound

def set_user_session(user):
    """
    Store user details in session state after login.
    """
    st.session_state["user"] = {
        "id": user["id"],
        "username": user["username"],
    }
    st.session_state["preferences"] = user.get("preferences", {})
    st.session_state["show_auth_forms"] = False

def clear_user_session():
    """
    Clear user session data (logout).
    """
    st.session_state.pop("user", None)
    st.session_state.pop("preferences", None)
    st.session_state["show_auth_forms"] = True

def read_uploaded_file(uploaded_file):
    """
    Read uploaded file and return its content.
    """
    if uploaded_file is not None:
        try:
            return uploaded_file.read()
        except Exception as e:
            print(f"Error reading uploaded file: {e}")
    return None

def format_summary(summary_data):
    """
    Format the summary data for display.
    """
    if not summary_data:
        return "No summary available."
    
    summary = summary_data.get("summary", "")
    key_points = summary_data.get("key_points", [])

    formatted = f"### Summary\n{summary}\n\n### Key Points\n"
    for idx, point in enumerate(key_points, start=1):
        formatted += f"{idx}. {point}\n"
    return formatted

def play_audio(file_path):
    """
    Play an audio file from the given file path.
    """
    try:
        playsound(file_path)
    except Exception as e:
        print(f"Error playing audio: {e}")


#NEW CODE -

import re

def validate_email(email):
    """Validates an email address format."""
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(regex, email))

def show_message(message, message_type="info"):
    """
    Displays a message on the Streamlit UI.
    message_type can be 'info', 'success', or 'error'.
    """
    if message_type == "info":
        st.info(message)
    elif message_type == "success":
        st.success(message)
    elif message_type == "error":
        st.error(message)

def process_uploaded_file(uploaded_file):
    """Processes an uploaded file and returns its content."""
    try:
        if uploaded_file is not None:
            file_bytes = uploaded_file.read()
            return file_bytes
    except Exception as e:
        st.error(f"Error processing uploaded file: {e}")
        return None
