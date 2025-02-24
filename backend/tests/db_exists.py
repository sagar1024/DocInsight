from app.database import SessionLocal
from app.models import User

# Create a new database session
db = SessionLocal()

# Fetch all users (to verify if the table exists)
users = db.query(User).all()

# Print the retrieved data
print(users)

# Close the session
db.close()
