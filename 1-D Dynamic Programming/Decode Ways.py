from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        @lru_cache(None)
        def helper(i: int) -> int:
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i == len(s)-1:
                return 1

            j = i+1
            res = 0
            while j <= len(s) and int(s[i:j]) <= 26:
                res += helper(j)
                j += 1

            return res

        return helper(0)