from outputFormatter import OutputFormatter

class JsonOutputFormatter(OutputFormatter):

    def __init__(self):
        pass

    def format(self, message: str):
        print(" message ", message, " json formatted")


class PlainTextOutputFormatter(OutputFormatter):

    def __init__(self):
        pass

    def format(self, message: str):
        print(" message ", message, " plain text formatted")