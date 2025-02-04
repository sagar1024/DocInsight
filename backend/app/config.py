import os

from dotenv import load_dotenv
load_dotenv()

#from pydantic import BaseSettings
from pydantic_settings import BaseSettings

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is not set. Check your .env file.")

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    log_level: str
    gemini_api_key: str  # Add this field
    voice_api_key: str   # Add this field
    debug: bool          # Add this field

    class Config:
        env_file = ".env"  # Load from .env file

# Load settings
settings = Settings()