from typing import List
from math import inf

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low, res = inf, -inf
        for price in prices:
            low = min(low, price)
            res = max(res, price-low)
        return res