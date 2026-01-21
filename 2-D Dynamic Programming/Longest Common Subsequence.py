from functools import lru_cache

class SolutionIterative:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        N, M = len(text1), len(text2)
        dp = [[0 for _ in range(M)] for _ in range(N)]
        
        colFlag = False
        for i in range(N):
            if text1[i] == text2[0]:
                colFlag = True
            dp[i][0] = 1 if colFlag else 0
        
        rowFlag = False
        for j in range(M):
            if text1[0] == text2[j]:
                rowFlag = True
            dp[0][j] = 1 if rowFlag else 0
        
        for i in range(1, N):
            for j in range(1, M):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(
                        dp[i-1][j] if i-1 >= 0 else 0,
                        dp[i][j-1] if j-1 >= 0 else 0
                    )

        return dp[-1][-1]

class SolutionRecursive:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        TC: O(n*m)
        SC: O(n*m)
        """
        @lru_cache(None)
        def helper(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + helper(i+1, j+1)
            
            return max(helper(i+1, j), helper(i, j+1))

        return helper(0, 0)