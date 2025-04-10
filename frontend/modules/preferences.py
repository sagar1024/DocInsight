# import streamlit as st

# def render():
#     """Render the Preferences Page."""
#     st.title("User Preferences")
#     st.markdown(
#         """
#         Customize your experience with DocInsight. 
#         Your preferences will be saved for registered users.
#         """
#     )

#     # Summary Preferences
#     st.subheader("Summary Preferences")
#     summary_length = st.slider("Default Summary Length", 10, 500, 100, step=10)
#     focus_sections = st.text_input(
#         "Default Focus Sections (optional)", placeholder="e.g., Executive Summary, Conclusion"
#     )
#     language = st.selectbox(
#         "Default Language for Summaries", ["English", "Spanish", "French", "German", "Others"]
#     )

#     # Notification Preferences
#     st.subheader("Notification Preferences")
#     email_notifications = st.checkbox("Receive Email Notifications for Updates", value=True)

#     # Save Preferences
#     if st.button("Save Preferences"):
#         st.success("Preferences saved successfully! (For registered users only).")
#         st.session_state["preferences"] = {
#             "summary_length": summary_length,
#             "focus_sections": focus_sections,
#             "language": language,
#             "email_notifications": email_notifications,
#         }

#     # Display Saved Preferences
#     st.subheader("Your Current Preferences")
#     preferences = st.session_state.get("preferences", None)
    
#     if preferences:
#         st.json(preferences)
#     else:
#         st.warning("No preferences saved yet.")

import streamlit as st
import json
from utils.api_client import fetch_preferences, update_preferences

def render():
    st.title("User Preferences")
    st.markdown("""
        Customize your experience with DocInsight.
        Your preferences will be saved for registered users.
    """)

    user = st.session_state.get("user", {})
    user_id = user.get("id")

    if not user_id:
        st.warning("Please log in to access and save preferences.")
        return

    # Fetch preferences if not already in session
    if "preferences" not in st.session_state:
        prefs = fetch_preferences(user_id)

        # Ensure prefs is a dictionary
        if isinstance(prefs, str):
            try:
                prefs = json.loads(prefs)
            except json.JSONDecodeError:
                prefs = {}
        st.session_state["preferences"] = prefs or {}

    current_prefs = st.session_state["preferences"]

    st.subheader("Summary Preferences")

    summary_length = st.slider(
        "Default Summary Length", 10, 500, 
        current_prefs.get("summary_length", 100), step=10
    )
    focus_sections = st.text_input(
        "Default Focus Sections (optional)", 
        value=current_prefs.get("focus_sections", "")
    )
    language = st.selectbox(
        "Default Language for Summaries",
        ["English", "Spanish", "French", "German", "Others"],
        index=["English", "Spanish", "French", "German", "Others"].index(
            current_prefs.get("language", "English")
        )
    )

    st.subheader("Notification Preferences")
    email_notifications = st.checkbox(
        "Receive Email Notifications for Updates", 
        value=current_prefs.get("email_notifications", True)
    )

    if st.button("Save Preferences"):
        preferences = {
            "summary_length": summary_length,
            "focus_sections": focus_sections,
            "language": language,
            "email_notifications": email_notifications,
        }

        success = update_preferences(user_id, preferences)
        if success:
            st.session_state["preferences"] = preferences
            st.success("Preferences saved successfully!")
        else:
            st.error("Failed to save preferences.")

    # st.subheader("Your Current Preferences")
    # st.json(st.session_state.get("preferences", {}))
    
    # st.subheader("Your Current Preferences")
    st.markdown("# Your Current Preferences")
    prefs = st.session_state.get("preferences", {})
    if prefs:
        st.markdown("#### Summary Preferences -")
        st.write(f"**Summary Length:** {prefs.get('summary_length', '-')}")
        st.write(f"**Focus Sections:** {prefs.get('focus_sections', '-')}")
        st.write(f"**Language:** {prefs.get('language', '-')}")

        st.markdown("#### Notification Preferences -")
        st.write(f"**Email Notifications:** {'Enabled' if prefs.get('email_notifications', False) else 'Disabled'}")
    else:
        st.warning("No preferences saved yet.")
