from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        TC: O(nlogm)
        SC: O(1)
        """
        def simulate(rate: int) -> bool:
            res = 0
            for pile in piles:
                res += math.ceil(pile/rate)
            return res <= h

        l, r = 1, sum(piles)
        while l < r:
            c = (l+r)//2
            if simulate(c):
                r = c
            else:
                l = c+1

        return l