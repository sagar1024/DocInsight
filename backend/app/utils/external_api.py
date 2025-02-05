import requests
import os

# Correct Gemini API URL
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print(GEMINI_API_KEY)

#GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
#GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GEMINI_API_KEY}"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

async def call_gemini_api(prompt: str) -> str:
    """
    Calls the Gemini API with a given prompt.

    Args:
        prompt (str): The user's query, optionally including document context.

    Returns:
        str: The chatbot's response.
    """
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    
    try:
        response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", json=payload, headers=headers)
        response.raise_for_status()  # Raise error for non-200 responses
        data = response.json()
        
        # Extract response text
        response_text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response from Gemini API")
        return response_text

    except Exception as e:
        return f"Error calling Gemini API: {str(e)}"
    