class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1, 0, -1):
            print(i)
            max_profit = max(max_profit, prices[i] - min(prices[0:i]))
        return max_profit