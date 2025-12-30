from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        l, r = 0, len(height)-1
        maxL = maxR = 0
        res = 0

        while l <= r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL > height[l]:
                res += maxL - height[l]
                l += 1
                continue
            if maxR > height[r]:
                res += maxR - height[r]
                r -= 1
                continue

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res