import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1

        heap =[]
        for key, val in mp.items():
            if len(heap) < k or val > heap[0][0]:
                heapq.heappush(heap, [val, key])
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]


