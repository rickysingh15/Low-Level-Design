
from baseCache import BaseCache
from value import Value

class CacheService:

    def __init__(self, cache: BaseCache):
        self.cache = cache

    def get(self, key: str):
        return self.cache.get(key)

    def put(self, key: str, value: str):
        return self.cache.put(key, value)

    def getKeysOrder(self):
        return self.cache.getKeysOrder()