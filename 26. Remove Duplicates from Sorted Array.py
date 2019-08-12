from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        end = 1

        while start < len(nums):
            while end < len(nums):
                if nums[end] == nums[start]:
                    end += 1
                else:
                    break
            
            nums[start:end] = [nums[start]]

            start += 1
            end = start + 1

        return end - 1
            
        

