
from abc import ABC, abstractmethod
from publisher import Publisher
from subscriber import Subscriber
from topic import Topic
from observer import Observer

class Actor(ABC):

    def __init__(self):
        pass


class PubActor(Publisher):

    def __init__(self):
        pass

    def publish(self, message: str, topic: Topic):
        topic.put_message(message)


class SubActor(Subscriber, Observer):

    def __init__(self):
        super().__init__()

    def subscribe(self, topic: Topic):
        topic.add_observer(self)
        self.topics.append(topic)
        return True
    
    def update(self):
        print("Notification received to subscriber ", self)
        return self.pull_all_messages()
        
    def pull_message_from_topic(self, topic: Topic):
        req_topic = None
        for t in self.topics:
            if t.id == topic.id:
                req_topic = t
        return req_topic.get_message()
    
    def pull_all_messages(self):
        all_messages = []
        for t in self.topics:
            all_messages.append(t.get_message())

        print("Messages pulled are ", all_messages)
        return all_messages
    