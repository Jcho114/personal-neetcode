from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        TC: O(2^(T/m))
        SC: O(T/m)
        """
        res = []

        def helper(i: int, curr: List[int], sm: int):
            if sm > target or i == len(candidates):
                return
            if sm == target:
                res.append(curr.copy())
                return
            
            curr.append(candidates[i])
            helper(i, curr, sm+candidates[i])
            curr.pop()
            helper(i+1, curr, sm)
        
        helper(0, [], 0)
        return res