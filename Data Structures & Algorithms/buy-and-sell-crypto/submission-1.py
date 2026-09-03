class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxD = 0
        minD = prices[0]

        for p in prices:
            maxD = max(maxD, p - minD)
            minD = min(minD, p)

        return maxD    