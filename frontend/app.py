# import streamlit as st
# from components.navbar import render_navbar
# from pages import home, summarization, chatbot, voice_assistant, preferences

# # Configure Streamlit page settings
# st.set_page_config(
#     page_title="DocInsight - AI Document Summarizer",
#     page_icon="assets/logo.png",
#     layout="wide",
#     initial_sidebar_state="expanded"
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
#     # Render the navigation bar
#     # st.sidebar.image("assets/logo.png", use_column_width=True)
#     st.sidebar.title("DocInsight")
#     st.sidebar.markdown("Revolutionizing Document Analysis")

#     # Navigation
#     selection = st.sidebar.radio("Navigate to", list(PAGES.keys()))
    
#     # Render the selected page
#     page = PAGES[selection]
#     page.render()

# if __name__ == "__main__":
#     main()

import streamlit as st
from components.navbar import render_navbar
from pages import home, summarization, chatbot, voice_assistant, preferences

# Configure Streamlit page settings
st.set_page_config(
    page_title="DocInsight - AI Document Summarizer",
    #page_icon="assets/logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
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
