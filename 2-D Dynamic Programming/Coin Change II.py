from typing import List
from functools import lru_cache

class SolutionOptimal:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        TC: O(n*a)
        SC: O(a)
        """
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(n):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]

        return dp[amount]

class SolutionRecursive:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        TC: O(n*a)
        SC: O(n*a)
        """
        coins.sort()

        @lru_cache(None)
        def helper(i: int, a: int) -> int:
            if a == amount:
                return 1
            if i >= len(coins) or amount - a < coins[i]:
                return 0

            return helper(i+1, a) + helper(i, a+coins[i])

        return helper(0, 0)