from entities.user import User
from entities.restaurant import Restaurant
from entities.location import Location
from entities.restaurantService import RestaurantService

class RegisterService:

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.restaurant_service = RestaurantService()

    def register_user(self, id: int, name: str, gender: str, phone: str, location_name: str, pincode: str) -> User:
        location = Location(location_name, pincode)
        user = User(id, name, gender, phone, location)
        self.restaurant_service.addUser(user)
        return user

    def register_restaurant(self, name: str, dish_name: str, dish_price: int, dish_quantity: int, locations: list) -> Restaurant:
        l = []
        for inp in locations:
            location = Location(inp[0], inp[1])
            l.append(location)
        restaurant = Restaurant(name, dish_name, dish_price, dish_quantity, l)
        self.restaurant_service.addRestaurant(restaurant)
        print("Restaurant registered successfully")
        return restaurant