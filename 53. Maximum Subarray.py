from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        import numpy as np

        lens = len(nums)
        dp = np.zeros(lens, dtype=int); dp[0] = nums[0]
        opt = np.zeros(lens, dtype=int); opt[0] = nums[0]

        for i in range(1, lens):
            opt[i] = max(opt[i-1], dp[i-1]+nums[i], nums[i])
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return opt[lens-1]


