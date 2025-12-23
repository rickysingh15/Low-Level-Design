
from uuid import uuid4
import threading
class Ingredient:

    def __init__(self, name: str, count: int):
        self.id = str(uuid4())
        self.name = name
        self.count = count
        self.lock = threading.Lock()

    def get_count(self):
        return self.count

    def decrement_count(self, count: int):
        with self.lock:
            self.count -= count

    def update_count(self, count: int):
        with self.lock:
            self.count = count

    def describe(self):
        print("name is ", self.name)
        print("count is ", self.count)
