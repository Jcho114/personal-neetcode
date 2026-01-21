from functools import lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        @lru_cache(None)
        def helper(i: int, j: int) -> int:
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            if s[i] == t[j]:
                return helper(i+1, j+1) + helper(i+1, j)
            return helper(i+1, j)
        
        return helper(0, 0)