from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from .. import schemas, models, utils
from ..database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

# User registration
@router.post("/register", response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if the user already exists
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    
    # Hash the user's password and create the user
    hashed_password = utils.auth.hash_password(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# User login
@router.post("/login", response_model=schemas.Token)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Authenticate the user
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user or not utils.auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    # Generate an access token
    access_token_expires = timedelta(minutes=utils.auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = utils.auth.create_access_token(data={"sub": user.id}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

# Get the current user
@router.get("/me", response_model=schemas.UserResponse)
def get_current_user(token: str, db: Session = Depends(get_db)):
    user_id = utils.auth.decode_access_token(token)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
    
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user
