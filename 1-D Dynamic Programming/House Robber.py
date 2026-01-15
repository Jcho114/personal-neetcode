from typing import List
from functools import lru_cache

class SolutionOptimal:
    def rob(self, nums: List[int]) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        prev = curr = 0
        for num in nums:
            prev, curr = curr, max(prev+num, curr)
        return max(prev, curr)

class SolutionIterative:
    def rob(self, nums: List[int]) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        nums[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])
        return nums[-1]

class SolutionRecursive:
    def rob(self, nums: List[int]) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        @lru_cache(None)
        def helper(curr: int) -> int:
            if curr == 0:
                return nums[0]
            if curr == 1:
                return max(nums[0], nums[1])
            return max(helper(curr-2) + nums[curr], helper(curr-1))

        return helper(len(nums)-1)