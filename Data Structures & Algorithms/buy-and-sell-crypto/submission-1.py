class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        prof = 0
        for p in range(len(prices)):
            if prices[p] < min_price:
                min_price = prices[p]
            current_profit = prices[p] - min_price
            if current_profit > prof:
                prof = current_profit
        return prof