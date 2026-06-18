class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        most = 0 

        for i in range (len(prices)):
            most = max(most, prices[i] - buy)
            buy = min(buy, prices[i])

        return most
