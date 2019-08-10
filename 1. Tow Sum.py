from typing import List

# 两边扫描，暴力求解
class Solution_1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lens = len(nums)
        # flag = False

        for r1 in range(0, lens):
            for r2 in range(r1+1, lens):
                if nums[r1] + nums[r2] == target:
                    # flag = True
                    return [r1, r2]

