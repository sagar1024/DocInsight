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

import streamlit as st
from components.navbar import render_navbar
from modules import home, summarization, chatbot, voice_assistant, preferences

# Configure Streamlit page settings
st.set_page_config(
    page_title="DocInsight - AI Document Summarizer",
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
    
    # Check if the selected page is Summarization to include image and text logic
    if selection == "Summarization":
        file = st.file_uploader("Upload a document", type=["pdf", "docx", "pptx", "txt"])
        if file:
            # Call backend API or process the file (mocked here for now)
            summary = "This is a generated summary of the document."
            image_count = 2  # Example mock value
            images = ["image1.jpg", "image2.jpg"]  # Replace with actual image byte arrays

            st.write(f"Summary generated for the document: {summary}")
            st.write(f"Number of images processed: {image_count}")

            if image_count > 0:
                st.write("Extracted Images:")
                for idx, img in enumerate(images):
                    # If `img` is a byte array, use Image.open(io.BytesIO(img))
                    st.image(img, caption=f"Image {idx + 1}", use_column_width=True)
    else:
        # Render other pages normally
        page.render()

if __name__ == "__main__":
    main()
