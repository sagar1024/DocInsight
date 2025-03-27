from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.routes import summarization, chatbot, auth, voice, preferences
from app.database import Base, engine
from fastapi.staticfiles import StaticFiles

import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

#Initialize database tables
Base.metadata.create_all(bind=engine)

#Create FastAPI app instance
app = FastAPI(
    title="DocInsight API",
    description="API for the DocInsight AI-powered document summarization and analysis application",
    version="1.0.0"
)

#Serve generated audio files
app.mount("/generated_audio", StaticFiles(directory="generated_audio"), name="audio")

#Health Check Route
@app.get("/")
def health_check():
    return {"message": "Welcome to DocInsight"}

#Include routers

#app.include_router(summarization.router, prefix="/summarize", tags=["Summarization"])
app.include_router(summarization.router)
#app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])
app.include_router(chatbot.router)
app.include_router(auth.router)
app.include_router(voice.router)
app.include_router(preferences.router, prefix="/preferences", tags=["Preferences"])

# Global Exception Handler for Debugging
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error. Check logs for details."},
    )
    