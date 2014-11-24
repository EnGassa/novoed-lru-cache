class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__usage = []
        self.__store = {}

    # @return an integer
    def get(self, key):
        val = self.__store.get(key)
        # update usage order
        if val:
            self.__update_usage(key) 
        else:
            val = -1
        return val
        
    def __update_usage(self, key):
        try:
            idx = self.__usage.index(key)
            self.__usage.remove(key)
        except:
            pass
        self.__usage.insert(0, key)

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if not self.__store.get(key) and len(self.__store) == self.__capacity:
            # make room for 1
            purged = self.__usage.pop()
            try:
                self.__store.pop(purged)
            except:
                pass
        self.__store[key] = value
        self.__update_usage(key)
        
    # Clears the cache
    def clear(self):
        self.__store = {}
        self.__usage = []
        