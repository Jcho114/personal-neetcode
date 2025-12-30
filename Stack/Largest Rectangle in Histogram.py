from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        TC: O(n)
        SC: O(n)
        """
        stack = [-1]
        res = 0

        for i, height in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= height:
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                res = max(res, curr_height*curr_width)
            stack.append(i)
    
        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_width = len(heights) - stack[-1] - 1
            res = max(res, curr_height*curr_width)
        
        return res