from sqlalchemy.orm import Session
from backend.db.connection import get_db
from backend.db.models import PromptLog
from backend.data.cleaner import full_clean  # NEU

# Memory service stores and retrieves user interaction history

def log_prompt(prompt: str):
    db: Session = next(get_db())
    cleaned = full_clean(prompt)  # CLEAN BEFORE STORING
    entry = PromptLog(prompt=cleaned)
    db.add(entry)
    db.commit()

def get_recent_prompts(limit: int = 10):
    db: Session = next(get_db())
    return (
        db.query(PromptLog)
        .order_by(PromptLog.created_at.desc())
        .limit(limit)
        .all()
    )
