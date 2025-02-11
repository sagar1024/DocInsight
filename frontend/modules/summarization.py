import streamlit as st
from utils.api_client import summarize_document

def render():
    """Render the Summarization Page."""
    st.title("Document Summarization")
    st.markdown(
        """
        Upload your document to generate a concise summary.
        Supported formats: **PDF**, **Word**, **Excel**, **PowerPoint**.
        """
    )

    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "xlsx", "pptx"])

    if uploaded_file:
        st.info("File uploaded successfully!")

        # Customization options
        st.subheader("Customization Options")
        summary_length = st.slider("Select summary length", 10, 500, 100, step=10)
        focus_sections = st.text_input("Focus on specific sections (optional)", placeholder="e.g., Executive Summary, Conclusion")
        language = st.selectbox("Select summary language", ["English", "Spanish", "French", "German", "Others"])

        # Generate Summary Button
        if st.button("Generate Summary"):
            st.info("Generating summary...")

            #Call the backend API to generate the summary
            summary = summarize_document(
                document=uploaded_file,
                summary_length=summary_length,
                focus_sections=focus_sections,
                language=language
            )

            if summary and "summary" in summary:
                st.subheader("Generated Summary")
                st.write(summary["summary"])
            else:
                st.error("Failed to generate summary. Please try again.")
