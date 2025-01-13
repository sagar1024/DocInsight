from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

# User Model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)  # To manage account status
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    preferences = relationship("Preference", back_populates="user", uselist=False)
    chat_history = relationship("ChatHistory", back_populates="user")

# Preference Model
class Preference(Base):
    __tablename__ = "preferences"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    summary_length = Column(String, default="medium")  # Options: 'short', 'medium', 'long'
    focus_sections = Column(Text, nullable=True)  # JSON format for selected sections
    language = Column(String, default="en")  # Language preference, e.g., 'en', 'es', 'fr'

    # Relationship
    user = relationship("User", back_populates="preferences")

# Chat History Model
class ChatHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    question = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationship
    user = relationship("User", back_populates="chat_history")

# Document Model (Optional: If you need to store uploaded document metadata)
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Null for visitors
    name = Column(String, nullable=False)  # Document name
    file_type = Column(String, nullable=False)  # e.g., 'pdf', 'docx'
    upload_date = Column(DateTime, default=datetime.utcnow)
    content = Column(Text, nullable=True)  # Optional: store document text content

    # Relationship
    user = relationship("User")
