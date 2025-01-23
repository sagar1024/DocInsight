from app.utils.voice_utils import text_to_speech_conversion, interpret_voice_command

def text_to_speech(text: str) -> bytes:
    """
    Convert text to speech using a voice API.
    
    Args:
        text (str): The text to convert.
    
    Returns:
        bytes: The audio file content.
    """
    try:
        audio_data = text_to_speech_conversion(text)
        return audio_data
    except Exception as e:
        raise ValueError(f"Failed to convert text to speech: {str(e)}")

def process_voice_command(command: str) -> str:
    """
    Process voice commands and return the appropriate response.
    
    Args:
        command (str): The voice command to process.
    
    Returns:
        str: The interpreted command response.
    """
    try:
        response = interpret_voice_command(command)
        return response
    except Exception as e:
        raise ValueError(f"Failed to process voice command: {str(e)}")
    