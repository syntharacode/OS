# Import OS module to access environment variables
import os

# Load environment variables from a .env file (if present)
from dotenv import load_dotenv

# Load variables into the process environment
load_dotenv()

# Define system-wide configuration settings for Synthara OS
class Settings:
    # Project metadata
    PROJECT_NAME: str = "SyntharaOS"
    VERSION: str = "0.1.0"

    # Model configuration (default is Falcon 1B if not overridden)
    MODEL_NAME: str = os.getenv("MODEL_NAME", "tiiuae/falcon-rw-1b")

    # Database connection URL
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://synthara:synthpass@localhost/synthdb")

    # Debug mode toggle
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    # Model generation defaults
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", 100))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", 0.7))

# Create a global settings instance for use throughout the OS
settings = Settings()
