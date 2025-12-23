
from abc import ABC, abstractmethod

class PayStrategy(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def pay(self, amount: int):
        pass