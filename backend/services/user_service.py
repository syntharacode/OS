from sqlalchemy.orm import Session
from backend.db.models import User
from backend.db.connection import get_db
from uuid import uuid4


def create_user(username: str) -> str:
    db: Session = next(get_db())
    api_key = str(uuid4())
    user = User(username=username, api_key=api_key)
    db.add(user)
    db.commit()
    db.refresh(user)
    return api_key


def get_user_by_key(api_key: str):
    db: Session = next(get_db())
    return db.query(User).filter(User.api_key == api_key).first()


def get_user_by_name(username: str):
    db: Session = next(get_db())
    return db.query(User).filter(User.username == username).first()