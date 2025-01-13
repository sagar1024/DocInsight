import streamlit as st

def render():
    """Render the Home Page."""
    st.title("Welcome to DocInsight")
    st.image("assets/logo.png", use_column_width=True)
    
    st.markdown(
        """
        ## Revolutionizing Document Analysis
        DocInsight is an AI-powered tool that helps you:
        - Summarize lengthy documents in seconds.
        - Query documents interactively using a chatbot.
        - Use voice commands and listen to summaries.
        
        ### Why Choose DocInsight?
        - Save time by focusing on the most critical content.
        - Make informed decisions quickly with interactive queries.
        - Enhance accessibility with voice-based interactions.

        ### Get Started
        - Use the sidebar to navigate to the desired functionality.
        - Upload a document for summarization or explore other features.
        """
    )

    st.info("Use the **Summarization** page to upload a document and generate summaries.")
    st.success("Ready to dive into your documents? Let’s get started!")
