from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Got help on TC from editorial

        M = # cells on board
        L = Maximum length of a word in words
        N = Total # of letters in dictionary

        TC: O(M*(4*e^(L-1)))
        SC: O(N)
        """
        root = {}
        for word in words:
            curr = root
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr["$"] = word
        
        N, M = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        res = []
        def dfs(curr, i, j, parent):
            word = curr.pop("$", None)
            if word:
                res.append(word)

            letter, board[i][j] = board[i][j], '.'

            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0 <= ni < N and 0 <= nj < M and board[ni][nj] in curr:
                    dfs(curr[board[ni][nj]], ni, nj, curr)

            board[i][j] = letter
            if not curr:
                parent.pop(letter)

        for i in range(N):
            for j in range(M):
                if board[i][j] in root:
                    dfs(root[board[i][j]], i, j, root)

        return res