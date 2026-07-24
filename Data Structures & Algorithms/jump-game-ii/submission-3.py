class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}
        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(nums) - 1:
                cache[i] = 0 
                return 0 
            if nums[i] == 0:
                cache[i] = float('inf')
                return float('inf')
            end = min(len(nums), i + nums[i] + 1)
            res = float('inf')
            for j in range(i + 1, end):
                res = min(res, 1 + dfs(j))
            cache[i] = res
            return res        
        return dfs(0)