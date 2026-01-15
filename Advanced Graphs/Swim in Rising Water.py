from typing import List
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        TC: O(n^2*logn)
        SC: O(n^2)
        """
        N, M = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        heap = [(grid[0][0], 0, 0)]
        grid[0][0] = -1
        res = 0

        while heap:
            time, i, j = heapq.heappop(heap)
            res = max(res, time)

            if i == N-1 and j == M-1:
                return res
            
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and grid[ni][nj] != -1:
                    heapq.heappush(heap, (grid[ni][nj], ni, nj))
                    grid[ni][nj] = -1
        
        return res