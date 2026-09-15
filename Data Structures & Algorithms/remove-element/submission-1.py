class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        numElements = len(nums)
        i = 0

        while i < numElements:
            if nums[i] == val:
                nums[i] = nums[numElements - 1]
                numElements -= 1
            else:
                i += 1

        return numElements

