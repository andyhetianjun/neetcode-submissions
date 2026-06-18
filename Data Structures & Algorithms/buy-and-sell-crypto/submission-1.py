class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = 0 
        best = 0

        for i in range (1, len(prices)):
            diff = prices[i] - prices[i - 1]
            cur = max(0, cur + diff)
            best = max(best, cur)

        return best
