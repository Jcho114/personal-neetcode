from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        TC: O(n)
        SC: O(n)
        """
        index = 0
        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            index += 1

        res = intervals[:index]

        while index < len(intervals) and newInterval[1] >= intervals[index][0]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1
        
        res.append(newInterval)
        res.extend(intervals[index:])

        return res