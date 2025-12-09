
import threading
from topic import Topic

class TopicService:

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
            self.topics = dict()

    def get_topic(self, topic: Topic):
        return self.topics.get(topic.id, None)
    
    def put_topic(self, topic: Topic):
        if topic.id in self.topics:
            print("Topic already present")
            return False
        self.topics[topic.id] = topic
        return True
    
    def create_topic(self):
        topic = Topic()
        self.put_topic(topic)
        return topic