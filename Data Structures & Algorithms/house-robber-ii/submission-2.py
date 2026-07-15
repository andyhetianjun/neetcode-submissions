class Solution:
    def rob(self, nums: List[int]) -> int:

        def func(array):
            prev1, prev2 = 0, 0
            for n in array:
                curr = max(n + prev2, prev1)
                prev2 = prev1
                prev1 = curr
            return prev1

        return max(nums[0], func(nums[1:]), func(nums[:-1]))
