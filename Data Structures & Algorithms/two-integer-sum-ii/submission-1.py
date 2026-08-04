class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            r = i + 1
            while r <= len(numbers) - 1:
                if numbers[i] + numbers[r] == target:
                    return [i + 1, r + 1]
                r += 1 