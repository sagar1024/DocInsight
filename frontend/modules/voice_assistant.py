# import streamlit as st
# from utils.api_client import voice_command, narrate_text

# def render():
#     """Render the Voice Assistant Page."""
#     st.title("Voice Assistant")
#     st.markdown(
#         """
#         Use voice commands to interact with DocInsight or listen to generated summaries.
#         """
#     )
    
#     #Narrate Document Summary (if available)
#     st.subheader("Narrate Document Summary")

#     if "document_summary" in st.session_state and st.session_state["document_summary"]:
#         st.success("Summary is available!")
#         st.text_area("Generated Summary", st.session_state["document_summary"], height=150, disabled=True)

#         if st.button("Play Summary Audio"):
#             with st.spinner("Generating narration..."):
#                 audio_path = narrate_text(st.session_state["document_summary"])
            
#             if audio_path:
#                 st.audio(audio_path, format="audio/mp3")
#             else:
#                 st.error("Failed to generate audio from summary.")
#     else:
#         st.warning("No summary available. Generate a summary in the Summary module first.")

#     #Voice Command Input (No File Upload Required)
#     st.subheader("Voice Commands")
#     if st.button("Activate Voice Command"):
#         st.info("Listening for voice input...")
#         with st.spinner("Processing voice command..."):
#             response = voice_command()
        
#         if response:
#             text_response = response.get("text_response", "No response received.")
#             audio_response = response.get("audio", None)

#             st.write(f"**Command Response**: {text_response}")
#             if audio_response:
#                 st.audio(audio_response, format="audio/mp3")
#             else:
#                 st.warning("Voice response unavailable.")
#         else:
#             st.error("Failed to process voice command.")

#ALTERNATE CODE -

import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, AudioProcessorBase
import requests
import io
import av
from ..utils.api_client import send_text_to_speech, send_voice_command

class AudioProcessor(AudioProcessorBase):
    def __init__(self):
        self.audio_buffer = io.BytesIO()

    def recv(self, frame: av.AudioFrame):
        """Receive audio frame and store it in buffer."""
        audio_data = frame.to_ndarray()
        self.audio_buffer.write(audio_data.tobytes())

    def get_audio(self):
        """Retrieve recorded audio."""
        return self.audio_buffer.getvalue()

def render():
    """Render the Voice Assistant Page."""
    st.title("Voice Assistant")
    st.markdown("Use voice commands to interact with DocInsight or listen to generated summaries.")

    # Narrate Document Summary (if available)
    st.subheader("Narrate Document Summary")

    if "document_summary" in st.session_state and st.session_state["document_summary"]:
        st.success("Summary is available!")
        st.text_area("Generated Summary", st.session_state["document_summary"], height=150, disabled=True)

        if st.button("Play Summary Audio"):
            with st.spinner("Generating narration..."):
                audio_url = send_text_to_speech(st.session_state["document_summary"])
            
            if audio_url:
                st.audio(audio_url, format="audio/mp3")
            else:
                st.error("Failed to generate audio from summary.")
    else:
        st.warning("No summary available. Generate a summary in the Summary module first.")

    # Voice Command Input
    st.subheader("Voice Commands")
    
    processor = AudioProcessor()
    webrtc_ctx = webrtc_streamer(
        key="speech-recorder",
        mode=WebRtcMode.SENDONLY,
        audio_processor_factory=lambda: processor,
        media_stream_constraints={"video": False, "audio": True},
    )

    if st.button("Submit Voice Command"):
        if processor.get_audio():
            with st.spinner("Processing voice command..."):
                response = send_voice_command(processor.get_audio())

            if response and "text_response" in response:
                st.write(f"**Command Response:** {response.get('text_response', 'No response received.')}")
                audio_response = response.get("audio", None)
                if audio_response:
                    st.audio(audio_response, format="audio/mp3")
                else:
                    st.warning("Voice response unavailable.")
            else:
                st.error("Failed to process voice command.")
        else:
            st.error("No audio detected. Please speak and submit again.")
