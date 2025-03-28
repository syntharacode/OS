# Import SQLAlchemy core and ORM tools
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Import OS module for reading environment variables
import os

# Get the database connection URL from environment (with fallback)
DB_URL = os.getenv("DATABASE_URL", "postgresql://synthara:synthpass@localhost/synthdb")

# Create the SQLAlchemy engine instance (core connection handler)
engine = create_engine(DB_URL)

# Create a configured session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative model definitions
Base = declarative_base()

# Initialize the database (create all tables)
def init_db():
    Base.metadata.create_all(bind=engine)
    print("[SyntharaOS] Database initialized.")
    return engine

# Dependency for FastAPI route functions to provide a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
