from abc import ABC, abstractmethod
from Entities.Calendar import Calendar

class Room(ABC):

    def __init__(self, count: int, price: int, capacity: int):
        self.count = count
        self.price = price
        self.capacity = capacity
        self.calendar = Calendar(self.count, self.capacity)

    @abstractmethod
    def book_room(self):
        pass