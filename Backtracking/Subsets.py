from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        TC: O(n * 2^n)
        SC: O(n)
        """
        res = []

        def helper(i: int, curr: List[int]):
            if i == len(nums):
                res.append(curr.copy())
                return

            helper(i+1, curr)
            curr.append(nums[i])
            helper(i+1, curr)
            curr.pop()

        helper(0, [])
        
        return res