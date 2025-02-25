from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    """
    User model for database.
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    preferences = Column(String, nullable=True)  # JSON string to store user preferences
    
    documents = relationship("Document", back_populates="user")
    
    def __repr__(self):
        return f"<User(username={self.username}, email={self.email}, is_active={self.is_active})>"
    