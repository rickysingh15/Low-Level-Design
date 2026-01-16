
from abc import ABC, abstractmethod

class State(ABC):

    def __init__(self, machine):
        self.machine = machine

    @abstractmethod
    def filInventory(self, cash_dict):
        pass

    @abstractmethod
    def pressMaintenanceButton(self):
        pass

    @abstractmethod
    def insertCard(self):
        pass

    @abstractmethod
    def depositCash(self, cash_dict: dict):
        pass

    @abstractmethod
    def enterPin(self, pin: str):
        pass

    @abstractmethod
    def getCash(self, amount: int):
        pass

    @abstractmethod
    def checkBalance(self):
        pass
