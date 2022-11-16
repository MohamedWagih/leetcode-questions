from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        ans = []
        max_heap = []
        
        for n, f in freq.items():
            heappush(max_heap, (-f, n))
        
        while k:
            f, n = heappop(max_heap)
            ans.append(n)
            k -= 1
        
        return ans
        