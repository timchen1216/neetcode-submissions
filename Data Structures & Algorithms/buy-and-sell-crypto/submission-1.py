class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0
        for p in prices[1:]:
            buyPrice = min(buyPrice, p)
            profit = max(profit, p - buyPrice)
        return profit