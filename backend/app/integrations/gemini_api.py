import requests
import os

from dotenv import load_dotenv

#Explicitly load .env file
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
load_dotenv(dotenv_path)

#Load API Key from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

#print(GEMINI_API_KEY)

#Correct Gemini API URL
#GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    
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
        "contents": [
            {
                "parts": [{"text": query}]
            }
        ]
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()

        print("Gemini API Raw Response:", result)  # Debugging

        # Correct parsing logic based on actual response
        if "candidates" in result and result["candidates"]:
            return result["candidates"][0].get("content", {}).get("parts", [{}])[0].get("text", "No response.")
        return "No valid response from API."

    except requests.exceptions.RequestException as e:
        return f"Error: Failed to connect to Gemini API - {str(e)}"
    except KeyError:
        return "Error: Unexpected API response format."
