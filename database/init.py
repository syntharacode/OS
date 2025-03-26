from backend.db.connection import init_db
from backend.db.schema import reflect_schema
from backend.db.models import User
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = init_db()
    reflect_schema().create_all(bind=engine)
    print("[✓] Synthara OS database initialized.")

    # Optional: seed admin user
    session = Session(bind=engine)
    if not session.query(User).filter_by(username="admin").first():
        session.add(User(username="admin", api_key="root-dev-key"))
        session.commit()
        print("[✓] Admin user seeded")
    session.close()