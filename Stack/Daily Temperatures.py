from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        TC: O(n)
        SC: O(n)
        """
        res = [0]*len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                j, _ = stack.pop()
                res[j] = i-j
            stack.append((i, temp))
        
        return res