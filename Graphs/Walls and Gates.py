from typing import List
from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        queue = deque()
        N, M = len(rooms), len(rooms[0])
        empty, gate = 2147483647, 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(N):
            for j in range(M):
                if rooms[i][j] == gate:
                    for di, dj in directions:
                        queue.append((1, i+di, j+dj))
        
        while queue:
            d, i, j = queue.popleft()
            if 0 <= i < N and 0 <= j < M and rooms[i][j] == empty:
                rooms[i][j] = d
                for di, dj in directions:
                    ni, nj = i+di, j+dj
                    queue.append((d+1, ni, nj))