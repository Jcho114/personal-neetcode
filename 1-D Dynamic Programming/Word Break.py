from typing import List
from functools import lru_cache

class SolutionIterative:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        TC: O(n*m*k)
        SC: O(n)
        """
        dp = [False]*(len(s)+1)
        dp[0] = True

        for i in range(len(s)+1):
            for word in wordDict:
                if i-len(word) >= 0 and s[i-len(word):i] == word and dp[i-len(word)]:
                    dp[i] = True
                    break

        return dp[-1]

class SolutionRecursive:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        TC: O(n*m*k)
        SC: O(n)
        """
        @lru_cache(None)
        def helper(curr: int) -> bool:
            if curr == len(s):
                return True
            
            res = False
            for word in wordDict:
                if s[curr:curr+len(word)] == word:
                    res = res or helper(curr+len(word))
            return res
        
        return helper(0)