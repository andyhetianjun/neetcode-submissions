class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        for num, freq in counts.items():
            buckets[freq].append(num)
        answer = []
        for i in range(n, 0, -1): 
            for num in buckets[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer