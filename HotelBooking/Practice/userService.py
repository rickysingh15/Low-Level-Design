


class UserService:
    _instance = None
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.users = dict()





class BookingService:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.bookings = dict()


















user1 = UserService()
user2  = UserService()
user3  = UserService()

if user1 is user3:
    print("same")
else:
    print("not same")


