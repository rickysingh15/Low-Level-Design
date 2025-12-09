from uuid import uuid4

class Player:

    def __init__(self, name: str, symbol: str, handle: str):
        self.id = str(uuid4())
        self.name = name
        self.symbol = symbol
        self.handle = handle