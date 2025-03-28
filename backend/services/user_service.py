# Import SQLAlchemy session handling
from sqlalchemy.orm import Session

# Import User model from Synthara DB schema
from backend.db.models import User

# Import DB session generator
from backend.db.connection import get_db

# Import UUID generator for creating secure API keys
from uuid import uuid4

# Create a new user with a unique API key
def create_user(username: str) -> str:
    db: Session = next(get_db())  # Get a DB session
    api_key = str(uuid4())        # Generate a unique API key
    user = User(username=username, api_key=api_key)
    db.add(user)
    db.commit()
    db.refresh(user)              # Refresh to get auto-generated fields (e.g. ID)
    return api_key

# Fetch a user by their API key
def get_user_by_key(api_key: str):
    db: Session = next(get_db())
    return db.query(User).filter(User.api_key == api_key).first()

# Fetch a user by their username
def get_user_by_name(username: str):
    db: Session = next(get_db())
    return db.query(User).filter(User.username == username).first()
