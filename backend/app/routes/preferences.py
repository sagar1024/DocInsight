from fastapi import APIRouter, HTTPException, Depends
from app.services.preferences import save_preferences, get_preferences
from app.models.user import User  # Assuming a User model exists
from app.utils.auth import get_current_user  # Dependency for user authentication

router = APIRouter()

@router.get("/preferences")
async def retrieve_preferences(user: User = Depends(get_current_user)):
    """
    Endpoint to retrieve the current user's preferences.
    """
    try:
        preferences = get_preferences(user.id)
        return {"preferences": preferences}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving preferences: {str(e)}")


@router.post("/preferences")
async def update_preferences(preferences: dict, user: User = Depends(get_current_user)):
    """
    Endpoint to save or update the current user's preferences.
    """
    try:
        save_preferences(user.id, preferences)
        return {"message": "Preferences updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving preferences: {str(e)}")
