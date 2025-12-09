
from abc import ABC, abstractmethod
from topic import Topic

class Subscriber(ABC):

    def __init__(self, topic: list[Topic] = None):
        self.topics = topic or []

    @abstractmethod
    def subscribe(self, topic: Topic):
        pass

    @abstractmethod
    def pull_message_from_topic(self, topic: Topic):
        pass
    
    @abstractmethod
    def pull_all_messages(self):
        pass