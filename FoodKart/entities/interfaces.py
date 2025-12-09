from abc import ABC, abstractmethod
from entities.location import Location
from entities.order import Order

class Orderable(ABC):

    def __init__(self, number: int):
        pass

class Dish(ABC):

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class RestaurantLister(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def listRestaurants(self, list, parameter: int):
        pass