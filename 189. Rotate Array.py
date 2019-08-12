from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)

        start = 0
        tmp = nums[start]

        for i in range(lens):
           
            tmp1 = nums[k % lens]
            nums[k % lens] = tmp
            tmp = tmp1

            start = (k * (i + 2)) % lens

        