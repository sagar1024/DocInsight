# import streamlit as st
# from components.navbar import render_navbar
# from modules import home, summarization, chatbot, voice_assistant, preferences

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="DocInsight - AI Document Summarizer",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         "Get Help": None,
#         "Report a bug": None,
#         "About": None,
#     }
# )

# # Define available pages
# PAGES = {
#     "Home": home,
#     "Summarization": summarization,
#     "Chatbot": chatbot,
#     "Voice Assistant": voice_assistant,
#     "Preferences": preferences,
# }

# def main():
#     st.sidebar.title("DocInsight")
#     st.sidebar.markdown("Revolutionizing Document Analysis")
    
#     # Render the navigation bar and get the selected menu
#     selection = render_navbar()

#     # Render the selected page
#     page = PAGES[selection]
#     page.render()

# if __name__ == "__main__":
#     main()

#ALTERNATE -

import streamlit as st
from components.navbar import render_navbar
from components.footer import render_footer
from components.auth_forms import render_login_form, render_signup_form
from utils.api_client import authenticate_user, register_user
from modules import home, summarization, chatbot, voice_assistant, preferences
from utils.helpers import show_message

# Configure Streamlit page settings
st.set_page_config(
    page_title="DocInsight - AI Document Summarizer",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": "DocInsight: Revolutionizing Document Analysis",
    }
)

# Define available pages
PAGES = {
    "Home": home,
    "Summarization": summarization,
    "Chatbot": chatbot,
    "Voice Assistant": voice_assistant,
    "Preferences": preferences,
}

def render_auth_page():
    """Renders the authentication page for login or signup."""
    st.title("Welcome to DocInsight!")
    auth_option = st.radio("Choose an option:", ["Login", "Sign Up"])

    if auth_option == "Login":
        user_data = render_login_form()
        if user_data:
            response = authenticate_user(user_data["email"], user_data["password"])
            if "token" in response:
                st.session_state["authenticated"] = True
                st.session_state["user"] = response
                st.success(f"Welcome back, {response.get('name', 'User')}!")
            else:
                show_message("Authentication failed. Please check your credentials.", "error")
    elif auth_option == "Sign Up":
        user_data = render_signup_form()
        if user_data:
            response = register_user(user_data["email"], user_data["password"], user_data["name"])
            if "success" in response:
                st.success("Registration successful! Please log in.")
            else:
                show_message("Registration failed. Please try again.", "error")

def main():
    # Check if the user is authenticated
    # if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
    #     render_auth_page()
    #     return

    # Render the navigation bar and get the selected menu
    selection = render_navbar()

    # Render the selected page
    if selection in PAGES:
        page = PAGES[selection]
        page.render()
    else:
        st.error("Page not found.")

    # Render the footer
    render_footer()

if __name__ == "__main__":
    main()
    
    