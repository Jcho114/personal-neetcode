class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        TC: O(n^2)
        SC: O(1)
        """
        res = ""

        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > len(res):
                res = s[l+1:r]

            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r-l-1 > len(res):
                res = s[l+1:r]

        return res