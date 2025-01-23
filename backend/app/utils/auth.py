# from passlib.context import CryptContext
# from jose import JWTError, jwt
# from datetime import datetime, timedelta

# # Configuration for password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # JWT configuration
# SECRET_KEY = "your_secret_key"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# # Hash the password
# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)

# # Verify password
# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

# # Create an access token
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# # Verify access token
# def decode_access_token(token: str):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         user_id: int = payload.get("sub")
#         if user_id is None:
#             raise ValueError("Invalid token payload")
#         return user_id
#     except JWTError:
#         return None
