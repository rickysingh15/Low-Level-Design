from Entities.Location import Location
from Entities.Hotel import Hotel
from Entities.User import User

class HotelService:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.hotels = dict()

    def register_hotel(self, name: str, location_name: str, pincode: str, owner: User):
        location = Location(location_name, pincode)
        hotel = Hotel(name, location, owner)

        if name not in self.hotels:
            print("Name not in hotels")
            self.hotels[name] = None

        self.hotels[name] = hotel

        print("Hotel registered successfully")
        return hotel
    
    def get_hotel(self, name: str):
        if name in self.hotels:
            return self.hotels[name]
        return None
    
    def add_room_to_hotel(self, hotel_name: str, type: str, count: int, price: int, capacity: int):
        if hotel_name not in self.hotels:
            print("Hotel not found")
            return False
        hotel = self.hotels[hotel_name]
        return hotel.add_room(type, count, price, capacity)
    
    def get_available_hotels(self, start_date: int, end_date: int, persons: int, location_name: str, pincode: str):
        available_hotels = dict()
        for hotel_name, hotel in self.hotels.items():
            print("---Checking availability for hotel:", hotel_name)
            if hotel.location.name == location_name and hotel.location.pincode == pincode and hotel.is_available(start_date, end_date, persons):
                print("---Hotel available:", hotel_name)
                if hotel_name not in available_hotels:
                    available_hotels[hotel_name] = dict()
                available_hotels[hotel_name] = hotel
        return available_hotels