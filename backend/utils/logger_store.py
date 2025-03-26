from collections import deque

# In-memory log buffer (used for frontend streaming/log viewing)
_log_buffer = deque(maxlen=100)


def log_message(message: str):
    _log_buffer.append(message)


def get_logs():
    return list(_log_buffer)

# Example usage (attach to main logger):
# from backend.utils.logger_store import log_message
# log_message("LLM started")