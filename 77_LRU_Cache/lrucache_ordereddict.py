import collections

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


if __name__ == "__main__":
    cache = LRUCache(10)
    for i in xrange(20):
        cache.set(i,i)
    print cache.cache
    print  cache.get(5)
    print  cache.get(15)
    cache.set(15, 30)
    print cache.cache
    cache.set(100,200)
    print cache.cache

