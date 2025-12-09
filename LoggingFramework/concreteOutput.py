from log import Log
from outputStrategy import OutputStrategy
from outputFormatter import OutputFormatter

class ConsoleOutputStrategy(OutputStrategy):

    def __init__(self, output_formatter: OutputFormatter):
        self.output_formatter = output_formatter

    def format(self, log: Log):
        message = self.output_formatter.format(log.message.get_content())
        log.message.set_content(message=message)
        return log

    def output(self, log: Log):
        log = self.format(log)
        print("log ", log.describe())
        print("Log printed on the console")


class DatabaseOutputStrategy(OutputStrategy):

    def __init__(self, connection, output_formatter: OutputFormatter):
        self.connection = connection
        self.output_formatter = output_formatter

    def format(self, log: Log):
        message = self.output_formatter.format(log.message.get_content())
        log.message.set_content(message=message)
        return log

    def output(self, log: Log):
        log = self.format(log)
        print("log ", log.describe())
        print("Log saved inside the database")


class FileOutputStrategy(OutputStrategy):

    def __init__(self, file_path: str, output_formatter: OutputFormatter):
        self.file_path = file_path
        self.output_formatter = output_formatter

    def format(self, log: Log):
        message = self.output_formatter.format(log.message.get_content())
        log.message.set_content(message=message)
        return log

    def output(self, log: Log):
        log = self.format(log)
        print("log ", log.describe())
        print("Log printed on a file ", self.file_path)