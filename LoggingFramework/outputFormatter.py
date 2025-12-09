
from abc import ABC, abstractmethod

class OutputFormatter:

    def __init__(self):
        pass

    @abstractmethod
    def format(self, message: str):
        pass
