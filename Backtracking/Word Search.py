from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        TC: O(n * 3^l)
        SC: O(l)
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def helper(i: int, j: int, c: int) -> bool:
            if c == len(word):
                return True

            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == word[c] and board[ni][nj] != '':
                    board[ni][nj] = ''
                    if helper(ni, nj, c+1):
                        return True
                    board[ni][nj] = word[c]
            return False

        N, M = len(board), len(board[0])
        for i in range(N):
            for j in range(M):
                if board[i][j] == word[0]:
                    board[i][j] = ''
                    if helper(i, j, 1):
                        return True
                    board[i][j] = word[0]
        
        return False