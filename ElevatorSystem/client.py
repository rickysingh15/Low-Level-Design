
from elevatorService import ElevatorService
from building import Building



building = Building(1,1,1,10)
building.start_elevator_service()

building.call_elevator(5, "normal")
building.call_elevator(3, "normal")


building.stop_elevator_service()