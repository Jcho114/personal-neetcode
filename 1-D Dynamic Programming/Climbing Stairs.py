from functools import lru_cache

class SolutionOptimal:
    def climbStairs(self, n: int) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        first, second = 0, 1
        for _ in range(n):
            second, first = first+second, second
        return second

class SolutionIterative:
    def climbStairs(self, n: int) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]

class SolutionRecursive:
    def climbStairs(self, n: int) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        @lru_cache(None)
        def helper(n: int) -> int:
            if n == 0 or n == 1:
                return 1
            return helper(n-1) + helper(n-2)
        
        return helper(n)