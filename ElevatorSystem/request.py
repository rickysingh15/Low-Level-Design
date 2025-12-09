
from floor import Floor
from elevator import Elevator

class Request:

    def __init__(self, destination_floor: Floor, elevator: Elevator = None):
        self.destination_floor = destination_floor
        self.elevator = elevator

        