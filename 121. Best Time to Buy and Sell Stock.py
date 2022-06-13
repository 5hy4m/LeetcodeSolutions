import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        max_value = sys.maxsize
        buy = max_value
        sell = 0
        max_profit = 0
        i=0
        while i < l:
            currentPrice = prices[i]
            if currentPrice <= buy:
                buy = currentPrice
                sell = 0
                i+=1
                continue
            
            if currentPrice >= sell:
                sell = currentPrice
                currentProfit = sell - buy
                if max_profit < currentProfit:
                    max_profit = currentProfit
                i+=1
                continue
                
            i+=1
        return max_profit