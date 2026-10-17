class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_price = profit = 0
        n=len(prices)
        for i in range(n-1,0,-1):
            sell_price = max(sell_price,prices[i])
            profit = max(profit,sell_price-prices[i-1])
        return profit
        