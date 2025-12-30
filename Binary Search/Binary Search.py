from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        TC: O(logn)
        SC: O(1)
        """
        l, r = 0, len(nums)-1

        while l <= r:
            c = (l+r)//2
            if nums[c] < target:
                l = c+1
            elif nums[c] > target:
                r = c-1
            else:
                return c

        return -1