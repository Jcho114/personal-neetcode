from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        pqueue, aqueue = deque(), deque()
        N, M = len(heights), len(heights[0])

        for i in range(1, N):
            pqueue.append((i, 0))
        
        for i in range(0, N-1):
            aqueue.append((i, M-1))
        
        for j in range(M):
            pqueue.append((0, j))
            aqueue.append((N-1, j))
        
        pvisited, avisited = set(), set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while pqueue:
            i, j = pqueue.popleft()
            pvisited.add((i, j))
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and heights[ni][nj] >= heights[i][j] and (ni, nj) not in pvisited:
                    pqueue.append((ni, nj))
        
        while aqueue:
            i, j = aqueue.popleft()
            avisited.add((i, j))
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and heights[ni][nj] >= heights[i][j] and (ni, nj) not in avisited:
                    aqueue.append((ni, nj))
        
        return list(pvisited.intersection(avisited))