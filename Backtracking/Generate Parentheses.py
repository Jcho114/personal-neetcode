from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        TC: O(2^n)
        SC: O(n)
        """
        res = []

        def helper(o: int, c: int, curr: str):
            if o == 0:
                res.append(curr + ")"*c)
                return
            
            helper(o-1, c, curr+"(")
            if c > o:
                helper(o, c-1, curr+")")

        helper(n, n, "")
        return res