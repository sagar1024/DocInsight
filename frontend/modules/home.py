import streamlit as st

def render():
    """Render the Home Page."""
    
    # st.title("Welcome to DocInsight")
    st.markdown("## Welcome to DocInsight")
    
    st.markdown("---")
    
    st.markdown("### Cut Through the Clutter – Summarize with AI!")
    st.markdown(
        """
        ```
        - Summarize lengthy documents in seconds.
        - Query documents interactively using a chatbot.
        - Use voice commands and listen to summaries.
        ```
        """
    )
    
    st.markdown("---")
    
    st.markdown("### Smart Summaries, Smarter Decisions!")
    st.markdown(
        """
        ```
        - Save time by focusing on the most critical content.
        - Make informed decisions quickly with interactive queries.
        - Enhance accessibility with voice-based interactions.
        ```
        """
    )
    
    st.markdown("---")
    
    st.markdown("### Unlock Insights, Instantly!")
    st.markdown(
        """
        ```
        - Use the sidebar to navigate to the desired functionality.
        - Upload a document for summarization or explore other features.
        ```
        """
    )

    st.info("NOTE - Use the **Summarization** page to upload a document and generate summaries.")
    st.success("Ready to dive into your documents? Let’s get started!")
    