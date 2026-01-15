from typing import List
from math import inf
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        TC: O(V+ElogV)
        SC: O(V+E)
        """
        distances = [inf]*n
        distances[k-1] = 0
        heap = [(0, k-1)]

        graph = [[] for _ in range(n)]
        for src, dst, time in times:
            graph[src-1].append((dst-1, time))

        while heap:
            dist, node = heapq.heappop(heap)
            for neighbor, time in graph[node]:
                new_distance = dist + time
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))

        res = max(distances)
        return res if res != inf else -1