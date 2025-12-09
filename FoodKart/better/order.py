from better.user import User
from better.rating import Rating
from uuid import uuid4

class Order():

    def __init__(self, user: User, quantity: int, restaurant = None):
        self.id = uuid4()
        self.user = user
        self.dish = restaurant.dish
        self.quantity = quantity
        self.restaurant = restaurant


    def describeOrder(self):
        print(f"Order ID: {self.id}")
        print(f"User: {self.user.name}")
        print(f"Dish: {self.dish}")
        print(f"Quantity: {self.quantity}")

    def rateOrder(self, rating: int, comment: str):
        rating = Rating(self.user, rating, comment)
        self.restaurant.addRating(rating)