
from abc import ABC, abstractmethod

class Subject(ABC):

    def __init__(self):
        super().__init__()
        
    @abstractmethod
    def notify(self):
        pass