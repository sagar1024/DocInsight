import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

#Database URL from config
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://sagar:password@localhost/docinsight_db")

#SQLAlchemy setup
#Create the database engine
engine = create_engine(DATABASE_URL)

#Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Define the base class for models
Base = declarative_base()

def get_db():
    """
    Provides a database session.
    """
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
        