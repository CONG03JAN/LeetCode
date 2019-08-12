from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for num in nums1:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1

        res = []
        
        for num in nums2:
            if num in dic and dic[num] > 0:
                res.append(num)
                dic[num] -= 1

        return res