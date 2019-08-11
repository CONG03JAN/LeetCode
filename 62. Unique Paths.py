class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        import numpy as np

        dp = [[0]*n]*m; dp = np.array(dp)

        dp[0, :] = 1
        dp[:, 0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]
