from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        fresh, rotten = 1, 2
        queue = deque()
        N, M = len(grid), len(grid[0])

        for i in range(N):
            for j in range(M):
                if grid[i][j] == rotten:
                    queue.append((i, j))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        waves = 0
        while queue:
            spread = False
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] == fresh:
                        spread = True
                        grid[ni][nj] = rotten
                        queue.append((ni, nj))
            if spread:
                waves += 1

        for i in range(N):
            for j in range(M):
                if grid[i][j] == fresh:
                    return -1
        
        return waves