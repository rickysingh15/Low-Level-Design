from abc import ABC, abstractmethod
from vehicle import Vehicle
from concrete.vehicles import Car, Bike, Truck

class VehicleFactory:

    def __init__(self):
        pass

    @abstractmethod
    def create_vehicle(self, passenger_name: str, number: str) -> Vehicle:
        pass


class CarFactory(VehicleFactory):

    def __init__(self):
        pass

    def create_vehicle(self, passenger_name: str, number: str):
        return Car(passenger_name, number)


class BikeFactory(VehicleFactory):

    def __init__(self):
        pass

    def create_vehicle(self, passenger_name: str, number: str):
        return Bike(passenger_name, number)


class TruckFactory(VehicleFactory):

    def __init__(self):
        pass

    def create_vehicle(self, passenger_name: str, number: str):
        return Truck(passenger_name, number)