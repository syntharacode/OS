# Import SQLAlchemy session type
from sqlalchemy.orm import Session

# Import DB session generator
from backend.db.connection import get_db

# Import PromptLog model for logging user inputs
from backend.db.models import PromptLog

# Memory service stores and retrieves user interaction history

# Save a prompt into the database for historical tracking
def log_prompt(prompt: str):
    db: Session = next(get_db())         # Open a database session
    entry = PromptLog(prompt=prompt)     # Create a new log entry
    db.add(entry)                        # Add the entry to the session
    db.commit()                          # Commit the transaction

# Retrieve the most recent prompts submitted to the system
def get_recent_prompts(limit: int = 10):
    db: Session = next(get_db())         # Open a database session
    return (
        db.query(PromptLog)              # Query all prompt logs
        .order_by(PromptLog.created_at.desc())  # Sort by most recent first
        .limit(limit)                    # Limit the number of returned entries
        .all()
    )
