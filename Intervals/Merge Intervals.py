from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        TC: O(nlogn)
        SC: O(n)
        """
        intervals.sort(key=lambda interval: interval[0])
        res = []
        
        for start, end in intervals:
            if res and start <= res[-1][1]:
                res[-1][0] = min(res[-1][0], start)
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start, end])

        return res