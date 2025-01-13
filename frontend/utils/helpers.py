import streamlit as st

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
