class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            start = i
            end = len(prices) - 1
            while start <= end:            
                profit = prices[end] - prices[start]                
                if profit > 0:
                    max_profit = max(max_profit, profit)
                end -= 1
                
        return max_profit