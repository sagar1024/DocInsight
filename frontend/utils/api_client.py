import requests

BASE_URL = "http://127.0.0.1:8000"  # Backend's URL (hosted remotely)

def register_user(email, password, username):
    """
    Register a new user with the backend API.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json={"username": username, "email": email, "password": password},
        )
        if response.status_code == 201:
            return response.json()  # Registration successful
        return {"error": "Registration failed"}
    except requests.exceptions.RequestException as e:
        print(f"Register API Error: {e}")
        return None

def login_user(username, password):
    """
    Authenticate user with the backend API.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={"username": username, "password": password},
        )
        if response.status_code == 200:
            return response.json()  # User details
        return None
    except requests.exceptions.RequestException as e:
        print(f"Login API Error: {e}")
        return None

def authenticate_user(email, password):
    """Sends login credentials to the backend authentication API."""
    url = f"{BASE_URL}/auth/login"
    payload = {"email": email, "password": password}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error authenticating user: {e}")
        return {"error": str(e)}
    
def summarize_document(document, summary_length=0.5, focus_sections="", language="English"):
    """
    Send a document for summarization to the backend API.
    """
    try:
        # Prepare the data
        files = {"file": document}  # 'file' is the key for the uploaded file
        data = {
            "summary_length": summary_length,
            "focus_sections": focus_sections,
            "language": language,
        }

        # Make the API request to the backend
        response = requests.post(f"{BASE_URL}/summarize", files=files, data=data)
        
        if response.status_code == 200:
            return response.json()  # Returns the summary data (e.g., {"summary": "generated summary"})
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Summarization API Error: {e}")
        return None

def query_chatbot(prompt):
    """
    Send a prompt to the chatbot API and get the response.
    """
    try:
        response = requests.post(f"{BASE_URL}/chatbot", json={"prompt": prompt})
        if response.status_code == 200:
            return response.json().get("response", "No response received.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Chatbot API Error: {e}")
        return None

def voice_command(command):
    """
    Send a voice command to the backend API and get the response.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/voice/command",
            json={"command": command},
        )
        if response.status_code == 200:
            return response.json()  # Backend response
        return None
    except requests.exceptions.RequestException as e:
        print(f"Voice Command API Error: {e}")
        return None
    
def fetch_preferences(user_id):
    """
    Fetch user preferences from the backend API.
    """
    try:
        response = requests.get(f"{BASE_URL}/preferences/{user_id}")
        if response.status_code == 200:
            return response.json()
        return None
    except requests.exceptions.RequestException as e:
        print(f"Preferences API Error: {e}")
        return None

def update_preferences(user_id, preferences):
    """
    Update user preferences in the backend API.
    """
    try:
        response = requests.put(
            f"{BASE_URL}/preferences/{user_id}",
            json=preferences,
        )
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"Update Preferences API Error: {e}")
        return False
    