from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        TC: O(n!)
        SC: O(n)
        """
        res = []

        def helper(i: int):
            if i == len(nums):
                res.append(nums.copy())
                return
            
            for j in range(i, len(nums)):
                nums[i], nums[j], = nums[j], nums[i]
                helper(i+1)
                nums[i], nums[j], = nums[j], nums[i]

        helper(0)
        return res