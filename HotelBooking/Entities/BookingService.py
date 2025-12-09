from Entities.Hotel import Hotel
from Entities.Booking import Booking
from Entities.User import User
from Entities.Period import Period
from Entities.Rating import Rating
from Entities.Room import Room

class BookingService:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.bookings = dict()

    def add_booking(self, booking: Booking, start: int, end: int, persons: int):
        self.bookings[booking.id] = booking
        booking.room.book_room(start, end,  int(persons/booking.room.capacity)) 
        return booking.id
    

    def book(self, hotel: Hotel, room: Room, user: User , start: int, end: int, persons: int):

        print("Booking requrest recieved")
        period = Period(start, end)

        status, min_booking = room.get_availability(start, end)
        print("min booking is ", min_booking)
        if not status:
            print("Room not avalaiable for dates")

        if min_booking * room.capacity < persons:
            print("Not enough rooms for ", persons, " persons")
            return None
        
        booking = Booking(user, room, hotel, period)
        self.add_booking(booking, start, end, persons)
        return booking
    
    def rate_hotel(self, booking: Booking, rating: float, comment: str = ""):
        hotel = booking.hotel
        hotel.add_rating(Rating(booking.user, rating, comment))