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
    
#     # Check if the selected page is Summarization to include image and text logic
#     if selection == "Summarization":
#         file = st.file_uploader("Upload a document", type=["pdf", "docx", "pptx", "txt"])
#         if file:
#             # Call backend API or process the file (mocked here for now)
#             summary = "This is a generated summary of the document."
#             image_count = 2  # Example mock value
#             images = ["image1.jpg", "image2.jpg"]  # Replace with actual image byte arrays

#             st.write(f"Summary generated for the document: {summary}")
#             st.write(f"Number of images processed: {image_count}")

#             if image_count > 0:
#                 st.write("Extracted Images:")
#                 for idx, img in enumerate(images):
#                     # If `img` is a byte array, use Image.open(io.BytesIO(img))
#                     st.image(img, caption=f"Image {idx + 1}", use_column_width=True)
#     else:
#         # Render other pages normally
#         page.render()

# if __name__ == "__main__":
#     main()

#ALTERNATE -

# import streamlit as st
# from components.navbar import render_navbar
# from components.footer import render_footer
# from modules import home, summarization, chatbot, voice_assistant, preferences

# st.set_page_config(
#     page_title="DocInsight - AI Document Summarizer",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

# # Available pages
# PAGES = {
#     "Home": home,
#     "Summarization": summarization,
#     "Chatbot": chatbot,
#     "Voice Assistant": voice_assistant,
#     "Preferences": preferences,
# }

# def main():
#     # Render navigation bar
#     selection = render_navbar()

#     # Render selected page
#     page = PAGES[selection]
#     page.render()

#     # Render footer
#     render_footer()

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
    if "authenticated" not in st.session_state or not st.session_state["authenticated"]:
        render_auth_page()
        return

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
    
    