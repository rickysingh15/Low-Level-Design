from entities.restaurantService import RestaurantService
from entities.user import User

class LoginService:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.restaurant_service = RestaurantService()

    def loginUser(self, id: int) -> bool:
        for registered_user in self.restaurant_service.users:
            if id == registered_user.id:
                self.restaurant_service.logged_in_user = registered_user
                return True
            
        print("Not registerd user")
        return False
    
    def getLoggedInUser(self):
        return self.restaurant_service.logged_in_user