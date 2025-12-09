
from abc import ABC, abstractmethod

class Handler(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def set_next(self):
        pass
    
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def can_handle(self):
        pass
    
    @abstractmethod
    def handle(self):
        pass