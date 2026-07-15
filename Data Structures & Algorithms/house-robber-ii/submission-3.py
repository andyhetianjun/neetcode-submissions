class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.func(nums[1:]), self.func(nums[:-1]))
    def func(self, array):
        prev1, prev2 = 0, 0
        for n in array:
            curr = max(n + prev2, prev1)
            prev2 = prev1
            prev1 = curr
        return prev1

        
