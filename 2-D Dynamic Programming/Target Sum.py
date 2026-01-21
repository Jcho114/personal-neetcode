from typing import List
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        TC: O(n*sum(nums))
        SC: O(n*sum(nums))
        """
        @lru_cache(None)
        def helper(i: int, curr: int) -> int:
            if i == len(nums):
                return int(curr == target)
            return helper(i+1, curr+nums[i]) + helper(i+1, curr-nums[i])

        return helper(0, 0)