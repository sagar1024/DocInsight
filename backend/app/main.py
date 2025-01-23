from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routes import auth, summarization
from .database import engine, Base

# Initialize the database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="DocInsight",
    description="An AI-powered application for summarizing and analyzing documents",
    version="1.0.0",
)

# CORS settings
origins = [
    "http://localhost:3000",  # Replace with your frontend's origin
    "https://your-production-frontend.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router)
app.include_router(summarization.router)

@app.get("/")
def root():
    return {"message": "Welcome to DocInsight!"}
