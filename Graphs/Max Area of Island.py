from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        N, M = len(grid), len(grid[0])

        def helper(i: int, j: int) -> int:
            if 0 <= i < N and 0 <= j < M and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + sum(helper(i+di, j+dj) for di, dj in directions)
            return 0
        
        res = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    res = max(res, helper(i, j))
        
        return res