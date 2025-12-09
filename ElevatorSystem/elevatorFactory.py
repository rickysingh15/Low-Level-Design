
from abc import ABC, abstractmethod
from concreteElevator import NormalElevator, ExpressElevator, ServiceElevator
from serveStrategy import ServeStrategy

class ElevatorFactory:

    def __init__(self):
        pass

    @abstractmethod
    def create_elevator(self, elevator_service, service_strategy: ServeStrategy):
        pass


class NormalElevatorFactory(ElevatorFactory):
    def __init__(self):
        pass

    def create_elevator(self, elevator_service, serve_strategy: ServeStrategy):
        return NormalElevator( serve_strategy, elevator_service)


class ExpressElevatorFactory(ElevatorFactory):
    def __init__(self):
        pass

    def create_elevator(self, elevator_service, serve_strategy: ServeStrategy):
        return ExpressElevator(serve_strategy, elevator_service)


class ServiceElevatorFactory(ElevatorFactory):
    def __init__(self):
        pass

    def create_elevator(self, elevator_service, serve_strategy: ServeStrategy):
        return ServiceElevator(serve_strategy, elevator_service)