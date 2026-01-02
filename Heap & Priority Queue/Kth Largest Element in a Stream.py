from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        TC: O(nlogk)
        SC: O(k)
        """
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        TC: O(logk)
        SC: O(k)
        """
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]