from backend.db.connection import Base
from backend.db.models import PromptLog, User

# This file allows pre-import aggregation of all models for automatic creation

def reflect_schema():
    return Base.metadata

# Optional use:
# reflect_schema().create_all(bind=engine)