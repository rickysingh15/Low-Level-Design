from abc import ABC, abstractmethod

class PaymentMethod:

    def __init__(self):
        pass
    
    @abstractmethod
    def pay(self):
        pass