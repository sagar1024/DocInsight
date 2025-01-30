import requests
import os

# Load API Key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini API endpoint (replace with the correct one if needed)
GEMINI_API_URL = "https://api.gemini.com/v1/chat"

def generate_chatbot_reply(query: str) -> str:
    """
    Sends the user's query to the Gemini API and returns the chatbot's response.

    Args:
        query (str): The input query from the user.

    Returns:
        str: The chatbot's response.
    """
    if not GEMINI_API_KEY:
        return "Error: Missing Gemini API Key."

    payload = {
        "model": "gemini-pro",  # Adjust based on available models
        "messages": [{"role": "user", "content": query}],
        "temperature": 0.7,  # Adjust temperature for creativity
    }

    headers = {
        "Authorization": f"Bearer {GEMINI_API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for HTTP issues
        result = response.json()
        
        # Extract the chatbot's response
        return result.get("choices", [{}])[0].get("message", {}).get("content", "No response received.")
    
    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to Gemini API - {str(e)}"
    except KeyError:
        return "Error: Unexpected API response format."
    