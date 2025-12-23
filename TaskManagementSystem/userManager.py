
from user import User
class UserManager:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, users: dict[str, User] = None):
        if not hasattr(self, "_initialized"):
            self.initialized = True
            self.users = users or {}


    def create_user(self, name: str):
        user = User(name)
        self.users[user.id] = user
        return user
    