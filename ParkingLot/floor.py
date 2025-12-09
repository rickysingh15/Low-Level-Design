
from uuid import uuid4
from concrete.spots import Compact, Regular, Oversize

class Floor:

    def __init__(self, compact_spots_per_floor: int, rate_of_compact_spot_per_min: int, 
                    regular_spots_per_floor: int, rate_of_regular_spot_per_min: int, 
                    oversize_spots_per_floor: int, rate_of_oversize_spot_per_min: int,
                    compact_spots: list[Compact] = None, regular_spots: list[Regular] = None, oversize_spots: list[Oversize] = None):
        self.id = str(uuid4())
        self.compact_spots = compact_spots or []
        self.regular_spots = regular_spots or []
        self.oversize_spots = oversize_spots or []

        for i in range(compact_spots_per_floor):
            compact_spot = Compact(rate_of_compact_spot_per_min)
            self.compact_spots.append(compact_spot)

        for i in range(regular_spots_per_floor):
            regular_spot = Regular(rate_of_regular_spot_per_min)
            print("rate of regular spot is ", rate_of_regular_spot_per_min)
            self.regular_spots.append(regular_spot)

        for i in range(oversize_spots_per_floor):
            oversize_spot = Oversize(rate_of_oversize_spot_per_min)
            self.oversize_spots.append(oversize_spot) 


