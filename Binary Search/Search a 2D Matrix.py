from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        TC: O(log(nm))
        SC: O(1)
        """
        N, M = len(matrix), len(matrix[0])
        l, r = 0, N-1
        row = None

        while l <= r:
            c = (l+r)//2
            if matrix[c][0] <= target <= matrix[c][-1]:
                row = c
                break
            elif matrix[c][-1] < target:
                l = c+1
            else:
                r = c-1

        if row is None:
            return False
        
        l, r = 0, M-1
        while l <= r:
            c = (l+r)//2
            if matrix[row][c] < target:
                l = c+1
            elif matrix[row][c] > target:
                r = c-1
            else:
                return True
        
        return False