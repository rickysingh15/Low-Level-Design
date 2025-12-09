from abc import ABC, abstractmethod
from uuid import uuid4
from vehicle import Vehicle

class Spot:
    def __init__(self, rate_per_min: int, vehicle: Vehicle = None):
        self.id = str(uuid4())
        self.vehicle = vehicle
        self.rate = rate_per_min

    def reserve(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def free(self):
        self.vehicle = None

    def describe(self):
        print("spot id is ", self.id)
        print("spot vehicle is ", self.vehicle)
        print("rate is ", self.rate)