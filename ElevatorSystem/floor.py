
class Floor():

    def __init__(self, number: int, elevator_service):
        self.number = number
        self.elevator_service = elevator_service

    def call_elevator(self, type: str):
        elevator = self.elevator_service.get_elevator(type)
        elevator.add_request(self.number)
