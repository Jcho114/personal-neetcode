from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        TC: O(nlogn)
        SC: O(n)
        """
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            s1, s2 = -heapq.heappop(heap), -heapq.heappop(heap)
            if s1 == s2:
                continue
            diff = s2-s1
            heapq.heappush(heap, diff)
        
        return -heap[0] if heap else 0