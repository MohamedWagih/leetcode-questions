from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heappush(maxHeap, -stone)
        
        while len(maxHeap) > 1:
            s1 = -heappop(maxHeap)
            s2 = -heappop(maxHeap)
            newStone = abs(s1-s2)
            if newStone > 0:
                heappush(maxHeap, -newStone)
        
        if maxHeap:
            return -heappop(maxHeap)
        
        return 0
            