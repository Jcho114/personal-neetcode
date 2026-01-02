from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        TC: O(2^n)
        SC: O(n^2)
        """
        dromes = set()

        for i in range(len(s)):
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                dromes.add(s[l:r+1])
                l -= 1
                r += 1

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                dromes.add(s[l:r+1])
                l -= 1
                r += 1
        
        res = []
        def helper(i: int, curr: List[str]):
            if i >= len(s):
                res.append(curr.copy())
                return

            for j in range(i+1, len(s)+1):
                if s[i:j] in dromes:
                    curr.append(s[i:j])
                    helper(j, curr)
                    curr.pop()
        
        helper(0, [])
        return res