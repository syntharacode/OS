# Import SQLAlchemy column types and utility functions
from sqlalchemy import Column, Integer, String, DateTime, Text, func

# Import the declarative base from the Synthara DB module
from backend.db.connection import Base

# Database model for logging prompts received by the system
class PromptLog(Base):
    __tablename__ = "prompt_logs"

    id = Column(Integer, primary_key=True, index=True)  # Unique identifier
    prompt = Column(Text, nullable=False)               # The raw prompt text
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Timestamp (auto-filled)

# Database model for registered users of the system
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)               # Unique user ID
    username = Column(String(100), unique=True, nullable=False)      # Unique username
    api_key = Column(String(256), unique=True, nullable=False)       # Unique API key for access
    created_at = Column(DateTime(timezone=True), server_default=func.now())  # Account creation timestamp
