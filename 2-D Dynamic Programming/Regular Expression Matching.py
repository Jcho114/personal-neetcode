from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        @lru_cache(None)
        def backtrack(si: int, pi: int) -> bool:
            if pi == len(p):
                return si == len(s)

            first_match = si < len(s) and p[pi] in {s[si], "."}
            if pi < len(p)-1 and p[pi+1] == "*":
                return (
                    backtrack(si, pi+2) or
                    (
                        first_match
                        and backtrack(si+1, pi)
                    )
                )
            else:
                return first_match and backtrack(si+1, pi+1)
        
        return backtrack(0, 0)