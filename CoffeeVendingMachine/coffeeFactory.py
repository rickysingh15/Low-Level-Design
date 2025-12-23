
from coffee import Coffee
from abc import ABC, abstractmethod

class CoffeeFactory:

    def __init__(self):
        pass

    def order_coffee(self) -> Coffee:
        return self.prepare()        

    @abstractmethod
    def prepare(self) -> Coffee:
        pass