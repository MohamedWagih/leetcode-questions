from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        min_heap = []
        
        for num1 in nums1[:k]:
            for num2 in nums2[:k]:
                pair_sum = num1 + num2
                if len(min_heap) < k:
                    heappush(min_heap, (-pair_sum, [num1, num2]))
                else:
                    if pair_sum > -min_heap[0][0]:
                        break
                    else:
                        heappop(min_heap)
                        heappush(min_heap, (-pair_sum, [num1, num2]))
        while min_heap:
            result.append(heappop(min_heap)[1])
        
        return result