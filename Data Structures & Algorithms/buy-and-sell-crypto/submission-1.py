class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        #buy day
        start = 0
        #sell day
        end = 1  
        while end <= len(prices)-1:                      
            profit = prices[end] - prices[start]                
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                start = end
            end += 1
                
        return max_profit