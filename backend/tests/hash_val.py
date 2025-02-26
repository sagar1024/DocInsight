from ..app.utils.auth import hash_password
from ..app.routes.auth import User

user = User()

print("Hashed Password:", hash_password(user.password))
