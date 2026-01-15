from typing import List
from collections import defaultdict
from math import inf
import heapq

class SolutionOptimal:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        TC: O(N^2)
        SC: O(N)
        """
        res = 0
        visited = set()
        distances = [inf]*len(points)
        distances[0] = 0

        while len(visited) < len(points):
            best_edge = inf
            best_node = -1

            for node in range(len(points)):
                if node not in visited and best_edge > distances[node]:
                    best_edge = distances[node]
                    best_node = node
            
            res += best_edge
            visited.add(best_node)

            for node in range(len(points)):
                x1, y1 = points[best_node]
                x2, y2 = points[node]
                dist = abs(x1-x2) + abs(y1-y2)

                if node not in visited and distances[node] > dist:
                    distances[node] = dist
            
        return res

class SolutionUnoptimal:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        TC: O(N^2 log N)
        SC: O(N^2)
        """
        graph = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                graph[i].append((j, dist))
                graph[j].append((i, dist))

        res = 0
        visited = set()
        heap = [(0, 0)]

        while len(visited) < len(points):
            dist, node = heapq.heappop(heap)
            if node in visited:
                continue
            res += dist
            visited.add(node)
            for neighbor, next_dist in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(heap, (next_dist, neighbor))

        return res