import streamlit as st
from components.header import render_header
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

# Light/Dark mode state
if "dark_mode" not in st.session_state:
    st.session_state["dark_mode"] = False

# Apply Light/Dark mode styling
if st.session_state["dark_mode"]:
    st.markdown(
        """
        <style>
            body { background-color: #121212; color: white; }
            .stApp { background-color: #121212; color: white; }
            .navbar-container { background-color: #333 !important; color: white !important; }
        </style>
        """,
        unsafe_allow_html=True
    )

# Render the header at the top
render_header()

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
                st.experimental_rerun()  #Force rerun to update the page
            else:
                show_message("Authentication failed. Please check your credentials.", "error")
    # elif auth_option == "Sign Up":
    #     user_data = render_signup_form()
    #     if user_data:
    #         response = register_user(user_data["username"], user_data["email"], user_data["password"])
    #         #print("Register API Response:", response) #Debugging
    #         if "success" in response:
    #             st.success("Registration successful! Please log in.")
    #         else:
    #             show_message("Registration failed. Please try again.", "error")
    elif auth_option == "Sign Up":
        user_data = render_signup_form()
        if user_data:
            response = register_user(user_data["username"], user_data["email"], user_data["password"])
            if response.get("success"):
                st.success(response.get("message", "Registration successful! Please log in."))
            else:
                show_message(response.get("error", "Registration failed. Please try again."), "error")

#Styling for the whole app -
def load_custom_css():
    """Inject custom CSS for dark reddish theme."""
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)   

def main():
    # Load CSS at the start
    load_custom_css()
    
    # User authentication
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        render_auth_page()
        return

    # Render the navigation bar
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
    