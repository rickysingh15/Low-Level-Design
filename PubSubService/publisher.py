
from abc import ABC, abstractmethod
from topic import Topic

class Publisher(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def publish(self, message: str, topic: Topic):
        pass