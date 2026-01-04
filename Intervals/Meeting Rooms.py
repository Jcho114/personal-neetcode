from typing import List
from math import inf

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        TC: O(nlogn)
        SC: O(n)
        """
        if len(intervals) <= 1:
            return True

        intervals.sort(key=lambda interval: interval[1])
        k = -inf

        for start, end in intervals:
            if start < k:
                return False
            k = end
        
        return True