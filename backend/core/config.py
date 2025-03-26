import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "SyntharaOS"
    VERSION: str = "0.1.0"
    MODEL_NAME: str = os.getenv("MODEL_NAME", "tiiuae/falcon-rw-1b")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://synthara:synthpass@localhost/synthdb")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    MAX_TOKENS: int = int(os.getenv("MAX_TOKENS", 100))
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", 0.7))

settings = Settings()