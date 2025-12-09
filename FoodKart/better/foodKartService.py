
from better.user import User
from better.restaurant import Restaurant
from better.location import Location
from better.dish import Dish
from better.ConcreteLister import RatingsLister, PricesLister
from better.order import Order

class FoodKartService():
    
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, restaurant: list[Restaurant] = None):
        if not hasattr(self, "_initialized"):
            self._initialized = True
        self.users = {}
        self.restaurants = restaurant or []
        self.logged_in_user = None

    def register_user(self, id: int, name: str, gender: str, phone: str, location_name: str, pincode: str) -> User:
        if phone in self.users:
            print("User already registered")
            return self.users[phone]
        location = Location(location_name, pincode)
        user = User(id, name, gender, phone, location)
        self.users[phone] = user
        return user

    def register_restaurant(self, name: str, dish_name: str, dish_price: int, dish_quantity: int, locations: list) -> Restaurant:

        if self.logged_in_user is None:
            print("No user logged in")
            return None
        
        dish = Dish(dish_name, dish_price)
        restaurant = Restaurant(name, dish_name, dish_price, dish_quantity, self.logged_in_user)
        restaurant.dish = dish
        for loc in locations:
            location = Location(loc[0], loc[1])
            restaurant.locations.append(location)

        self.restaurants.append(restaurant)
        return restaurant
    
    def login_user(self, phone: str) -> User:
        if phone not in self.users:
            print("User not registered")
            return None
        self.logged_in_user = self.users[phone]
        return self.logged_in_user
    

    def updateQuantity(self, restaurant_name: str, quantity_to_add: int):
        if not self.logged_in_user:
            print("No user logged in")
            return False
        res = None
        for restaurant in self.restaurants:
            if restaurant.name == restaurant_name:
                res = restaurant
                break

        if res is None:
            print("Restaurant not found")
            return False
        
        if res.owner != self.logged_in_user:
            print("Only owner can update quantity")
            return False
        
        res.updateQuantity(quantity_to_add)
        return True

    def showRestaurants(self, param: str, order: str):
        l = []
        for res in self.restaurants:
            if res.dish_quantity > 0:
                l.append(res)   

        print("filtered restaurants:", [r.name for r in l])
        lister = None
        if param == "ratings":
            lister = RatingsLister()
        elif param == "prices":
            lister = PricesLister()
        return lister.listRestaurants(l, order)
    
    def orderOnline(self, restaurant_name: str, quantity: int):
        if not self.logged_in_user:
            print("No user logged in")
            return None
        
        restaurant = None
        for res in self.restaurants:
            if res.name == restaurant_name:
                restaurant = res
                break
        
        if restaurant is None:
            print("Restaurant not found")
            return None
        
        return restaurant.placeOrder(self.logged_in_user, quantity)

    def rateRestaurant(self, order: Order, rating: int, comment: str):
        order.rateOrder(rating, comment)
        