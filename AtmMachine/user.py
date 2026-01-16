
from uuid import uuid4

class User:

    def __init__(self, name :str):
        self.id = str(uuid4())
        self.name = name