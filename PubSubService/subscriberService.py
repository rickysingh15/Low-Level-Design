
import threading 
from actor import SubActor
from topic import Topic

class SubscriberService:

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.subscribers = []

    def create_subscriber(self):
        subscriber = SubActor()
        return subscriber
    
    def subscribe(self, actor: SubActor, topic: Topic):
        actor.subscribe(topic)
