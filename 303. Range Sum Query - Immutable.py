from typing import List

# 超时
class NumArray_1:

    def __init__(self, nums: List[int]):
        dp = []; dp.append([nums[0]])
        # print(dp)
        lens = len(nums)

        for i in range(0, lens):
            for j in range(i+1, lens):
                # print(dp[-1])
                dp[-1].append(dp[-1][-1] + nums[j])
            if i+1<lens: dp.append([nums[i+1]])

        self.target = dp

    def sumRange(self, i: int, j: int) -> int:

        return self.target[i][j-i]

class NumArray:

    def __init__(self, nums: List[int]):
        
        import numpy as np
        self.dp = np.array([0])

        for d in nums:
            self.dp = np.append(self.dp, d + self.dp[-1])

    def sumRange(self, i: int, j: int) -> int:

        return self.dp[j+1] - self.dp[i]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
