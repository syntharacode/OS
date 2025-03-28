
# logger_store.py

import logging

# This example uses a simple in-memory log store.
# In production, you might read from a file or logging backend.
LOG_STORE = []

def add_log(record: str, level: str = "INFO"):
    LOG_STORE.append({"level": level.upper(), "message": record})

def get_logs(limit=50, level=None):
    # Optional filtering by log level
    filtered_logs = LOG_STORE
    if level:
        level = level.upper()
        filtered_logs = [log for log in LOG_STORE if log["level"] == level]
    
    # Return the most recent 'limit' logs
    return filtered_logs[-limit:]
