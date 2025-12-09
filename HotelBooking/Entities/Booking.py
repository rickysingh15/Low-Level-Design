from uuid import uuid4
from Entities.User import User
from Entities.Hotel import Hotel
from Entities.Period import Period
from Entities.Room import Room

class Booking:

    def __init__(self, user: User, room: Room, hotel: Hotel, period: Period):
        self.id = str(uuid4())
        self.user = user
        self.hotel = hotel
        self.period = period
        self.room = room

    def describe_booking(self):
        return f"Hotel Name: {self.hotel.name}, user: {self.user.name}, room: {self.room} , period: {self.period.start} to {self.period.end}"