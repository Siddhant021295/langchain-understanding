"""Configuration module for environment variables and settings."""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for application settings."""
    
    # OpenAI Configuration
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_ORG_ID: Optional[str] = os.getenv("OPENAI_ORG_ID")
    
    # Application Settings
    APP_ENV: str = os.getenv("APP_ENV", "development")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    @classmethod
    def is_openai_configured(cls) -> bool:
        """Check if OpenAI API key is configured."""
        return cls.OPENAI_API_KEY is not None and cls.OPENAI_API_KEY.strip() != ""
    
    @classmethod
    def get_openai_api_key(cls) -> Optional[str]:
        """Get OpenAI API key, ensuring it's not empty."""
        key = cls.OPENAI_API_KEY
        return key if key and key.strip() else None
    
    @classmethod
    def validate_config(cls) -> dict:
        """Validate configuration and return status."""
        status = {
            "openai_configured": cls.is_openai_configured(),
            "app_env": cls.APP_ENV,
            "log_level": cls.LOG_LEVEL,
        }
        return status


# Create a global config instance
config = Config()
