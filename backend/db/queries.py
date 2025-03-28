# Import SQLAlchemy session type for type hints
from sqlalchemy.orm import Session

# Import Synthara database models
from backend.db.models import PromptLog, User

# General-purpose query helpers for interacting with the Synthara database

# Retrieve recent prompt logs with an optional limit (default: 100)
def get_all_prompts(db: Session, limit: int = 100):
    return db.query(PromptLog).order_by(PromptLog.created_at.desc()).limit(limit).all()

# Retrieve a user object by their username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Delete a prompt log by its ID
# Returns True if deleted, False if no matching record found
def delete_prompt_by_id(db: Session, prompt_id: int):
    prompt = db.query(PromptLog).filter(PromptLog.id == prompt_id).first()
    if prompt:
        db.delete(prompt)
        db.commit()
        return True
    return False
