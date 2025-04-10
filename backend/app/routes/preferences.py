# from fastapi import APIRouter, HTTPException, Depends
# from app.services.preferences import save_preferences, get_preferences
# from app.models.users import User  #User model exists
# from app.utils.auth import get_current_user  # Dependency for user authentication

# router = APIRouter()

# @router.get("/preferences")
# async def retrieve_preferences(user: User = Depends(get_current_user)):
#     """
#     Endpoint to retrieve the current user's preferences.
#     """
#     try:
#         preferences = get_preferences(user.id)
#         return {"preferences": preferences}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error retrieving preferences: {str(e)}")


# @router.post("/preferences")
# async def update_preferences(preferences: dict, user: User = Depends(get_current_user)):
#     """
#     Endpoint to save or update the current user's preferences.
#     """
#     try:
#         save_preferences(user.id, preferences)
#         return {"message": "Preferences updated successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error saving preferences: {str(e)}")

# from fastapi import APIRouter, HTTPException, Depends
# from sqlalchemy.orm import Session
# from app.services.preferences import save_preferences, get_preferences
# from app.models.users import User
# from app.utils.auth import get_current_user
# from app.database import get_db
# import json

# router = APIRouter()

# @router.get("/preferences/{user_id}")
# async def retrieve_preferences(user_id: int, db: Session = Depends(get_db)):
#     try:
#         preferences = get_preferences(user_id, db)

#         # Fix: ensure preferences is returned as dict, not string
#         if isinstance(preferences, str):
#             try:
#                 preferences = json.loads(preferences)
#             except json.JSONDecodeError:
#                 preferences = {}

#         return preferences

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error retrieving preferences: {str(e)}")

# @router.put("/preferences/{user_id}")
# async def update_preferences(user_id: int, preferences: dict, db: Session = Depends(get_db)):
#     try:
#         save_preferences(user_id, preferences, db)
#         return {"message": "Preferences updated successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error saving preferences: {str(e)}")

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.services.preferences import save_preferences, get_preferences
from app.database import get_db

router = APIRouter()

@router.get("/preferences/{user_id}")
async def retrieve_preferences(user_id: int, db: Session = Depends(get_db)):
    try:
        return get_preferences(user_id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving preferences: {str(e)}")

@router.put("/preferences/{user_id}")
async def update_preferences(user_id: int, preferences: dict, db: Session = Depends(get_db)):
    try:
        save_preferences(user_id, preferences, db)
        return {"message": "Preferences updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving preferences: {str(e)}")
