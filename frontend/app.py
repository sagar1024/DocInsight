import streamlit as st
from components.navbar import render_navbar
from modules import home, summarization, chatbot, voice_assistant, preferences

# Configure Streamlit page settings
st.set_page_config(
    page_title="DocInsight - AI Document Summarizer",
    #page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": None,
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

def main():
    st.sidebar.title("DocInsight")
    st.sidebar.markdown("Revolutionizing Document Analysis")
    
    # Render the navigation bar and get the selected menu
    selection = render_navbar()

    # Render the selected page
    page = PAGES[selection]
    page.render()

if __name__ == "__main__":
    main()
