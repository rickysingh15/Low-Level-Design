
from abc import ABC, abstractmethod
class ServeStrategy(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def serve(self):
        pass