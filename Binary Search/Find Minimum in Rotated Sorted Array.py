from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        TC: O(logn)
        SC: O(1)
        """
        l, r = 0, len(nums)-1
        while l < r:
            c = (l+r)//2
            if nums[c] > nums[r]:
                l = c+1
            else:
                r = c
        return nums[r]