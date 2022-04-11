from heapq import * 
class KthLargest:
    
    # T: O(nlogk)
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.minHeap = []
        
        # T: O(nlogk)
        for num in nums:
            if len(self.minHeap) < k:
                heappush(self.minHeap, num)
            elif num > self.minHeap[0]:
                heappop(self.minHeap)
                heappush(self.minHeap, num)                
    
    # T: O(logk)
    def add(self, val: int) -> int:
        if len(self.minHeap) < self.k:
            heappush(self.minHeap, val)
        elif  val > self.minHeap[0]:
            heappop(self.minHeap)
            heappush(self.minHeap, val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)