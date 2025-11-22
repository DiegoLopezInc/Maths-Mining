"""Configuration for the math validation system."""

import os
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration settings for math validation."""
    
    # OpenAI API settings
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.1"))
    
    # Validation settings
    MAX_RETRIES: int = 3
    TIMEOUT: int = 30
    
    @classmethod
    def is_configured(cls) -> bool:
        """Check if the configuration is valid."""
        return cls.OPENAI_API_KEY is not None and len(cls.OPENAI_API_KEY) > 0


# Global config instance
config = Config()
