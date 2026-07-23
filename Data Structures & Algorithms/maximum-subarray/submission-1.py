class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        great = nums[0]
        if len(nums) == 1:
            return nums[0] 
        for i in range(len(nums)):
            if cur < 0:
                cur = 0
            cur += nums[i]
            great = max(great, cur)
        return great
            