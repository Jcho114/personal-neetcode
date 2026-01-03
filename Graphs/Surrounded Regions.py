from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        N, M = len(board), len(board[0])
        queue = deque()

        for i in range(N):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][M-1] == "O":
                queue.append((i, M-1))
        
        for j in range(1, M-1):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[N-1][j] == "O":
                queue.append((N-1, j))

        while queue:
            i, j = queue.popleft()
            board[i][j] = "L"
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and board[ni][nj] == "O":
                    queue.append((ni, nj))

        for i in range(N):
            for j in range(M):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "L":
                    board[i][j] = "O"
