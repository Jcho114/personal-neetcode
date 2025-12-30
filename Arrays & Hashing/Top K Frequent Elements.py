from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        TC: O(nlogn)
        SC: O(n)
        """
        freqs = Counter(nums)
        return sorted(set(nums), key=lambda num: freqs[num], reverse=True)[:k]
