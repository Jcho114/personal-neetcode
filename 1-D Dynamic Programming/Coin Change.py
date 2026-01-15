from typing import List
from math import inf
from functools import lru_cache

class SolutionIterative:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        TC: O(A*C)
        SC: O(A)
        """
        dp = [inf]*(amount+1)
        dp[0] = 0

        for curr in range(amount+1):
            for coin in coins:
                if curr-coin >= 0 and dp[curr-coin]+1 < dp[curr]:
                    dp[curr] = dp[curr-coin]+1

        return dp[-1] if dp[-1] != inf else -1

class SolutionRecursive:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        TC: O(A*C)
        SC: O(A)
        """
        @lru_cache(None)
        def helper(curr: int) -> int:
            if curr == 0:
                return 0

            res = inf
            for coin in coins:
                if curr-coin >= 0:
                    res = min(res, helper(curr-coin))
            return res+1

        res = helper(amount)
        return res if res != inf else -1