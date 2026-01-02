from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        TC: O(4^n)
        SC: O(n)
        """
        chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def helper(i: int, curr: str):
            if i == len(digits):
                res.append(curr)
                return
            
            paths = chars[digits[i]]
            for path in paths:
                helper(i+1, curr+path)
    
        helper(0, "")
        return res