from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        TC: O(n)
        SC: O(n)
        """
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False
