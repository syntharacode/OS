import logging
from backend.core.config import settings
from backend.models.loader import load_model
from backend.db.connection import init_db

logger = logging.getLogger("synthara")

class SyntharaEngine:
    def __init__(self):
        self.model = None
        self.db = None

    def boot(self):
        logger.info("[SyntharaOS] Booting core engine...")
        self.db = init_db()
        self.model = load_model()
        logger.info("[SyntharaOS] Core boot completed.")

    def get_model(self):
        return self.model

    def get_db(self):
        return self.db

# Global instance of the SyntharaOS Engine
engine = SyntharaEngine()
