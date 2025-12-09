
from abc import ABC, abstractmethod
from uuid import uuid4

class Elevator(ABC):

    def __init__(self):
        self.id = str(uuid4())

    def get_id(self):
        return self.id
    
    @abstractmethod
    def add_request(self):
        pass

    @abstractmethod
    def run(self):
        pass