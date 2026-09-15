from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

# Create the SQLAlchemy engine
engine = create_engine(settings.database_url)

# SessionLocal class will act as a factory for new database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our SQLAlchemy models
Base = declarative_base()

# Dependency for FastAPI routers to yield a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
