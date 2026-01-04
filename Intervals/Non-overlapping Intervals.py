from typing import List
from math import inf

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        TC: O(nlogn)
        SC: O(n)
        """
        intervals.sort(key=lambda interval: interval[1])
        k = -inf
        res = 0

        for start, end in intervals:
            if start < k:
                res += 1
                continue
            k = end
        
        return res