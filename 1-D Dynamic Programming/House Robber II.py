from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        if len(nums) == 1:
            return nums[0]

        def helper(l: int, r: int) -> int:
            prev = curr = 0
            for i in range(l, r+1):
                num = nums[i]
                prev, curr = curr, max(prev+num, curr)
            return max(prev, curr)

        return max(helper(0, len(nums)-2), helper(1, len(nums)-1))