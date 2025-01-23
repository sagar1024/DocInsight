import streamlit as st
from utils.api_client import summarize_document, voice_command
from utils.helpers import play_audio

def render():
    """Render the Voice Assistant Page."""
    st.title("Voice Assistant")
    st.markdown(
        """
        Use voice commands to interact with DocInsight or listen to generated summaries.
        """
    )

    # Upload file for TTS summary
    st.subheader("Listen to Document Summary")
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "xlsx", "pptx"])

    if uploaded_file:
        st.info("File uploaded successfully!")
        if st.button("Generate and Play Summary"):
            # Call backend to generate summary
            summary = summarize_document(file=uploaded_file)

            if summary:
                # Convert summary to speech
                audio_path = play_audio(summary)
                st.audio(audio_path, format="audio/mp3")
            else:
                st.error("Failed to generate summary for TTS. Please try again.")

    # Voice Command Input
    st.subheader("Voice Commands")
    if st.button("Activate Voice Command"):
        st.info("Listening for voice input...")
        command_result = voice_command()

        if command_result:
            st.write(f"**Command Result**: {command_result}")
        else:
            st.error("Failed to process voice command. Try again.")
            