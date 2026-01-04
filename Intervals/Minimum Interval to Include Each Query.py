from typing import List
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        NOTE: Heavily based off of neetcode solution
        TC: O((n+m)log(n+m))
        SC: O(n+m)
        """
        events = []

        for i, (start, end) in enumerate(intervals):
            events.append((start, 0, end-start+1, i))
            events.append((end, 2, end-start+1, i))

        for i, query in enumerate(queries):
            events.append((query, 1, i))

        events.sort()

        sizes = []
        active = [True]*len(intervals)
        res = [-1]*len(queries)

        for _, kind, *rest in events:
            if kind == 0:
                heapq.heappush(sizes, (rest[0], rest[1]))
            elif kind == 2:
                active[rest[1]] = False
            else:
                i = rest[0]
                while sizes and not active[sizes[0][1]]:
                    heapq.heappop(sizes)
                if sizes:
                    res[i] = sizes[0][0]
        
        return res