# Run Tests:
# python -m unittest tests.unit_tests
# from the root of the repository
from collections import OrderedDict
class LRUCache():

    # @param capacity, an integer
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__store = OrderedDict()

    # @param key
    # @return an object
    def get(self, key):
        try:
            val = self.__store.pop(key)
            # update usage order
            self.__store[key] = val
            return val
        except:
            return None

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            self.__store.pop(key)
        except:
            pass
        self.__store[key] = value
        while(len(self.__store) > self.__capacity):
            self.__store.popitem(last=False)

    # Clears the cache
    def clear(self):
        self.__store = OrderedDict()

