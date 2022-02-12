from heapq import *

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        
        # consider matrix rows as m sorted lists
        for rowIdx in range(len(matrix)):
            heappush(min_heap, (matrix[rowIdx][0], 0, matrix[rowIdx]))
        
        numCount = 0
        while min_heap:
            num, idx, nums = heappop(min_heap)
            numCount += 1
            
            if numCount == k:
                return num
            
            if idx+1 < len(nums):
                heappush(min_heap, (nums[idx+1], idx+1, nums))
            