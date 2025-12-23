
from abc import ABC, abstractmethod
from uuid import uuid4

class Coffee:

    def __init__(self):
        self.id = str(uuid4())