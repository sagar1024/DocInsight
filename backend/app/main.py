# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from .routes import auth, summarization
# from .database import engine, Base

# # Initialize the database
# Base.metadata.create_all(bind=engine)

# # Initialize FastAPI app
# app = FastAPI(
#     title="DocInsight",
#     description="An AI-powered application for summarizing and analyzing documents",
#     version="1.0.0",
# )

# # CORS settings
# origins = [
#     "http://localhost:3000",  # Replace with your frontend's origin
#     "https://your-production-frontend.com"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Include routers
# app.include_router(auth.router)
# app.include_router(summarization.router)

# @app.get("/")
# def root():
#     return {"message": "Welcome to DocInsight!"}

from fastapi import FastAPI
from app.routes import summarization, chatbot, voice, preferences
from app.database import Base, engine

# Initialize database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app instance
app = FastAPI(
    title="DocInsight API",
    description="API for the DocInsight AI-powered document summarization and analysis application",
    version="1.0.0"
)

# Health Check Route
@app.get("/")
def health_check():
    return {"message": "Welcome to DocInsight"}

# Include routers
app.include_router(summarization.router, prefix="/summarize", tags=["Summarization"])
app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(voice.router, prefix="/voice", tags=["Voice"])
app.include_router(preferences.router, prefix="/preferences", tags=["Preferences"])
