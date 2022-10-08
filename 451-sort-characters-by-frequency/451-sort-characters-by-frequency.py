import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        max_heap = []
        
        for c, f in freq.items():
            heapq.heappush(max_heap, [-f, c])
        
        output = ''        
        while max_heap:
            f, c = heapq.heappop(max_heap)

            output += c*-f
            
        return output
            