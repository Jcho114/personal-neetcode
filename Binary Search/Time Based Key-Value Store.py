from collections import defaultdict

class TimeMap:
    def __init__(self):
        """
        TC: O(1)
        SC: O(n)
        """
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        TC: O(1)
        SC: O(1)
        """
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        TC: O(logn)
        SC: O(1)
        """
        if key not in self.map:
            return ""
        
        lst = self.map[key]
        l, r = 0, len(lst)-1
        
        while l <= r:
            c = (l+r)//2
            if lst[c][0] < timestamp:
                l = c+1
            elif lst[c][0] > timestamp:
                r = c-1
            else:
                return lst[c][1]
        
        return lst[r][1] if r >= 0 else ""