import os

from dotenv import load_dotenv
load_dotenv()

#from pydantic import BaseSettings
from pydantic_settings import BaseSettings

# class Settings(BaseSettings):
#     # Database Configuration
#     DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/docinsight_db")

#     # Gemini API Key
#     GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "your_gemini_api_key")

#     # Voice API Key (if any)
#     VOICE_API_KEY: str = os.getenv("VOICE_API_KEY", "your_voice_api_key")

#     # Other settings
#     ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")  # e.g., "development" or "production"
#     DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"

#     class Config:
#         env_file = ".env"  # Load from .env file

from pydantic_settings import BaseSettings

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