from functools import lru_cache
from typing import List

class SolutionIterative:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        dp = [0]*(len(cost)+1)
        dp[0] = dp[1] = 0
        for i in range(2, len(cost)+1):
            one, two = dp[i-1] + cost[i-1], dp[i-2] + cost[i-2]
            dp[i] = min(one, two)
        return dp[-1]

class SolutionRecursive:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        @lru_cache(None)
        def helper(curr: int) -> int:
            if curr <= 1:
                return 0
            one, two = helper(curr-1) + cost[curr-1], helper(curr-2) + cost[curr-2]
            return min(one, two)

        return helper(len(cost))