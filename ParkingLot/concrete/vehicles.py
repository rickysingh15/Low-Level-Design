from vehicle import Vehicle
from parkingStrategy import CarParkStrategy, BikeParkStrategy, TruckParkStrategy

class Car(Vehicle):
    def __init__(self, passenger_name, number):
        super().__init__(passenger_name, number, "car")
        self.parking_strategy = CarParkStrategy()


class Bike(Vehicle):
    def __init__(self, passenger_name, number):
        super().__init__(passenger_name, number, "bike")
        self.parking_strategy = BikeParkStrategy()


class Truck(Vehicle):
    def __init__(self, passenger_name, number):
        super().__init__(passenger_name, number, "truck")
        self.parking_strategy = TruckParkStrategy()