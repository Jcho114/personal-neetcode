from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        @lru_cache(None)
        def helper(i: int, j: int) -> bool:
            k = i+j
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if i < len(s1) and s1[i] == s3[k] and helper(i+1, j):
                return True
            if j < len(s2) and s2[j] == s3[k] and helper(i, j+1):
                return True
            return False

        return helper(0, 0)