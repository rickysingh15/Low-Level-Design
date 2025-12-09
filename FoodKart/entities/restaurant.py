from entities.interfaces import Dish
from entities.user import User
from entities.order import Order
from entities.location import Location
from entities.rating import Rating

class Restaurant():

    def __init__(self, name: str, dish_name: str, dish_price: int, dish_quantity: int, locations: list[Location] = None, orders: list[Order] = None, ratings: list[Rating] = None):
        self.name = name
        self.locations = locations or []
        self.location_map = {location.pincode: location for location in locations}
        self.orders = orders or []
        self.dish_name = dish_name
        self.dish_price = dish_price
        self.dish_quantity = dish_quantity
        self.dish = Dish(dish_name, dish_price)
        self.rating = 0.0
        self.ratings = ratings or []

    def addRating(self, rating):
        self.ratings.append(rating)
        rating_sum = 0
        for rating in self.ratings:
            rating_sum += rating.rating
        self.rating = rating_sum / len(self.ratings)

    def updateQuantity(self, quantity_to_add: int):
        self.dish_quantity += quantity_to_add


    def placeOrder(self, user: User, quantity: int):
        order = Order(user, self.dish, quantity, self)
        if quantity > self.dish_quantity:
            print("Can't place order, order is ", quantity-self.dish_quantity, " more than available quantity")
            return order
        self.orders.append(order)
        self.dish_quantity -= quantity
        return order
    
    def describeRestaurant(self):
        print(f"Name: {self.name}")
        print(f"Location: {', '.join([location.name for location in self.locations])}")
        print(f"Dish: {self.dish_name}")
        print(f"Price: {self.dish_price}")
        print(f"Quantity: {self.dish_quantity}")
        print(f"Rating: {self.rating}")


    def getRestaurantRating(self):
        return self.rating

    