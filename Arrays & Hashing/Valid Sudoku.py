from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        TC: O(n^2)
        SC: O(n^2)
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        N, M = len(board), len(board[0])
        for i in range(N):
            for j in range(M):
                curr = board[i][j]
                if curr == ".":
                    continue
                
                if curr in rows[i]:
                    return False
                rows[i].add(curr)

                if curr in cols[j]:
                    return False
                cols[j].add(curr)

                square = (i//3, j//3)
                if curr in squares[square]:
                    return False
                squares[square].add(curr)
        
        return True

