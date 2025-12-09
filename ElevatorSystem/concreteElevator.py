
from elevator import Elevator
from serveStrategy import ServeStrategy
from direction import Direction
from constants import Directions
from concreteStates import IdleState
from request import Request
from subject import Subject
from observer import Observer
from typing import Set
from floor import Floor
import time

class NormalElevator(Elevator, Subject):

    def __init__(self, strategy: ServeStrategy, elevator_service, requests: list[Request] = None, observers: list[Observer] = None):
        super().__init__()
        self.strategy = strategy
        self.elevator_service = elevator_service
        self.direction = Directions.IDLE.value
        self.current_floor = Floor(0, self.elevator_service)
        self.state = IdleState(self.elevator_service)
        self.is_running = True
        self.upRequests = set()
        self.downRequests = set()
        self.observers = observers
        print("Normal Elevator created ", self, " with elevator service:", self.elevator_service)

    def change_state(self, state):
        print("Changing state from ", self.state , " -------> ", state)
        self.state = state

    def get_up_requests(self):
        return self.upRequests
    
    def get_down_requests(self):
        return self.downRequests
    
    def set_current_floor(self, floor: Floor):
        self.current_floor = floor
    
    def get_current_floor(self):
        return self.current_floor
    
    def select_floor(self, floor_num: int):
        self.add_request(floor_num)

    def add_request(self, floor_num: int):
        print("Current state of elevator is ", self.state)
        print("Adding request to elevator for floor ", floor_num)
        request = Request(Floor(floor_num, self.elevator_service), self)
        self.state.add_request(request, self)

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        for obs in self.observers:
            if obs == observer:
                self.observers.remove(obs)
                break

    def notify(self):
        for obs in self.observers:
            obs.update()


    def run(self):
        print("About to run with elevator ", self)
        while self.is_running:
            try:
                self.state.move(self)
                time.sleep(1)
            except Exception as e:
                self.is_running = False
                break


class ExpressElevator(Elevator, Subject):

    def __init__(self, strategy: ServeStrategy, elevator_service , requests: list[Request] = None, observers: list[Observer] = None):
        super().__init__()
        self.strategy = strategy
        self.elevator_service = elevator_service
        self.direction = Directions.IDLE.value
        self.current_floor = Floor(0, self.elevator_service)
        self.state = IdleState(elevator_service)
        self.is_running = True
        self.upRequests = set()
        self.downRequests = set()
        self.observers = observers
        print("Express Elevator created ", self, " with elevator service:", self.elevator_service)

    def change_state(self, state):
        print("Changing state from ", self.state , " -------> ", state)
        self.state = state

    def get_up_requests(self):
        return self.upRequests
    
    def get_down_requests(self):
        return self.downRequests
    
    def get_current_floor(self):
        return self.current_floor
    
    def set_current_floor(self, floor: Floor):
        self.current_floor = floor

    def add_request(self, floor_num: int):
        request = Request(Floor(floor_num, self.elevator_service), self)
        self.state.add_request(request, self)

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        for obs in self.observers:
            if obs == observer:
                self.observers.remove(obs)
                break

    def notify(self):
        for obs in self.observers:
            obs.update()

    def run(self):
        print("About to run with elevator ", self)
        while self.is_running:
            try:
                self.state.move(self)
                time.sleep(1)
            except Exception as e:
                self.is_running = False
                break


class ServiceElevator(Elevator, Subject):

    def __init__(self, strategy: ServeStrategy, elevator_service , requests: list[Request] = None, observers: list[Observer] = None):
        super().__init__()
        self.strategy = strategy
        self.elevator_service = elevator_service
        self.direction = Directions.IDLE.value
        self.current_floor = Floor(0, self.elevator_service)
        self.state = IdleState(self.elevator_service)
        self.is_running = True
        self.upRequests = set()
        self.downRequests = set()
        self.observers = observers
        print("Service Elevator created ", self, " with elevator service:", self.elevator_service)

    def change_state(self, state):
        print("Changing state from ", self.state , " -------> ", state)
        self.state = state

    def get_up_requests(self):
        return self.upRequests
    
    def get_down_requests(self):
        return self.downRequests
    
    def get_current_floor(self):
        return self.current_floor
    
    def set_current_floor(self, floor: Floor):
        self.current_floor = floor

    def add_request(self, floor_num: int):
        request = Request(Floor(floor_num, self.elevator_service), self)
        self.state.add_request(request, self)

    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        for obs in self.observers:
            if obs == observer:
                self.observers.remove(obs)
                break

    def notify(self):
        for obs in self.observers:
            obs.update()


    def run(self):
        print("About to run with elevator ", self)
        while self.is_running:
            try:
                self.state.move(self)
                time.sleep(1)
            except Exception as e:
                self.is_running = False
                break