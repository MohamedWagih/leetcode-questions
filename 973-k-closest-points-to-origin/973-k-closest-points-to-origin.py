from heapq import *
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            origin_distance = sqrt( x*x + y*y)
            if len(maxHeap) < k:
                heappush(maxHeap, (-origin_distance,[x, y]))
            elif origin_distance < -maxHeap[0][0]:
                heappop(maxHeap)
                heappush(maxHeap, (-origin_distance,[x, y]))
        
        output = []
        while maxHeap:
            origin_distance, point = maxHeap.pop()
            output.append(point)
        
        return output
