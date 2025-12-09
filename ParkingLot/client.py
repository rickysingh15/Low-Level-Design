from parkingLot import ParkingLot
from concrete.vehicles import Car, Bike, Truck

floors = 1
compact_spots_per_floor = 5
regular_spots_per_floor = 3
oversize_spots_per_floor =  1
rate_of_compact_spot_per_min = 1
rate_of_regular_spot_per_min = 3
rate_of_oversize_spot_per_min = 5


parking_lot = ParkingLot(floors, compact_spots_per_floor, regular_spots_per_floor, oversize_spots_per_floor, rate_of_compact_spot_per_min,
                         rate_of_regular_spot_per_min, rate_of_oversize_spot_per_min)

ticket1 = parking_lot.park_vehicle("Tushar", "up14es5662", "car")
ticket1.print_ticket()

ticket2 = parking_lot.park_vehicle("Ann", "up16et5212", "car")
ticket2.print_ticket()

ticket3 = parking_lot.park_vehicle("dikesh", "up16io4562", "car")
ticket3.print_ticket()

parking_lot.unpark_vehicle(ticket1, "cash")

ticket4 = parking_lot.park_vehicle("shubham", "up32er6565", "car")
ticket4.print_ticket()

