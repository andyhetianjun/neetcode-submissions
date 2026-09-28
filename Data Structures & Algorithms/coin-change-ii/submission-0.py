from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def waysToMake(i:int, x:int ) -> int:
            if i == len(coins):
                return 1 if x == 0 else 0 
            take = 0 

            if coins[i] <= x:
                take = waysToMake(i, x - coins[i])
            skip = waysToMake(i + 1, x)
            return skip + take
        return waysToMake(0, amount)