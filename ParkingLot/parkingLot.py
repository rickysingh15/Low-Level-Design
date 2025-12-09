from parkingManager import ParkingManager
from paymentManager import PaymentManager
from spotManager import SpotManager
from ticket import Ticket
from vehicle import Vehicle
from vehicleFactory import CarFactory, BikeFactory, TruckFactory
class ParkingLot:


    def get_factory(self, type: str):
        type = type.lower()
        if type == "car":
            factory = CarFactory()
        elif type == "bike":
            factory = BikeFactory()
        elif type == "truck":
            factory = TruckFactory()
        else:
            print("Invalid vehicle type")
        return factory

    def __init__(self, floors: int, compact_spots_per_floor: int, regular_spots_per_floor: int, oversize_spots_per_floor: int,
                 rate_of_compact_spot_per_min: int, rate_of_regular_spot_per_min: int, rate_of_oversize_spot_per_min: int):
        self.compact_spots_per_floor = compact_spots_per_floor
        self.regular_spots_per_floor = regular_spots_per_floor
        self.oversize_spots_per_floor = oversize_spots_per_floor
        self.rate_of_compact_spot_per_hour = rate_of_compact_spot_per_min
        self.rate_of_regular_spot_per_hour = rate_of_regular_spot_per_min
        self.rate_of_oversize_spot_per_hour = rate_of_oversize_spot_per_min
        self.floors = floors
        self.parking_manager = ParkingManager()
        self.payment_manager = PaymentManager()
        self.spot_manager = SpotManager(floors, compact_spots_per_floor, rate_of_compact_spot_per_min, 
                                        regular_spots_per_floor, rate_of_regular_spot_per_min, 
                                        oversize_spots_per_floor, rate_of_oversize_spot_per_min)
        
    def park_vehicle(self, passenger_name: str, vehicle_number: str, type: str) -> Ticket:
        
        factory = self.get_factory(type)
        vehicle = factory.create_vehicle(passenger_name, vehicle_number)
        spot = self.spot_manager.find_and_reserve(vehicle)
        ticket = self.parking_manager.create_ticket(vehicle, spot)
        return ticket

    def unpark_vehicle(self, ticket: Ticket, payment_type: str):
        ticket = self.parking_manager.process_ticket(ticket)
        self.spot_manager.free_spot(ticket.spot)
        self.payment_manager.process_payment(ticket, payment_type)
        return True