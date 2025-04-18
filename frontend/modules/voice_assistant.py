import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, AudioProcessorBase
import requests
import io
import av
from utils.api_client import send_text_to_speech, send_voice_command

class AudioProcessor(AudioProcessorBase):
    """Handles audio input from WebRTC streaming."""
    def __init__(self):
        self.audio_buffer = io.BytesIO()

    def recv(self, frame: av.AudioFrame):
        """Receive and store audio frame."""
        audio_data = frame.to_ndarray()
        self.audio_buffer.write(audio_data.tobytes())

    def get_audio(self):
        """Retrieve recorded audio data."""
        return self.audio_buffer.getvalue()

def render():
    """Render the Voice Assistant Page."""
    st.title("Voice Assistant")
    st.markdown("Listen to generated summaries or use voice commands to interact with DocInsight")

    #Narrating Document Summary
    st.subheader("Narrate Document Summary")
    summary = st.session_state.get("document_summary", "")

    if summary:
        st.success("Summary is available!")
        st.text_area("Generated Summary", summary, height=150, disabled=True)

        if st.button("Play Summary Audio"):
            with st.spinner("Generating narration..."):
                audio_url = send_text_to_speech(summary)
                
            if audio_url:
                st.audio(audio_url, format="audio/mp3")
            else:
                st.error("Failed to generate audio from summary.")
    else:
        st.warning("No summary available. Generate a summary in the Summary module first.")

    # Voice Command Input
    # st.subheader("Voice Commands")

    # processor = AudioProcessor()
    # webrtc_ctx = webrtc_streamer(
    #     key="speech-recorder",
    #     mode=WebRtcMode.SENDONLY,
    #     audio_processor_factory=lambda: processor,
    #     media_stream_constraints={"video": False, "audio": True},
    # )

    # if st.button("Submit Voice Command"):
    #     audio_data = processor.get_audio()
    #     if audio_data:
    #         with st.spinner("Processing voice command..."):
    #             response = send_voice_command(audio_data)

    #         if response:
    #             text_response = response.get("text_response", "No response received.")
    #             audio_response = response.get("audio")

    #             st.write(f"**Command Response:** {text_response}")
    #             if audio_response:
    #                 st.audio(audio_response, format="audio/mp3")
    #             else:
    #                 st.warning("Voice response unavailable.")
    #         else:
    #             st.error("Failed to process voice command.")
    #     else:
    #         st.error("No audio detected. Please speak and submit again.")
