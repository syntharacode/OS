# Establish the DB engine connection
from backend.db.connection import init_db

# Load database schema definitions
from backend.db.schema import reflect_schema

# Import user model for seeding
from backend.db.models import User

# SQLAlchemy session management
from sqlalchemy.orm import Session

# This script initializes the Synthara database and seeds an admin user (if missing)
if __name__ == "__main__":
    # Initialize DB engine (creates or connects to configured database)
    engine = init_db()

    # Reflect schema and create all required tables
    reflect_schema().create_all(bind=engine)
    print("[✓] Synthara OS database initialized.")

    # Optionally seed a default admin user (for dev/testing environments)
    session = Session(bind=engine)
    if not session.query(User).filter_by(username="admin").first():
        session.add(User(username="admin", api_key="root-dev-key"))
        session.commit()
        print("[✓] Admin user seeded")
    session.close()
