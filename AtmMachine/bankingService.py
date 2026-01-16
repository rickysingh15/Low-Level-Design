
from abc import ABC, abstractmethod

class BankService(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def debit(self):
        pass


class ICICIBanckingService(BankService):

    def __init__(self):
        pass

    def authenticate(self):
        pass

    def debit(self):
        pass
