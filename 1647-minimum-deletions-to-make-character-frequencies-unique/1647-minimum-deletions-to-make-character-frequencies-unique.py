from heapq import *
class Solution:
    # time: o(n + nlogn) | space: O(n)
    def minDeletions(self, s: str) -> int:
        
        # O(n)
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # O(nlogn)
        min_heap = []
        for char in freq:
            heappush(min_heap, [freq[char], char])
        
        # O(nlogn)
        total_deletion= 0
        freq_set = set()
        while min_heap:
            f, c = heappop(min_heap)
            while f in freq_set:
                f -= 1
                total_deletion += 1
            if f > 0 :
                freq_set.add(f)
                
        return total_deletion
        
        
            
        