from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        res = 0

        l, r = 0, len(height)-1
        while l <= r:
            area = min(height[l], height[r])*(r-l)
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res