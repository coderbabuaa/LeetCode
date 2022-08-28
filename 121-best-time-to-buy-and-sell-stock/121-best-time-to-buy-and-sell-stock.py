class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for p in prices[1:]:
            if p < min_price:
                min_price = p
            elif max_profit < p - min_price:
                max_profit = p - min_price
        return max_profit