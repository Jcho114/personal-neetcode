from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        @lru_cache(None)
        def helper(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0
            
            if buying:
                return max(
                    helper(i+1, False) - prices[i],
                    helper(i+1, True)
                )
            else:
                return max(
                    helper(i+1, False),
                    helper(i+2, True) + prices[i]
                )

        return helper(0, True)