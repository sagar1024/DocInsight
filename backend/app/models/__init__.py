from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import all models
from .user import User
from .document import Document
