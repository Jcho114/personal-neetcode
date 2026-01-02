from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        TC: O(2^n)
        SC: O(n)
        """
        res = []
        nums.sort()

        def helper(i: int, curr: List[int]):
            if i == len(nums):
                res.append(curr.copy())
                return res
            
            curr.append(nums[i])
            helper(i+1, curr)
            curr.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            helper(i+1, curr)

        helper(0, [])
        return res