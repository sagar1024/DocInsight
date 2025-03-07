import streamlit as st
from utils.api_client import voice_command, narrate_text

def render():
    """Render the Voice Assistant Page."""
    st.title("Voice Assistant")
    st.markdown(
        """
        Use voice commands to interact with DocInsight or listen to generated summaries.
        """
    )
    
    #Narrate Document Summary (if available)
    st.subheader("Narrate Document Summary")

    if "document_summary" in st.session_state and st.session_state["document_summary"]:
        st.success("Summary is available!")
        st.text_area("Generated Summary", st.session_state["document_summary"], height=150, disabled=True)

        if st.button("Play Summary Audio"):
            with st.spinner("Generating narration..."):
                audio_path = narrate_text(st.session_state["document_summary"])
            
            if audio_path:
                st.audio(audio_path, format="audio/mp3")
            else:
                st.error("Failed to generate audio from summary.")
    else:
        st.warning("No summary available. Generate a summary in the Summary module first.")

    #Voice Command Input (No File Upload Required)
    st.subheader("Voice Commands")
    if st.button("Activate Voice Command"):
        st.info("Listening for voice input...")
        with st.spinner("Processing voice command..."):
            response = voice_command()
        
        if response:
            text_response = response.get("text_response", "No response received.")
            audio_response = response.get("audio", None)

            st.write(f"**Command Response**: {text_response}")
            if audio_response:
                st.audio(audio_response, format="audio/mp3")
            else:
                st.warning("Voice response unavailable.")
        else:
            st.error("Failed to process voice command.")
            