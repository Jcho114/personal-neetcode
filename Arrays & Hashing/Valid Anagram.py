from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        TC: O(n+m)
        SC: O(n+m)
        """
        count = Counter(s)
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1
        return all(val == 0 for _, val in count.items())
