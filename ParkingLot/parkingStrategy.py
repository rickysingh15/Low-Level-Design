from abc import ABC, abstractmethod
from floor import Floor

class ParkingStrategy(ABC):

    def __init__(self):
        pass
    
    @abstractmethod
    def find_spot(self):
        pass


class CarParkStrategy(ParkingStrategy):

    def __init__(self):
        pass

    def find_spot(self, floors: list[Floor]):
        for floor in floors:
            for spot in floor.regular_spots:
                if spot.is_empty():
                    return spot

        for floor in floors: 
            for spot in floor.oversize_spots:
                if spot.is_empty():
                    return spot
            
        return None


class BikeParkStrategy(ParkingStrategy):

    def __init__(self):
        pass

    def find_spot(self, floors: list[Floor]):
        for floor in floors:
            for spot in floor.compact_spots:
                if spot.is_empty():
                    return spot
        return None

class TruckParkStrategy(ParkingStrategy):

    def __init__(self):
        pass

    def find_spot(self, floors: list[Floor]):
        for floor in floors:
            for spot in floor.oversize_spots:
                if spot.is_empty():
                    return spot
        return None