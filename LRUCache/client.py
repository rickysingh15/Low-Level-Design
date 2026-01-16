

from lruCache import LRUCache
from cacheService import CacheService
from operation import OperationType

cap = 1
service = CacheService(LRUCache(cap))

# val = service.get(5)
# print(val)

print(service.put(5, 10))

val1 = service.get(5)
print(val1)

print(service.put(8, 2))

print(service.getKeysOrder())

# print(service.put(8, 9))

# print(service.put(12, 123))

# print(service.getKeysOrder())

# print(service.put(19, 123))

# val2 = service.get(8)
# print(val2)

# print(service.getKeysOrder())

# print(service.put(12, 50))

# print(service.getKeysOrder())

# print(service.put(8, 9))

# print(service.getKeysOrder())

# print(service.put(15, 1))

# print(service.getKeysOrder())

# print(service.put(15, 3))

# print(service.getKeysOrder())

# print(service.put(12, 1))

# print(service.getKeysOrder())

# print(service.put(34, 9765))

# print(service.getKeysOrder())

#12 , 8 , 5 
# 19, 12, 8