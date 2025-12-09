
from abc import ABC, abstractmethod

class State(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def add_request(self):
        pass
    