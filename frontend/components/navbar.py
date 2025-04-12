import streamlit as st

def render_navbar():
    """Render the Navbar with project name, feedback button, and navigation menu."""

    #Project Name
    st.sidebar.markdown("## 📄 DocInsight")
    st.sidebar.markdown("*AI-powered document summarization and analysis tool.*")

    st.sidebar.markdown("---")

    #Navigation Menu
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio(
        "Navigate to",
        ["Home", "Summarization", "Chatbot", "Voice Assistant", "Preferences"],
        index=0
    )

    st.sidebar.markdown("---")

    #User Authentication Info
    if "user" in st.session_state:
        st.sidebar.markdown(f"**Logged in as:** {st.session_state['user']['username']}")
        if st.sidebar.button("Logout"):
            st.session_state.pop("user", None)
            st.session_state.pop("preferences", None)
            st.success("Logged out successfully!")
    else:
        st.sidebar.markdown("**Not logged in**")
        if st.sidebar.button("Login/Register"):
            st.session_state["show_auth_forms"] = True
    
    # Feedback Button
    # if st.sidebar.button("Give Feedback"):
    #     st.sidebar.markdown("### We value your feedback!")
    #     feedback = st.sidebar.text_area("Tell us your thoughts:")
    #     if st.sidebar.button("Submit Feedback"):
    #         if feedback:
    #             st.success("Thank you for your feedback!")
    #             #Yet to integrate a backend API to store feedback
    #         else:
    #             st.warning("Please enter some feedback before submitting.")

    return menu
