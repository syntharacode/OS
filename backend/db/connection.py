from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DB_URL = os.getenv("DATABASE_URL", "postgresql://synthara:synthpass@localhost/synthdb")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)
    print("[SyntharaOS] Database initialized.")
    return engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()