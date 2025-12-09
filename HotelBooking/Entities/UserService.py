from Entities.User import User


class UserService:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.users = dict()


    def register_user(self, name: str, email: str, phone: str, location_name: str, pincode: str) -> User:
        user = User(name, email, phone, location_name, pincode)
        self.users[phone] = user
        print("User registered successfully")
        return user
    
    def login_user(self, phone: str):
        if phone in self.users:
            print("User logged in successfully")
            return self.users[phone]

        print("User not found")
        return None
