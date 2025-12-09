from Entities.UserService import UserService
from Entities.HotelService import HotelService
from Entities.BookingService import BookingService
from Entities.Booking import Booking
from Entities.Hotel import Hotel
from Entities.Room import Room

class BookingPlatform:

    def __init__(self):
        self.user_service = UserService()
        self.hotel_service = HotelService()
        self.booking_service = BookingService()
        self.logged_in_user = None

    def get_user_service(self) -> UserService:
        return self.user_service
    
    def get_hotel_service(self) -> HotelService:
        return self.hotel_service
    
    def get_booking_service(self) -> BookingService:
        return self.booking_service

    def register_user(self, name: str, email: str, phone: str, location_name: str, pincode: str):

        if self.logged_in_user is not None:
            print("User already logged in, log out to register new user")
            return None

        return self.user_service.register_user(name, email, phone, location_name, pincode)
    
    def register_hotel(self, name: str, location_name: str, pincode: str):
        if self.logged_in_user is None:
            print("User not logged in")
            return None
        return self.hotel_service.register_hotel(name, location_name, pincode, self.logged_in_user)

    def add_room_to_hotel(self, hotel_name: str, type: str, count: int, price: int, capacity: int):
        if self.logged_in_user is None:
            print("User not logged in")
            return False
        
        return self.hotel_service.add_room_to_hotel(hotel_name, type, count, price, capacity)
        
    
    def login_user(self, phone: str):
        user = self.user_service.login_user(phone)
        if user is None:
            return False
        
        self.logged_in_user = user
        return True
    
    def get_available_hotels(self, start_date: int, end_date: int, persons: int, location_name: str, pincode: str):

        if self.logged_in_user is None:
            print("User not logged in")
            return []

        return self.hotel_service.get_available_hotels(start_date, end_date, persons, location_name, pincode)
    
    def get_available_rooms(self, hotel_name: str, start: int, end: int):
        if self.logged_in_user is None:
            print("User not logged in")
            return []
        
        hotel = self.hotel_service.get_hotel(hotel_name)
        if hotel is None:
            print("Hotel not found")
            return None

        return hotel.get_available_rooms(start, end) 
    

    def book_hotel(self, hotel_name: str, room_type: str, start_date: int, end_date: int, persons: int):
        
        if self.logged_in_user is None:
            print("User not logged in")
            return None
        
        if self.hotel_service.get_hotel(hotel_name) is None:
            print("Hotel not found")
            return None
        
        hotel = self.hotel_service.get_hotel(hotel_name)
        room = hotel.get_room(room_type)
        if room is None:
            print("Room not found")
            return None
        booking = self.booking_service.book(hotel, room, self.logged_in_user, start_date, end_date, persons)
        return booking
        
    def rate_hotel(self, booking: Booking, rating_value: float, comment: str):
        if self.logged_in_user is None:
            print("User not logged in")
            return False
        
        self.booking_service.rate_hotel(booking, rating_value, comment)
        return True
        
        