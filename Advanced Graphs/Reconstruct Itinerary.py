from typing import List
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        TC: O(ElogE)
        SC: O(E)
        """
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        for src in graph:
            graph[src].sort(reverse=True)

        res = []

        def backtrack(curr: str):
            while graph[curr]:
                backtrack(graph[curr].pop())
            res.append(curr)
        
        backtrack("JFK")
        
        return res[::-1]