import threading
from floor import Floor
from spot import Spot
from vehicle import Vehicle
from concrete.vehicles import Car, Bike, Truck
class SpotManager:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, no_of_floors: int, compact_spots_per_floor: int, rate_of_compact_spot_per_min: int, 
                        regular_spots_per_floor: int, rate_of_regular_spot_per_min: int, 
                        oversize_spots_per_floor: int, rate_of_oversize_spot_per_min: int, floors: list[Floor] = None):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.no_of_floors = no_of_floors
            self.compact_spots_per_floor = compact_spots_per_floor
            self.rate_of_compact_spot_per_min = rate_of_compact_spot_per_min
            self.regular_spots_per_floor = regular_spots_per_floor
            self.rate_of_regular_spot_per_min = rate_of_regular_spot_per_min
            self.oversize_spots_per_floor = oversize_spots_per_floor
            self.rate_of_oversize_spot_per_min = rate_of_oversize_spot_per_min
            self.floors = floors or []
            self.reserve_lock = threading.Lock()


            for i in range(no_of_floors):
                floor = Floor(self.compact_spots_per_floor, self.rate_of_compact_spot_per_min, 
                            self.regular_spots_per_floor, self.rate_of_regular_spot_per_min, 
                            self.oversize_spots_per_floor, self.rate_of_oversize_spot_per_min)
                self.floors.append(floor)
    
    def find_and_reserve(self, vehicle):
        with self.reserve_lock:
            spot = vehicle.parking_strategy.find_spot(self.floors)
            if spot is None:
                print("No Spots available")
                return None
            self.reserve_spot(spot, vehicle)
            return spot
        
    def reserve_spot(self, spot: Spot, vehicle: Vehicle):
        spot.reserve(vehicle)

    def free_spot(self, spot):
        spot.free()
        