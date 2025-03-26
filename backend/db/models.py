from sqlalchemy import Column, Integer, String, DateTime, Text, func
from backend.db.connection import Base

class PromptLog(Base):
    __tablename__ = "prompt_logs"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, nullable=False)
    api_key = Column(String(256), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())