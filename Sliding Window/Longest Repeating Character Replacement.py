from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        counts = defaultdict(int)
        res = l = 0
        maxFreq = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            maxFreq = max(maxFreq, counts[s[r]])
            while l < r and maxFreq + k < r-l+1:
                counts[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res