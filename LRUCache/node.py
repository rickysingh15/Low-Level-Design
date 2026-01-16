
from __future__ import annotations
from uuid import uuid4
from value import Value

class Node:

    def __init__(self, key: str, value: Value, next: Node = None, prev: Node = None):
        self._id = str(uuid4())
        self._key = key
        self._value = value
        self._next = next
        self._prev = prev

    @property
    def key(self):
        return self._key
    
    @property
    def id(self):
        return self._id
    
    @property
    def value(self):
        return self._value
    
    @property
    def next(self):
        return self._next

    @property
    def prev(self):
        return self._prev    
    
    @key.setter
    def key(self, key: str):
        self._key = key

    @value.setter
    def value(self, value: Value):
        self._value = value

    @next.setter
    def next(self, next: Node):
        self._next = next

    @prev.setter
    def prev(self, prev: Node):
        self._prev = prev