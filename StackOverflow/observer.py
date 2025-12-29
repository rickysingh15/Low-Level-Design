
from abc import ABC, abstractmethod

class Observer:

    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass