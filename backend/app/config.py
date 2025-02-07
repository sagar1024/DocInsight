# import os
# from dotenv import load_dotenv

# load_dotenv()

# #from pydantic import BaseSettings
# from pydantic_settings import BaseSettings

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# if not GEMINI_API_KEY:
#     raise ValueError("GEMINI_API_KEY is not set. Check your .env file.")

# class Settings(BaseSettings):
#     database_url: str
#     secret_key: str
#     algorithm: str
#     access_token_expire_minutes: int
#     log_level: str
#     gemini_api_key: str  # Add this field
#     voice_api_key: str   # Add this field
#     debug: bool          # Add this field

#     class Config:
#         env_file = ".env"  # Load from .env file

# # Load settings
# settings = Settings()

import os
from dotenv import load_dotenv

#Explicitly load .env file
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(dotenv_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Check your .env file.")

#print(f"Loaded GEMINI_API_KEY: {GEMINI_API_KEY}")  # Debugging line

#Define the Settings class
class Settings:
    def __init__(self):
        self.GEMINI_API_KEY = GEMINI_API_KEY

#Create the settings instance
settings = Settings()