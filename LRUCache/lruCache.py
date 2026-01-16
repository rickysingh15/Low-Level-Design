
import threading
from baseCache import BaseCache
from typing import Dict
from node import Node

class LRUCache(BaseCache):

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, capacity: int):
        if not hasattr(self, "_initialized"):
            self._initialized = True
            self.totalCapacity = capacity
            self.currCapacity = 0
            self.head = None
            self.tail = None
            self.keyToNodeMap: Dict[str, Node] = {}


    def getKeysOrder(self):
        with LRUCache._lock:
            order = list()
            curr = self.head
            while curr != None:
                order.append(curr.key)
                curr = curr.next
            return order

    def get(self, key):
        with LRUCache._lock:
            node = None
            if key in self.keyToNodeMap:
                node = self.keyToNodeMap.get(key, None)
                self.setHead(node)
                return node.value
            return -1

    def put(self, key, value):
        with LRUCache._lock:
            node = None
            if key not in self.keyToNodeMap:
                node = Node(key, value)
                self.keyToNodeMap[key] = node
                self.currCapacity += 1
            else:
                node = self.keyToNodeMap.get(key, None)
                node.value = value
            self.setHead(node)
            if self.currCapacity > self.totalCapacity:
                self.deleteTail()
                self.currCapacity -= 1

    def setHead(self, node: Node):
        if self.head == None:
            print("No head found making ", node.key, " as head")
            self.head = node
            self.tail = node
            return

        if self.head == node:
            print("node already at head")
            return
        
        if self.tail == node:
            self.tail = self.tail.prev

    
        prevNode = node.prev
        nextNode = node.next
        if prevNode:
            prevNode.next = node.next
        if nextNode:
            nextNode.prev = node.prev
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None
        if self.tail is None:
            print("setting tail to ", node.key)
            self.tail = node


    def deleteTail(self):
        tail_node = self.keyToNodeMap.get(self.tail.key)
        self.tail = self.tail.prev
        self.tail.next = None
        self.keyToNodeMap.pop(tail_node.key)
        print("after deleting tail ", self.keyToNodeMap.keys())
        if tail_node:
            del tail_node

        
