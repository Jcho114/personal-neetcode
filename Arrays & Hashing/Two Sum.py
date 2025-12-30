from typing import List
from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        TC: O(n)
        SC: O(n)
        """
        dct = defaultdict(int)
        for i, num in enumerate(nums):
            if num in dct:
                return [i, dct[num]]
            dct[target-num] = i
        return [-1,-1]
