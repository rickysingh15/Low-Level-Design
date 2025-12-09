from Entities.Location import Location
from Entities.User import User
from Entities.ConcreteRoom import SingleRoom, DoubleRoom, Suite
from Entities.Rating import Rating

class Hotel:

    def __init__(self, name: str, location: Location, owner: User):
        self.name = name
        self.location = location
        self.rooms = dict()
        self.owner = owner
        self.rating = 0.0
        self.ratings = list()

    def add_room(self, type: str, count: int, price: int, capacity: int):
        if type == "single":
            room = SingleRoom(count, price, capacity)
        elif type == "double":
            room = DoubleRoom(count, price, capacity)
        elif type == "suite":
            room = Suite(count, price, capacity)
        else:
            print("Invalid room type")
            return False
        self.rooms[type] = room
        return True
    
    def update_room(self, type: str, count: int = None, price: int = None, capacity: int = None):
        
        if self.rooms.get(type, None) is None:
            print("Invalid room type or room type does not exist in hotel")
            return False
        
        room = self.rooms.get(type)
        if count is not None:
            room.count = count

        if price is not None:
            room.price = price

        if capacity is not None:
            room.capacity = price

        self.rooms[type] = room
        return True
    
    def get_room(self, room_type: str):
        
        room = self.rooms.get(room_type, None)
        if room is None:
            print("Invalid room type or room type not present in hotel")
            return None
        
        return room
    
    def add_rating(self, rating: Rating):
        self.ratings.append(rating)
        total = 0.0
        for rating_obj in self.ratings:
            total += rating_obj.rating
        self.rating = total / len(self.ratings) if self.ratings else 0.0

    # def is_available(self, start_date: int, end_date: int, persons: int):

    #     print("----Checking room capacity")
    #     total_capacity = 0
    #     for room_type, rooms in self.rooms.items():
    #         for room in rooms:
    #             print(" room is ", room.describe_room())
    #             status, rooms_left = room.get_availability(start_date, end_date)
    #             if status:
    #                 total_capacity += (room.capacity * rooms_left)
    #                 print("-----total_capacity is ", total_capacity)
    #             if total_capacity >= persons:
    #                 print("------Sufficient capacity")
    #                 return True
    #     return False
    

    def is_available(self, start_date: int, end_date: int, persons: int):
        total_capacity = 0
        for room_type, room in self.rooms.items():
            status, max_allowed_booking = room.get_availability(start_date, end_date)
            if status:
                total_capacity += (max_allowed_booking * room.capacity)
                if total_capacity >= persons:
                    return True
        return False
    
    def get_available_rooms(self, start_date: int, end_date: int):
        available_rooms = dict()
        for room_type, room in self.rooms.items():
            status, max_allowed_booking = room.get_availability(start_date, end_date)
            if status:
                available_rooms[room_type] = room
        return available_rooms


    def describe_hotel(self):
        return f"Hotel Name: {self.name}, Location: {self.location.name}, Pincode: {self.location.pincode}, Owner: {self.owner.name}"
