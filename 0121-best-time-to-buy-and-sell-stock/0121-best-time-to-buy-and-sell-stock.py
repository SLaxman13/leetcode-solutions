class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ma = 0
        mi = prices[0]
        for i in prices:
            if i < mi:
                mi = i
            profit = i - mi
            if profit > ma:
                ma = profit
        return ma