import requests

BASE_URL = "http://localhost:8000/api"  # Replace with your backend's URL if hosted remotely.

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

def register_user(username, password):
    """
    Register a new user with the backend API.
    """
    try:
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json={"username": username, "password": password},
        )
        if response.status_code == 201:
            return response.json()  # Registration successful
        return None
    except requests.exceptions.RequestException as e:
        print(f"Register API Error: {e}")
        return None

def fetch_summarization(document, summary_length=0.5):
    """
    Send a document for summarization.
    """
    try:
        files = {"file": document}
        data = {"summary_length": summary_length}
        response = requests.post(f"{BASE_URL}/summarize", files=files, data=data)
        if response.status_code == 200:
            return response.json()  # Summary result
        return None
    except requests.exceptions.RequestException as e:
        print(f"Summarization API Error: {e}")
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
