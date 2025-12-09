from entities.user import User
from uuid import uuid4
from entities.rating import Rating

class Order():

    def __init__(self, user: User, dish: str, quantity: int, restaurant = None):
        self.id = uuid4()
        self.user = user
        self.dish = dish
        self.quantity = quantity
        self.restaurant = restaurant

    def rateRestaurant(self, rating: int, comment: str):
        rating = Rating(self.user, rating, comment)
        self.restaurant.addRating(rating)

    def describeOrder(self):
        print(f"Order ID: {self.id}")
        print(f"User: {self.user.name}")
        print(f"Dish: {self.dish}")
        print(f"Quantity: {self.quantity}")