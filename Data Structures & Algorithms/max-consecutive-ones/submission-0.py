class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        most = 0
        count = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1 
            else:
                most = max(most, count)
                count = 0 
        
        return max(most, count)