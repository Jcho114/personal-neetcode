from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        s = set(nums)
        res = 0
        for num in set(nums):
            if num-1 in s:
                continue
            count = 0
            while num in s:
                num += 1
                count += 1
            res = max(count, res)
        return res