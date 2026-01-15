from typing import List
from math import inf

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        TC: O(n)
        SC: O(1)
        """
        minVal = maxVal = 1
        res = -inf
        for num in nums:
            temp1, temp2, temp3 = minVal*num, maxVal*num, num
            minVal, maxVal = min(temp1, temp2, temp3), max(temp1, temp2, temp3)
            res = max(res, maxVal)
        return res