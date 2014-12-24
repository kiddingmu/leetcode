class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.priority = 0
        self.size = 0

    # @return an integer
    def get(self, key):
        val = self.cache.get(key, None)
        if val:
            return val[0]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            self.cache[key] = (value, self.priority+1)
        else:
            self.priority += 1
            if self.size < self.capacity:
                self.cache[key] = (value, self.priority)
                self.size += 1
            else:
                # find the least recently used item
                sorted_cache = sorted(self.cache.items(), key=lambda x:x[1][1])
                delete_key = sorted_cache[0][0]
                # delete the item
                del self.cache[delete_key]
                # add new item
                self.cache[key] = (value, self.priority)


if __name__ == "__main__":
    cache = LRUCache(10)
    for i in xrange(20):
        cache.set(i,i)
    print cache.size
    print cache.cache
    print  cache.get(5)
    print  cache.get(15)
    cache.set(15, 30)
    print cache.cache
    cache.set(100,200)
    print cache.cache

