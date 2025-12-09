
from outputStrategy import OutputStrategy
from log import Log

class OutputController:

    def __init__(self, output_strategy: OutputStrategy):
        self.output_strategy = output_strategy

    def output(self, log: Log):
        self.output_strategy.output(log=log)