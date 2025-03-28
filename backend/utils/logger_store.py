# logger_store.py

import logging

# This example uses a simple in-memory log store.
# In production, you might read from a file or logging backend.
LOG_STORE = []  # Global in-memory list to hold log records

# Add a log entry to the in-memory store
def add_log(record: str, level: str = "INFO"):
    LOG_STORE.append({
        "level": level.upper(),  # Normalize log level to uppercase
        "message": record         # Store the actual log message
    })

# Retrieve log entries with optional level filtering and pagination
def get_logs(limit=50, level=None):
    # Optional filtering by log level (e.g., "INFO", "ERROR")
    filtered_logs = LOG_STORE
    if level:
        level = level.upper()
        filtered_logs = [log for log in LOG_STORE if log["level"] == level]
    
    # Return the most recent 'limit' number of logs
    return filtered_logs[-limit:]
