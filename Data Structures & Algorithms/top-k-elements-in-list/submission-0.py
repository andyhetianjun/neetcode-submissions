class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        answer = []
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for _ in range(k):
            biggest = max(counts, key=counts.get)
            answer.append(biggest)
            del counts[biggest]
        return answer