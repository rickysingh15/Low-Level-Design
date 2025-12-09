
from uuid import uuid4
from message import Message
from logLevel import LogLevel
from datetime import datetime

class Log:

    def __init__(self, message: Message, level: str):
        self.id = str(uuid4())
        self.message = Message(message)
        self.timestamp = datetime.utcnow()
        self.level = level

    def describe(self):
        print("log level ", self.level)
        print("timestamp ", self.timestamp)
        print("message ", self.message.get_content())
