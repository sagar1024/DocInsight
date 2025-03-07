import streamlit as st
import re
from playsound import playsound

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

def validate_email(email):
    """Validates an email address format."""
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return bool(re.match(regex, email))

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
