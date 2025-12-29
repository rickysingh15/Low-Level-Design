
import threading
from user import User
from typing import Dict

class UserService:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "initialized"):
            self.initialized: True
            self.users: Dict[str, User] = {} 

    def create_user(self, name: str, email: str):
        user = User(name, email)
        self.users[user.get_id] = user
        return user
    
    def get_user(self, user_id: str):
        user = None
        if user_id in self.users:
            user = self.users[user_id]
        if not user:
            print("Invalid user")
        return user
    
    def add_upvote_to_user(self, user: User):
        print("user service called for upvoting a user ", user)
        if user:
            user.add_vote()
            return True
        return False
    
    def add_downvote_to_user(self, user: User):
        if user:
            user.dec_vote()
            return True
        return False
    
    def add_contribution_to_user(self, user: User):
        if user:
            user.add_contribution()
            return True
        return False
    
    def get_score(self, user: User):
        if user:
            return user.get_score()
        return None