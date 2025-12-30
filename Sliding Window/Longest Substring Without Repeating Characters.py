from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        seen = defaultdict(int)
        res = l = 0
        for r in range(len(s)):
            c = s[r]
            if c in seen and seen[c] >= l:
                l = seen[c]+1
            seen[c] = r
            res = max(res, r-l+1)
        return res