
from state import State
from elevator import Elevator
from request import Request
from floor import Floor

class IdleState(State):

    def __init__(self, elevator_service):
        self.elevator_service = elevator_service

    def move(self, elevator: Elevator):
        print("Moving")
        if elevator.is_running:
            if elevator.get_up_requests():
                elevator.change_state(MovingUpState(self.elevator_service))
            elif elevator.get_down_requests():
                elevator.change_state(MovingDownState(self.elevator_service))

    def add_request(self, request: Request, elevator: Elevator):
        current_floor = elevator.get_current_floor()
        print("current floor is ", current_floor.number)

        if current_floor.number > request.destination_floor.number:
            elevator.downRequests.add(request.destination_floor.number)
        elif current_floor.number < request.destination_floor.number:
            elevator.upRequests.add(request.destination_floor.number)
        else:
            print("Doors open")


class MovingUpState(State):

    def __init__(self, elevator_service):
        self.elevator_service = elevator_service

    def move(self, elevator: Elevator):
        if elevator.is_running:
            print("Moving")
            if not elevator.get_up_requests():
                elevator.change_state(IdleState(self.elevator_service))

            next_destination = min(elevator.get_up_requests())
            print("next destination is ", next_destination)
            current = elevator.get_current_floor()
            print("current floor is ", current.number)
            if current is not None and current.number == next_destination:
                print("Request fulfilled")
                elevator.upRequests.remove(current.number)
            else:
                number = current.number
                elevator.set_current_floor(Floor(number+1, self.elevator_service))

            if not elevator.get_up_requests():
                elevator.change_state(IdleState(self.elevator_service))

    def add_request(self, request: Request, elevator: Elevator):
        current_floor = elevator.get_current_floor()

        if current_floor.number > request.destination_floor.number:
            elevator.downRequests.add(request.destination_floor.number)
        elif current_floor.number < request.destination_floor.number:
            elevator.upRequests.add(request.destination_floor.number)
        else:
            print("Doors open")

class MovingDownState(State):

    def __init__(self, elevator_service):
        self.elevator_service = elevator_service

    def move(self, elevator: Elevator):
        if elevator.is_running:
            print("Moving")
            if not elevator.get_down_requests():
                elevator.change_state(IdleState(self.elevator_service))

            next_destination = max(elevator.get_down_requests())
            print("next destination is ", next_destination)
            current = elevator.get_current_floor()
            print("current floor is ", current.number)
            if current is not None and current.number == next_destination:
                print("Request fulfilled")
                elevator.downRequests.remove(current.number)
            else:
                number = current.number
                elevator.set_current_floor(Floor(number-1, self.elevator_service))

            if not elevator.get_down_requests():
                elevator.change_state(IdleState(self.elevator_service))

    def add_request(self, request: Request, elevator: Elevator):
        current_floor = elevator.get_current_floor()

        if current_floor.number > request.destination_floor.number:
            elevator.downRequests.add(request.destination_floor.number)
        elif current_floor.number < request.destination_floor.number:
            elevator.upRequests.add(request.destination_floor.number)
        else:
            print("Doors open")

