import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    # Database Configuration
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://user:sagar@localhost/docinsight_db")

    # Gemini API Key
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "AIzaSyC6P9NKEWJIA_O2nqsMR8swyTaqzghRZj8")

    # Voice API Key (if any)
    VOICE_API_KEY: str = os.getenv("VOICE_API_KEY", "your_voice_api_key")

    # Other settings
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")  # e.g., "development" or "production"
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"

    class Config:
        env_file = ".env"  # Load from .env file

# Create a settings object to use across the app
settings = Settings()
