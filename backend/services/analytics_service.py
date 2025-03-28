# Import SQL aggregation function for counting
from sqlalchemy import func

# Import DB session generator
from backend.db.connection import get_db

# Import PromptLog model (used to store all submitted prompts)
from backend.db.models import PromptLog

# Import SQLAlchemy session type
from sqlalchemy.orm import Session

# Retrieve the most frequently used prompt texts from the database
def get_most_common_prompts(limit: int = 20):
    db: Session = next(get_db())  # Get a new database session

    # Perform grouped count on prompt texts, order by frequency
    results = (
        db.query(PromptLog.prompt, func.count(PromptLog.prompt).label("count"))
        .group_by(PromptLog.prompt)
        .order_by(func.count(PromptLog.prompt).desc())
        .limit(limit)
        .all()
    )

    # Return list of prompt strings with associated usage counts
    return [{"prompt": r[0], "count": r[1]} for r in results]
