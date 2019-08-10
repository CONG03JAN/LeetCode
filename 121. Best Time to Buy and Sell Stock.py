from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minBuy, maxGain = float("+inf"), 0

        for p in prices:
            maxGain = max(maxGain, p-minBuy)
            minBuy = min(minBuy, p)

        return maxGain
