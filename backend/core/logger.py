import logging
import sys
from backend.utils.logger_store import log_message

logger = logging.getLogger("synthara")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
console_handler.setFormatter(formatter)

# In-memory log handler
class MemoryLogHandler(logging.Handler):
    def emit(self, record):
        msg = self.format(record)
        log_message(msg)

memory_handler = MemoryLogHandler()
memory_handler.setFormatter(formatter)

# Attach handlers (if not already attached)
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(memory_handler)

# Usage:
# from backend.core.logger import logger
# logger.info("Synthara OS started")