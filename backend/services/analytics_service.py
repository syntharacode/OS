from sqlalchemy import func
from backend.db.connection import get_db
from backend.db.models import PromptLog
from sqlalchemy.orm import Session


def get_most_common_prompts(limit: int = 20):
    db: Session = next(get_db())
    results = (
        db.query(PromptLog.prompt, func.count(PromptLog.prompt).label("count"))
        .group_by(PromptLog.prompt)
        .order_by(func.count(PromptLog.prompt).desc())
        .limit(limit)
        .all()
    )
    return [{"prompt": r[0], "count": r[1]} for r in results]