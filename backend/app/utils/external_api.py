import requests
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://api.gemini.com/v1/chat"

async def call_gemini_api(prompt: str) -> str:
    """
    Calls the Gemini API with a given prompt.

    Args:
        prompt (str): The user's query, optionally including document context.

    Returns:
        str: The chatbot's response.
    """
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
    payload = {"query": prompt}

    try:
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise error for non-200 responses
        data = response.json()
        return data.get("response", "No response from Gemini API")
    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"
