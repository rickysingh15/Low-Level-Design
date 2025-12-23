
from abc import ABC, abstractmethod

class MachineState:

    def __init__(self):
        pass

    @abstractmethod
    def select_coffee(self):
        pass

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def dispense(self):
        pass