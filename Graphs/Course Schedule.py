from typing import List
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        TC: O(V + E)
        SC: O(V + E)
        """
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
        
        return len(res) == numCourses