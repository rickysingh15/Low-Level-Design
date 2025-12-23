

from abc import ABC, abstractmethod

class State(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def start_progress(self):
        pass

    @abstractmethod
    def complete_task(self):
        pass

    @abstractmethod
    def reopen_task(self):
        pass