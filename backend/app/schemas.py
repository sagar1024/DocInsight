from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# Base User Schema
class UserBase(BaseModel):
    email: EmailStr

# User Creation Schema
class UserCreate(UserBase):
    username: str
    email: EmailStr
    password: str

# User Response Schema
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

# Login Schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Preference Schema
class PreferenceBase(BaseModel):
    summary_length: Optional[str] = Field(default="medium", description="Summary length: 'short', 'medium', 'long'")
    focus_sections: Optional[str] = Field(default=None, description="Selected sections in JSON format")
    language: Optional[str] = Field(default="en", description="Language preference, e.g., 'en', 'es', 'fr'")

class PreferenceCreate(PreferenceBase):
    pass

class PreferenceResponse(PreferenceBase):
    user_id: int

    class Config:
        orm_mode = True

# Chat History Schema
class ChatHistoryBase(BaseModel):
    question: str
    response: str

class ChatHistoryCreate(ChatHistoryBase):
    pass

class ChatHistoryResponse(ChatHistoryBase):
    id: int
    user_id: int
    timestamp: datetime

    class Config:
        orm_mode = True

# Token Schema
class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse

class TokenData(BaseModel):
    id: Optional[int] = None
