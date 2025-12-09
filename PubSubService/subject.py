
from abc import ABC, abstractmethod
from observer import Observer

class Subject(ABC):

    def __init__(self, observers: list[Observer] = None):
        self.observers = observers or []

    @abstractmethod
    def add_observer(self):
        pass    

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify(self):
        pass