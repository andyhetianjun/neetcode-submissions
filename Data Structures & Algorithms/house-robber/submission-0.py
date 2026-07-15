class Solution:
    def rob(self, nums: List[int]) -> int:
        totalEven = 0 
        totalOdd = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                totalEven += nums[i]
            else:
                totalOdd += nums[i]
            
        return max(totalEven, totalOdd)
