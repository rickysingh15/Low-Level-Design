from entities.restaurant import Restaurant
from entities.user import User
from entities.interfaces import RestaurantLister

class RestaurantService:

    _instance = None
    def __new__(cls):
        if cls._instance is None:
           cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, restaurants: list[Restaurant] = None, users: list[User] = None, user: User = None):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.restaurants = restaurants or []
            self.users = users or []
            self.logged_in_user = user

    def addRestaurant(self, restaurant: Restaurant):
        self.restaurants.append(restaurant)

    def addUser(self, user: User):
        self.users.append(user)

    def getAvailableRestaurants(self):
        available_restaurants = []
        user_location = self.logged_in_user.location
        for restaurant in self.restaurants:
            if restaurant.location_map.get(user_location.pincode, None) is not None and restaurant.dish_quantity > 0:
                available_restaurants.append(restaurant)

        return available_restaurants
    
    def showRestaurants(self):
        restaurants = self.getAvailableRestaurants()
        result = []
        for restaurant in restaurants:
            obj = {"Name": restaurant.name,
                    "Dish": restaurant.dish.name,
                    "Price": restaurant.dish.price}
            result.append(obj)

        return result
    
    def orderOnline(self, restaurant_name: str, quantity: int):
        for restaurant in self.restaurants:
            if restaurant.name == restaurant_name:
                order = restaurant.placeOrder(self.logged_in_user, quantity)
                return order



class RatingLister(RestaurantLister):

    def __init__(self):
        pass

    def listRestaurants(self, lis, parameter: int):
        result = sorted(lis, key=lambda x: x.rating, reverse=True)
        return result


class PriceLister(RestaurantLister):

    def __init__(self):
        pass

    def listRestaurants(self, lis, parameter: int):
        result = sorted(lis, key=lambda x: x.dish.price, reverse=True)
        return result