
import threading 
from floor import Floor
from elevatorService import ElevatorService
class Building:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, num_of_normal_elevators: int, num_of_express_elevators: int, num_of_service_elevators: int, num_of_floors: int, floors: list[Floor] = None):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.floors = floors or []
            self.num_of_floors = num_of_floors
            self.elevator_service = ElevatorService(num_of_normal_elevators, num_of_express_elevators, num_of_service_elevators)
            for i in range(self.num_of_floors):
                floor = Floor(i, self.elevator_service)
                self.floors.append(floor)

    def call_elevator(self, floor: int, type: str):
        self.elevator_service.request_elevator(floor, type)

    def start_elevator_service(self):
        self.elevator_service.start_all_elevators()


    def stop_elevator_service(self):
        self.elevator_service.stop_all_elevators()

        