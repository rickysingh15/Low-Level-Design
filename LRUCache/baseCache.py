

from abc import ABC, abstractmethod
from value import Value

class BaseCache:

    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def put(self, key: str, value:Value):
        pass