from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        res = [-1, -1]
        left = 0
        n = len(nums)
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid
                right = mid
                while left > 0 and nums[left-1] == nums[left]:
                    left -= 1
                while right < n - 1 and nums[right] == nums[right+1]:
                    right += 1
                res[0] = left
                res[1] = right
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return res

