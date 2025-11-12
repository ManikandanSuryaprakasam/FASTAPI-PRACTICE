"""Database configuration and session dependency for SQLAlchemy.

Provides:
- SQLALCHEMY_DATABASE_URL: SQLite connection string used to create the engine.
- engine: SQLAlchemy Engine created from the database URL.
- SessionLocal: sessionmaker factory configured with the engine (autocommit=False, autoflush=False).
- Base: declarative_base() used by ORM models to define tables.
- get_db(): dependency generator that yields a SessionLocal instance and ensures it is closed after use.

This module is used by the application to create the database tables and to provide a database session to FastAPI route handlers via dependency injection.
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi-practice.db"
 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()