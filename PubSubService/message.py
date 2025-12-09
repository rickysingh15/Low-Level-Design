
from uuid import uuid4
class Message:

    def __init__(self, content: str):
        self.id = str(uuid4())
        self.content = content