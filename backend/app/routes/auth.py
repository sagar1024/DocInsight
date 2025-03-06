from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta
from .. import schemas, models, utils
from ..utils.auth import hash_password, verify_password, create_access_token, decode_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from ..database import get_db
from app.models.users import User
from app.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])

#User registration
# @router.post("/register", response_model=UserResponse)
# def register_user(user: UserCreate, db: Session = Depends(get_db)):
#     #Checking if the user already exists
#     existing_user = db.query(User).filter(User.email == user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
#     new_user = User(
#         username=user.username,
#         email=user.email,
#         hashed_password=hash_password(user.password)
#         )
    
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
    
#     return {"message": "User registered successfully", "user_id": new_user.id}

@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    #Checking if the user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    new_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
        )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

# User login
@router.post("/login", response_model=schemas.Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Authenticate the user
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Generate an access token
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.id}, expires_delta=access_token_expires)
    
    return {
    "access_token": access_token,
    "token_type": "bearer",
    "user": user
    }

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")  # Token URL
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = decode_access_token(token)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")    
    return user
