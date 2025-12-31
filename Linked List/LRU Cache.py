from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        """
        TC: O(1)
        SC: O(n)
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        """
        TC: O(1)
        SC: O(1)
        """
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        """
        TC: O(1)
        SC: O(1)
        """
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)