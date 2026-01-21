from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        @lru_cache(None)
        def helper(i: int, j: int) -> int:
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return helper(i+1, j+1)
            return 1 + min(
                helper(i+1, j),
                helper(i, j+1),
                helper(i+1, j+1)
            )
        
        return helper(0, 0)