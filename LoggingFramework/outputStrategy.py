
from abc import ABC, abstractmethod
from log import Log
from outputFormatter import OutputFormatter

class OutputStrategy(ABC):

    def __init__(self, output_formatter: OutputFormatter):
        pass

    @abstractmethod
    def format(self, log: Log):
        pass

    @abstractmethod
    def output(self, log: Log):
        pass