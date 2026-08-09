class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            best_profit = max(best_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return best_profit