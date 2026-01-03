from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        N, M = len(grid), len(grid[0])

        def erase(i: int, j: int):
            if 0 <= i < N and 0 <= j < M and grid[i][j] == "1":
                grid[i][j] = "0"
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    erase(ni, nj)
        
        res = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] == "1":
                    erase(i, j)
                    res += 1
        
        return res