
from abc import ABC, abstractmethod

class Subject(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def add_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify(self):
        pass