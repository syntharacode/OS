import logging

# Load global system settings (e.g. model paths, DB URIs, etc.)
from backend.core.config import settings

# Load the LLM model into memory
from backend.models.loader import load_model

# Initialize database connection
from backend.db.connection import init_db

# Create a named logger for Synthara
logger = logging.getLogger("synthara")


# SyntharaEngine is the central bootstrap class responsible for initializing
# all core subsystems: database and LLM model.
class SyntharaEngine:
    def __init__(self):
        self.model = None  # Will hold the active LLM instance
        self.db = None     # Will hold the active DB connection/session

    # Bootstraps the engine: connects to DB and loads the model
    def boot(self):
        logger.info("[SyntharaOS] Booting core engine...")
        self.db = init_db()         # Establish database connection
        self.model = load_model()   # Load the LLM model
        logger.info("[SyntharaOS] Core boot completed.")

    # Accessor for the loaded LLM model
    def get_model(self):
        return self.model

    # Accessor for the DB connection/session
    def get_db(self):
        return self.db


# Global singleton instance of the Synthara Engine
engine = SyntharaEngine()
