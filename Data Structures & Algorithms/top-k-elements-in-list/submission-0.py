from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = defaultdict(int)
        for num in nums:
            store[num] += 1
        heap = list()
        heap_length = 0
        for key, value in store.items():
            heapq.heappush(heap, (value, key))
            heap_length += 1
            if heap_length > k:
                _ = heapq.heappop(heap)
        return [key for value, key in heap]