from better.rating import Rating
from better.location import Location
from better.order import Order
from better.dish import Dish
from better.user import User


class Restaurant():

    def __init__(self, name: str, dish_name: str, dish_price: int, dish_quantity: int, owner: User, locations: list[Location] = None, orders: list[Order] = None, ratings: list[Rating] = None):
        self.name = name
        self.dish_name = dish_name
        self.dish_price = dish_price
        self.dish_quantity = dish_quantity
        self.dish = Dish(dish_name, dish_price)
        self.rating = 0.0
        self.locations = locations or []
        self.orders = orders or []
        self.ratings = ratings or []
        self.owner = owner

    def addRating(self, rating: Rating):
        rating_sum = 0
        self.ratings.append(rating)
        for rating in self.ratings:
            rating_sum += rating.rating
        self.rating = rating_sum / len(self.ratings)


    def updateQuantity(self, quantity_to_add: int):
        self.dish_quantity += quantity_to_add


    def placeOrder(self, user: User, quantity: int):
        if quantity > self.dish_quantity:
            print("Can't place order, order is ", quantity-self.dish_quantity, " more than available quantity")
            return None
        order = Order(user, quantity, self)
        self.dish_quantity -= quantity
        self.orders.append(order)
        return order
    
    def describeRestaurant(self):
        print(f"Name: {self.name}")
        print(f"Location: {', '.join([location.name for location in self.locations])}")
        print(f"Dish: {self.dish_name}")
        print(f"Price: {self.dish_price}")
        print(f"Quantity: {self.dish_quantity}")
        print(f"Rating: {self.rating}")
        print(f"Owner: {self.owner.name} \n")