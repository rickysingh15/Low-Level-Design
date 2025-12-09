from abc import ABC, abstractmethod
from uuid import uuid4

class Vehicle:
    def __init__(self, passenger_name: str, number: int, type: str):
        self.id = str(uuid4())
        self.passenger_name = passenger_name
        self.number = number
        self.type = type
        
    def describe(self):
        print(" vehicle id is ", self.id)
        print(" passenger name is ", self.passenger_name)
        print(" vehicle number is ", self.number)