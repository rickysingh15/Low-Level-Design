
import threading
from elevator import Elevator
from elevatorFactory import NormalElevatorFactory, ExpressElevatorFactory, ServiceElevatorFactory
from serveStrategy import ServeStrategy
from concreteServeStrategy import ScanServeStrategy, FcfsServeStrategy, LookServeStrategy
from observer import Observer
from request import Request
from executorService import ExecutorService
import time


class ElevatorService:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, no_of_normal_elevators: int, no_of_express_elevators: int, no_of_service_elevators: int):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.executor_service = ExecutorService()
            self.elevators = {
                "normal": [],
                "express": [],
                "service": []
            }

            for i in range(no_of_normal_elevators):
                elevator = self.get_elevator_factory("normal").create_elevator(self, FcfsServeStrategy())
                self.elevators["normal"].append(elevator)

            # for i in range(no_of_express_elevators):
            #     elevator = self.get_elevator_factory("express").create_elevator(self, FcfsServeStrategy())
            #     self.elevators["express"].append(elevator)

            # for i in range(no_of_service_elevators):
            #     elevator = self.get_elevator_factory("service").create_elevator(self, FcfsServeStrategy())
            #     self.elevators["service"].append(elevator)

    def start_all_elevators(self):
        for elevator_type, lis in self.elevators.items():
            for elevator in lis:
                self.executor_service.start_on_thread(elevator, elevator.run)

        # for elevator_type, lis in self.elevators.items():
        #     for elevator in lis:
        #         self.executor_service.futures

    def stop_all_elevators(self):
        print("Waiting before cancelling all elevators")
        time.sleep(50)
        print("cancelling elevators")
        for elevator, future in self.executor_service.futures.items():
            elevator.is_running = False
            future.cancel()

    def request_elevator(self, dest_floor: int, elevator_type: str):
        elevator = self.get_elevator(elevator_type)
        elevator.add_request(dest_floor)

    def get_elevator(self, type: str):
        elevator = self.elevators[type][0]
        return elevator

    def register_observer_to_elevators(self, observer: Observer):
        for elevator_type, elevators in self.elevators.items():
            for elevator in elevators:
                elevator.add_observer(observer)

    def unregister_observer_to_elevators(self, observer: Observer):
        for elevator_type, elevators in self.elevators.items():
            for elevator in elevators:
                elevator.remove_observer(observer)

    def get_elevator_factory(self, factory_type: str):

        factory = None
        if factory_type.lower() == "normal":
            return NormalElevatorFactory()
        elif factory_type.lower() == "express":
            return ExpressElevatorFactory()
        elif factory_type.lower() == "service":
            return ServiceElevatorFactory()
        else:
            print("Invalid elevator type")
        return factory

    def create_elevator(self, type: str, serve_strategy: ServeStrategy):
        factory = self.get_elevator_factory(type)
        elevator = factory.create_elevator(serve_strategy)
        