import streamlit as st

def render_navbar():
    """Render the Navbar."""
    st.sidebar.title("Navigation")
    menu = st.sidebar.radio(
        "Navigate to",
        ["Home", "Summarization", "Chatbot", "Voice Assistant", "Preferences"],
        index=0
    )

    st.sidebar.markdown("---")
    
    if "user" in st.session_state:
        # Show logged-in user details
        st.sidebar.markdown(f"**Logged in as:** {st.session_state['user']['username']}")
        if st.sidebar.button("Logout"):
            st.session_state.pop("user", None)
            st.session_state.pop("preferences", None)
            st.success("Logged out successfully!")
    else:
        st.sidebar.markdown("**Not logged in**")
        if st.sidebar.button("Login/Register"):
            st.session_state["show_auth_forms"] = True

    st.sidebar.markdown("---")
    #st.sidebar.image("assets/logo.png", use_column_width=True)

    return menu
