from typing import List
from collections import defaultdict

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        N, M = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cache = defaultdict(int)

        def helper(i: int, j: int) -> int:
            if (i, j) in cache:
                return cache[i, j]

            res = 1
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and matrix[ni][nj] > matrix[i][j]:
                    res = max(res, 1+helper(ni, nj))

            cache[i, j] = res
            return res

        res = 0
        for i in range(N):
            for j in range(M):
                res = max(res, helper(i, j))
        return res