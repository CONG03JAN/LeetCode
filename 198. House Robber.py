from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = []

        for d in nums[:2]:
            dp.append(max(nums[0], d)) 

        for d in nums[2:]:
            dp.append(max(dp[-2]+d, dp[-1]))

        if dp:
            return dp[-1]
        else:
            return 0


