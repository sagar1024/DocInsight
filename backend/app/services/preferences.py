from sqlalchemy.orm import Session
from app.models.user import User

def get_preferences(user_id: int, db: Session) -> dict:
    """
    Retrieve user preferences from the database.
    
    Args:
        user_id (int): The ID of the user.
        db (Session): The database session.
    
    Returns:
        dict: The user's preferences.
    """
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user and user.preferences:
            return user.preferences
        return {}
    except Exception as e:
        raise ValueError(f"Failed to retrieve preferences: {str(e)}")

def save_preferences(user_id: int, preferences: dict, db: Session) -> None:
    """
    Save or update user preferences in the database.
    
    Args:
        user_id (int): The ID of the user.
        preferences (dict): The preferences to save.
        db (Session): The database session.
    """
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.preferences = preferences
            db.commit()
        else:
            raise ValueError("User not found")
    except Exception as e:
        raise ValueError(f"Failed to save preferences: {str(e)}")
