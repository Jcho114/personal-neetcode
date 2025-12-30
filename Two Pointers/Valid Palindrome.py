class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        TC: O(n)
        SC: O(1)
        """
        def valid(c: str) -> bool:
            return c in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        
        s = "".join(list(filter(valid, s))).lower()

        l, r = 0, len(s)-1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True