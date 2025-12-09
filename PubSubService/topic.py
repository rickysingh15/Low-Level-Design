
from uuid import uuid4
from collections import deque
from subject import Subject
from observer import Observer

class Topic(Subject):

    def __init__(self):
        super().__init__()
        self.id = str(uuid4())
        self.messages = deque()

    def put_message(self, message):
        print("Message pushed to topic ", self)
        self.messages.appendleft(message)
        self.notify()
    
    def get_message(self):
        if len(self.messages) == 0:
            return None 
        return self.messages[0]
    
    def add_observer(self, observer: Observer):
        self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        for obs in self.observers:
            if obs == observer:
                self.observers.remove(obs)

    def notify(self):
        print("Sending notification to all observers of topic ", self)
        for obs in self.observers:
            obs.update()