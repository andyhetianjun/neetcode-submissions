class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], Solution.func(nums[1:]), Solution.func(nums[:-1]))
    def func(array):
        prev1, prev2 = 0, 0
        for n in array:
            curr = max(n + prev2, prev1)
            prev2 = prev1
            prev1 = curr
        return prev1

        
