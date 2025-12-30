from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        TC: O(n)
        SC: O(n)
        """
        res = [1]
        prefix = 1

        for i in range(len(nums)-1):
            prefix *= nums[i]
            res.append(prefix)

        postfix = 1
        for i in range(len(nums)-1, 0, -1):
            postfix *= nums[i]
            res[i-1] *= postfix

        return res