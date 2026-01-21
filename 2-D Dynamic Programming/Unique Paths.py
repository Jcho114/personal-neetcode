from functools import lru_cache

class SolutionOptimal:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        TC: O(n*m)
        SC: O(m)        
        """
        bottom_row = [1]*m

        for _ in range(n-1):
            top_row = bottom_row
            bottom_row = [0]*m
            for j in range(m):
                bottom_row[j] += top_row[j]
                if j > 0:
                    bottom_row[j] += bottom_row[j-1]

        return bottom_row[-1]

class SolutionIterative:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        dp = [[0 for _ in range(m)] for _ in range(n)]
        directions = [(1, 0), (0, 1)]
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                for di, dj in directions:
                    ni, nj = i-di, j-dj
                    if 0 <= ni < n and 0 <= nj < m:
                        dp[i][j] += dp[ni][nj]

        return dp[-1][-1]

class SolutionRecursive:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        directions = [(1, 0), (0, 1)]

        @lru_cache(None)
        def helper(i: int, j: int) -> int:
            if i == n-1 and j == m-1:
                return 1

            res = 0
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m:
                    res += helper(ni, nj)
            return res
        
        return helper(0, 0)