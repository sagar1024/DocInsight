import requests
import os

from dotenv import load_dotenv

# Explicitly load .env file
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
load_dotenv(dotenv_path)

# Check if GEMINI_API_KEY is loaded
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

#print(GEMINI_API_KEY)

async def call_gemini_api(prompt: str) -> str:
    """
    Calls the Gemini API with a given prompt.

    Args: prompt (str): The user's query, optionally including document context.

    Returns: str: The chatbot's response.
    """
    
    headers = {"Content-Type": "application/json"}
    max_length = 5000  # Gemini API might have length limits
    
    #Trim the text if it's too long
    if len(prompt) > max_length:
        prompt = prompt[:max_length] + "...\n[Content trimmed]"
        
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    
    try:
        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise error for non-200 responses
        data = response.json()
        
        # Extract response text
        response_text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response from Gemini API")
        return response_text

    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"
    