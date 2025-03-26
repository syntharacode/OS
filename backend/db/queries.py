from sqlalchemy.orm import Session
from backend.db.models import PromptLog, User

# General-purpose query helpers

def get_all_prompts(db: Session, limit: int = 100):
    return db.query(PromptLog).order_by(PromptLog.created_at.desc()).limit(limit).all()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def delete_prompt_by_id(db: Session, prompt_id: int):
    prompt = db.query(PromptLog).filter(PromptLog.id == prompt_id).first()
    if prompt:
        db.delete(prompt)
        db.commit()
        return True
    return False