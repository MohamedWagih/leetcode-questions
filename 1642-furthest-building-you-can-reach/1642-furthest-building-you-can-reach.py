from heapq import *
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        # to keep track of largest positive differences
        # with ladders
        min_heap = []
        
        for i in range(0, len(heights)-1):
            curr_diff = heights[i+1] - heights[i]
            if curr_diff > 0:
                # keep useing ladders if we have
                if ladders > 0:
                    ladders -= 1
                    heappush(min_heap, curr_diff)

                # if there is no ladders then try replace
                # the smallest difference ladder with bricks
                elif min_heap and curr_diff > min_heap[0]:
                    heappush(min_heap, curr_diff)
                    bricks -= heappop(min_heap)

                # no other options just use bricks
                else:
                    bricks -= curr_diff

                # if we ran out of bricks so we failed to make the last jump
                if bricks < 0:
                    return i
        
        return len(heights)-1