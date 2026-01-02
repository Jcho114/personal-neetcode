from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        TC: O(2^n)
        SC: O(n)
        """
        res = set()
        candidates.sort()

        def helper(i: int, curr: List[int], sm: int):
            if sm == target:
                res.add(tuple(curr))
                return
            if i == len(candidates) or sm > target:
                return
            
            curr.append(candidates[i])
            helper(i+1, curr, sm+candidates[i])
            curr.pop()
            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1, curr, sm)
            
        helper(0, [], 0)
        return [list(tup) for tup in res]