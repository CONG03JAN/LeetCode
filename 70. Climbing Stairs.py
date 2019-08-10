from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
       
        import numpy as np
        dp = np.zeros(n+1, dtype=int)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]