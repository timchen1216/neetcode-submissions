class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            curProfit = prices[i] - buyPrice
            profit = max(curProfit, profit)
        return profit