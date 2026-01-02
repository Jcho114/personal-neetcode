from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        TC: O(n!)
        SC: O(n^2)
        """
        cols = set()
        diags = set()
        adiags = set()

        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []

        def helper(row: int):
            if row == n:
                res.append(["".join(row) for row in board])
                return

            for col in range(n):
                diag = row-col
                adiag = row+col

                if col in cols or diag in diags or adiag in adiags or board[row][col] == 'Q':
                    continue

                board[row][col] = 'Q'
                cols.add(col)
                diags.add(diag)
                adiags.add(adiag)

                helper(row+1)

                board[row][col] = '.'
                cols.remove(col)
                diags.remove(diag)
                adiags.remove(adiag)

        helper(0)
        return res