
import threading
from actor import PubActor

class PublisherService:

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
            self.publishers = []

    def create_publisher(self):
        actor = PubActor()
        self.publishers.append(actor)
        return actor