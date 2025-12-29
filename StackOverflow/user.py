
from uuid import uuid4
import threading
from observer import Observer

class User(Observer):

    def __init__(self, name: str, email: str):
        self._id = str(uuid4())
        self._name = name
        self._email = email
        self._score = 0
        self._contributions = 0
        self._votes = 0
        self.lock = threading.Lock()

    def update(self):
        print("user ", self._name ," received notification")

    @property
    def get_id(self):
        return self._id
    
    @property
    def get_name(self):
        return self._name
    
    @property
    def get_email(self):
        return self._email
    
    @property
    def get_score(self):
        print("user name ", self._name)
        print("user votes ", self._votes)
        return self._score

    def add_vote(self):
        with self.lock:
            self._votes += 1
            print("new votes are ", self._votes)
            self.update_score()

    def dec_vote(self):
        with self.lock:
            self._votes -= 1
            print("new votes are ", self._votes)
            self.update_score()
            

    def get_votes(self):
        with self.lock:
            return self._votes

    def add_contribution(self):
        with self.lock:
            self._contributions += 1
            print("new contributions are ", self._contributions)
            self.update_score()
            

    def get_contributions(self):
        with self.lock:
            return self._contributions

    def update_score(self):
        self._score = self._votes + self._contributions

    def get_score(self):
        with self.lock:
            return self._score