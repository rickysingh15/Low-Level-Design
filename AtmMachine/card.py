from uuid import uuid4
class Card:

    def __init__(self):
        self.id = str(uuid4())
        self.cvv = str(uuid4())[:3]