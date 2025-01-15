import streamlit as st

def render():
    """Render the Preferences Page."""
    st.title("User Preferences")
    st.markdown(
        """
        Customize your experience with DocInsight. 
        Your preferences will be saved for registered users.
        """
    )

    # Summary Preferences
    st.subheader("Summary Preferences")
    summary_length = st.slider("Default Summary Length", 10, 500, 100, step=10)
    focus_sections = st.text_input(
        "Default Focus Sections (optional)", placeholder="e.g., Executive Summary, Conclusion"
    )
    language = st.selectbox(
        "Default Language for Summaries", ["English", "Spanish", "French", "German", "Others"]
    )

    # Notification Preferences
    st.subheader("Notification Preferences")
    email_notifications = st.checkbox("Receive Email Notifications for Updates", value=True)

    # Save Preferences
    if st.button("Save Preferences"):
        st.success("Preferences saved successfully! (For registered users only).")
        st.session_state["preferences"] = {
            "summary_length": summary_length,
            "focus_sections": focus_sections,
            "language": language,
            "email_notifications": email_notifications,
        }

    # Display Saved Preferences
    st.subheader("Your Current Preferences")
    preferences = st.session_state.get("preferences", None)
    if preferences:
        st.json(preferences)
    else:
        st.warning("No preferences saved yet.")
