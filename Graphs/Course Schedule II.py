from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0]*numCourses
        graph = defaultdict(list)

        for dst, src in prerequisites:
            graph[src].append(dst)
            indegrees[dst] += 1
        
        queue = deque()
        for course, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(course)
        
        res = []
        while queue:
            course = queue.popleft()
            res.append(course)

            for dst in graph[course]:
                indegrees[dst] -= 1
                if indegrees[dst] == 0:
                    queue.append(dst)
        
        return res if len(res) == numCourses else []