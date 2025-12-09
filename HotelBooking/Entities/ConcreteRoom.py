from uuid import uuid4
from Entities.Room import Room


class SingleRoom(Room):

    def __init__(self, count: int, price: int, capacity: int):
        super().__init__(count, price, capacity)
        self.id = str(uuid4())

    def book_room(self, start: int, end: int, book_for_days: int):
        return self.calendar.book_slot(start, end, book_for_days)
    
    def get_availability(self, start_date: int, end_date: int):
        return self.calendar.get_availability(start_date, end_date)
    
    def describe_room(self):
        return f"Single Room - ID: {self.id}, Price: {self.price}, Capacity: {self.capacity}"


class DoubleRoom(Room):

    def __init__(self, count: int, price: int, capacity: int):
        super().__init__(count, price, capacity)
        self.id = str(uuid4())

    def book_room(self, start: int, end: int, no_of_rooms: int):
        return self.calendar.book_slot(start, end, no_of_rooms)
    
    def get_availability(self, start_date: int, end_date: int):
        return self.calendar.get_availability(start_date, end_date)
    
    def describe_room(self):
        return f"Double Room - ID: {self.id}, Price: {self.price}, Capacity: {self.capacity}"


class Suite(Room):

    def __init__(self, count: int, price: int, capacity: int):
        super().__init__(count, price, capacity)
        self.id = str(uuid4())

    def book_room(self, start: int, end: int, book_for_days: int):
        return self.calendar.book_slot(start, end, book_for_days)
    
    def get_availability(self, start_date: int, end_date: int):
        return self.calendar.get_availability(start_date, end_date)
    
    def describe_room(self):
        return f"Suite - ID: {self.id}, Price: {self.price}, Capacity: {self.capacity}"