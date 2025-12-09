
from abc import ABC, abstractmethod

class State:

    def __init__(self):
        pass
        
    @abstractmethod
    def insert_coin(self):
        pass

    @abstractmethod
    def select_number(self):
        pass

    @abstractmethod
    def dispense_item(self):
        pass