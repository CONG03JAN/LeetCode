from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        right = len(nums) - 1
        left = 0

        while(left < right):

            mid = left + ((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        if nums[left] == target:
            return left
        else:
            return -1


s = Solution()


print(s.search([-1,0,3,5,9,12], 9))