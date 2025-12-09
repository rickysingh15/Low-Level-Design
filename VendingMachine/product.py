
import threading
from uuid import uuid4

class Product:

    def __init__(self, name: str, inventory_count: int, price: int):
        self.id = str(uuid4())
        self.name = name
        self.count = inventory_count
        self.price = price
        self.lock = threading.Lock()

    def update_count(self, incremented_by: int, decremented_by: int):
        with self.lock:
            self.count = self.count + (incremented_by-decremented_by)

    def update_price(self, new_price: int):
        with self.lock:
            self.price = new_price