from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime, LargeBinary
from app.database import Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Document(Base):
    """
    Document model for database.
    """
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    filename = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    summary = Column(Text, nullable=True)
    upload_time = Column(DateTime, default=datetime.utcnow)
    
    # Establish a relationship with the User model
    user = relationship("User", back_populates="documents")
    
    def __repr__(self):
        return f"<Document(filename={self.filename}, upload_time={self.upload_time})>"

class ImageData(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    image = Column(LargeBinary, nullable=False)
    ocr_text = Column(String, nullable=True)
