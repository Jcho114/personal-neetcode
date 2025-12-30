from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        
        def offsetted(i: int) -> int:
            return (i + offset) % len(nums)

        offset = r
        l, r = 0, len(nums)-1
        while l <= r:
            c = (l+r)//2
            ofc = offsetted(c)
            if nums[ofc] < target:
                l = c+1
            elif nums[ofc] > target:
                r = c-1
            else:
                return ofc
        
        return -1